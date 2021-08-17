from imap_tools import MailBox
from credentialUtils import Credentials
import logging


class Mailbox:
    def __init__(self, initial_folder):
        credentials = Credentials.get_credentials()
        self.mailbox = MailBox('imap.gmail.com').login(credentials.username, credentials.password,
                                                       initial_folder=initial_folder)
        logging.info('Mailbox created')
        self.messageList = self.mailbox.fetch()

    @classmethod
    def Unsub(cls):
        return cls("Unsubscribe")

    @classmethod
    def Inbox(cls):
        return cls("INBOX")

    def getSenders(self):
        senders = []

        for msg in self.messageList:
            senders.append(msg.from_)

        return senders

    def printAllMessages(self):
        for msg in self.messageList:
            message = Message(msg)
            message.print()

    def printAllFolders(self):
        for folder in self.mailbox.folder.list():
            print(folder)


class Message:
    def __init__(self, msg):
        self.subject = msg.subject.encode("ascii", "ignore").decode()
        self.from_ = msg.from_
        self.headers = msg.headers
        self.flags = msg.flags

    def print(self):
        print(self.from_, " -- ", self.subject)