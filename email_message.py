import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv  

PORT = 587  
EMAIL_SERVER = "smtp-mail.outlook.com"    # Adjust server address, if you are not using @outlook

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

# Take emails from .env
def get_receiver_emails():
    receiver_emails_str = os.getenv('RECEIVER_EMAILS', "")
    return [email.strip() for email in receiver_emails_str.split(",") if email]

def send_email(subject, name='friend'):
    receiver_emails = get_receiver_emails()
    
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Joezari - Software Engineer.", f"{sender_email}"))
    msg["To"] = ", ".join(receiver_emails)
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},
        Trying to send and automated email with code.
        
        Goals:
        - To practice and learn about different Python modules.
        - Send reminder of long-term goals
        - Reflect on achievements and appreciate progress
        
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
        <h1>Automated Email Created With Python</h1>
        <p>Hi {name},</p>
        <p>I wanted to share this automated email created with Python. It's not just an email; it's a way to practice and learn about different Python modules.</p>

        <h2>Goals:</h2>
        <ul>
            <li>Send reminders of long-term goals</li>
            <li>Reflect on achievements and appreciate progress</li>
        </ul>

        <h2>Icebox:</h2>
        <ul>
            <li>Fetch and add inspirational quotes? </li>
            <li>Fetch and display today's weather? </li>
            <li> Fetch for a random coding challenge? </li>
        </ul>

        <p>Cheers,<br>
        Joezari
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
        subject="Used Python code to send this",
    )