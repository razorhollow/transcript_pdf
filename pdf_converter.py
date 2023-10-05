#!/usr/bin/env python3

import os
import imaplib
import email
import smtplib
from docx import Document
from docx2pdf import convert
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
print('Hello World')

EMAIL = 'rob@razorhollow.com'