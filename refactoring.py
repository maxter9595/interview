import email
import smtplib
import imaplib
from email.header import Header
from email.message import Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailClient:
    def __init__(self, login: str, password: str,
                 subject: str, recipients: list,
                 message: str, header: Header = None,
                 smtp_server: str = 'smtp.gmail.com',
                 imap_server: str = 'imap.gmail.com'):
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header
        self.smtp_server = smtp_server
        self.imap_server = imap_server

    def send_email(self) -> None:
        """
        Отвечает за отправку писем.
        """

        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))

        with smtplib.SMTP(self.smtp_server, 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.login, self.password)
            server.sendmail(self.login, self.recipients, msg.as_string())

    def receive_email(self) -> Message:
        """
        Отвечает за получение писем.

        Выводной параметр:
        Message: сообщение, содержащееся в полученном письме.
        """

        with imaplib.IMAP4_SSL(self.imap_server) as mail:
            mail.login(self.login, self.password)
            mail.list()
            mail.select("inbox")

            criterion = '(HEADER Subject "%s")' % self.header \
                if self.header else 'ALL'

            _, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'

            latest_email_uid = data[0].split()[-1]
            _, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            return email.message_from_bytes(data[0][1])


if __name__ == "__main__":
    email_client = EmailClient(
        login='login@gmail.com',
        password='qwerty',
        subject='Subject',
        recipients=['vasya@email.com', 'petya@email.com'],
        message='Message'
    )

    email_client.send_email()
    email_message = email_client.receive_email()
