import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'August Lay'
email['to'] = 'email@email.com'
email['subject'] = 'you won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'Tim'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@email.com', '$Test1234')
    smtp.send_message(email)
