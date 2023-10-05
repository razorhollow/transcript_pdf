#!/usr/bin/env python3

import os
from decouple import config
import imaplib
import email
import smtplib
from docx import Document
from docx2pdf import convert
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')

#Connect to Gmail and Download Attachments
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(EMAIL, PASSWORD)
mail.select('inbox')
status, message_numbers = mail.search(None, '(UNSEEN)', '(FROM "christine@csrcourtreporting.com")')
if status != 'OK' :
  print("No new emails found!")
  exit()

for message_number in message_numbers[0].split():
  resp, data = mail.fetch(message_number, '(RFC822)')
  email_body = data[0][1]
  mail_info = email.message_from_bytes(email_body)

print(message_numbers[0].split())
