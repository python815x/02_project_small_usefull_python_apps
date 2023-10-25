from email.message import EmailMessage
from code import code
import ssl
import smtplib

email_sender = '' # add your email address
email_password = code
email_receiver = 'modspmqehqbuvrsvxp@cazlq.com'

subject = 'test'
body = """
    rtm is the best
"""

message = EmailMessage()
message['From'] = email_sender
message['To'] = email_receiver
message['Subject'] = subject
message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, message.as_string())

