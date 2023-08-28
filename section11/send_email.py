import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

import os
from dotenv import load_dotenv


# .envファイルの内容を読み込む
load_dotenv()

from_email = os.environ['from_email']
password = os.environ['password']

subject = 'Test send email'
body_text = 'Hello from email'
to_email = os.environ['to_email']

smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.starttls()
smtpobj.login(from_email, password)

msg = MIMEText(body_text)
msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email
msg['Date'] = formatdate()

smtpobj.send_message(msg)
smtpobj.close()
