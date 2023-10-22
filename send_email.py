import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from generate_code import *
# Email configuration

random_number=generate()
def send(recipient_email,rand_num=random_number):
    
    sender_email = "wmunyua4@gmail.com"
    recipient_email = recipient_email
    subject = "E-library Code "
    message = f"Hello,\nHere is your code: \t {random_number}"

    # Create the email content
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    # Attach the message
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    smtp_server = "smtp.gmail.com"  # Use your email provider's SMTP server
    smtp_port = 587  # Use the appropriate port for your email provider
    smtp_username = "wmunyua4@gmail.com"
    smtp_password = "hmmvqjihdnxrlsdb"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Use TLS (Transport Layer Security)
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

    print("Email sent successfully")


