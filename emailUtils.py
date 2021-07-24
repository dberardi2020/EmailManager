from beeprint import pp
from imap_tools import MailBox

from credentialUtils import Credentials


class Mailbox:
    def __init__(self, initial_folder):
        credentials = Credentials.get_credentials()
        self.mailbox = MailBox('imap.gmail.com').login(credentials.username, credentials.password,
                                                       initial_folder=initial_folder)

    @classmethod
    def setFolderUnsub(cls):
        return cls("Unsubscribe")

    @classmethod
    def setFolderInbox(cls):
        return cls("INBOX")

    def printAllMessages(self):
        for msg in self.mailbox.fetch():
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
        pp(self.flags)
