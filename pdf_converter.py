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

def clear():
  os.system('cls' if os.name == 'not' else 'clear')

EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')
SUPERVISOR_EMAIL = config('SUPERVISOR_EMAIL')

#Connect to Gmail and Download Attachments
clear()
print("Logging into mail...")
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(EMAIL, PASSWORD)
mail.select('inbox')
status, message_numbers = mail.search(None, '(UNSEEN)', f'(FROM "{SUPERVISOR_EMAIL}")')

if status != 'OK' :
  print("Error searching for emails.")
  exit()

for message_number in message_numbers[0].split():
  resp, data = mail.fetch(message_number, '(RFC822)')
  email_body = data[0][1]
  mail_info = email.message_from_bytes(email_body)

print(f"{len(message_numbers[0].split())} emails found")
