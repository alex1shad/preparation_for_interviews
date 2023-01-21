import email
import smtplib
import imaplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

with open('config.json', 'r') as file:
    sender, password = json.load(file).values()


class EmailWork:
    def __init__(self, message, subject, recipients):
        self.message = message
        self.subject = subject
        self.recipients = recipients

    def send_message(self):
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.login(sender, password)
        # identify ourselves to smtp gmail client
        server.ehlo()
        # secure our email with tls encryption
        server.starttls()
        # re-identify ourselves as an encrypted connection
        server.ehlo()
        server.sendmail(sender, self.recipients, msg.as_string())
        server.quit()

    def recieve_message(self, header=None):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(sender, password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    message = 'Message'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    user = EmailWork(message=message, subject=subject, recipients=recipients)
    user.send_message()
    user.recieve_message()
