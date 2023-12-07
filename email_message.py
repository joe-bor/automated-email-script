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

def get_receiver_emails():
    receiver_emails_str = os.getenv('RECEIVER_EMAILS', "")
    return [email.strip() for email in receiver_emails_str.split(",") if email]

def send_email(subject, receiver_emails, name='friend'):
    receiver_emails = get_receiver_emails()
    
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Joe - Software Engineer.", f"{sender_email}"))
    msg["To"] = ", ".join(receiver_emails)
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},
        Trying to send and automate email with code.
        I want to send automated emails to myself (and you too if you want) to constantly remind me of my goals
        and our 'small wins' to see our progress
        """
    )
    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    msg.add_alternative(
        f"""\
    <html>
      <body>
        <h1>Automated Email created with Python </h1>
        <p>Hi {name},</p>
        <p>I hope you are well.</p>
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