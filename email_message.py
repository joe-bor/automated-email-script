import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv  
from quotes import quotes
from random import choice

PORT = 587  
EMAIL_SERVER = "smtp-mail.outlook.com"    # Adjust server address, if you are not using @outlook
QUOTE = choice(quotes)

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

# Turn goals into <li> elements
def get_goals():
    goals_env = os.getenv("GOALS")
    goals_list = [f"<li>{goal.strip().capitalize()}</li>" for goal in goals_env.split(',') if goal]
    return "".join(goals_list)

# Turn reflections into <li> elements
def get_reflections():
    reflections_env = os.getenv("REFLECTIONS")
    reflections_list = [f"<li>{reflection.strip().capitalize()}</li>" for reflection in reflections_env.split(',') if reflection]
    return "".join(reflections_list)

# Take emails from .env
def get_receiver_emails():
    receiver_emails_str = os.getenv('RECEIVER_EMAILS', "")
    return [email.strip() for email in receiver_emails_str.split(",") if email]

def send_email(subject, name='Future Me'):
    receiver_emails = get_receiver_emails()
    
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Joezari - Software Engineer.", f"{sender_email}"))
    msg["To"] = ", ".join(receiver_emails)
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        {QUOTE['h']}
        
        Hi {name},
        Trying to send and automated email with code.
        
        Goals:
        {get_goals()}
        
        Reflections:
        {get_reflections()}
        
        Cheers,
        Joezari
        """
    )
    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    msg.add_alternative(
        f"""\
    <html>
    <body>
        <h2>{QUOTE['h']}</h2>
        
        <p>Hi {name},</p>
        <p>I wanted to share this automated email created with Python. It's not just an email; it's a way to practice and learn about different Python modules.</p>

        <h3>Goals:</h3>
        <ul>
            {get_goals()}
        </ul>
        
        <h3>Reflections:</h3>
        <ul>
            {get_reflections()}
        </ul>

        <h3>Icebox:</h3>
        <ul>
            <li>Fetch and display today's weather? </li>
            <li> Fetch for a random coding challenge? </li>
        </ul>

        <p>Cheers,<br>
        Joezari from December 2023
        </p>
    </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_emails, msg.as_string())


if __name__ == "__main__":
    send_email(
        subject="Daily Reminder from 2023",
    )