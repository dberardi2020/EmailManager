from imap_tools import MailBox, AND
import emailUtils as utils
import sys

mailbox = MailBox('imap.gmail.com').login(username, password, initial_folder='INBOX')


with MailBox('imap.gmail.com').login(username, password, initial_folder='INBOX') as mailbox:
    # for msg in mailbox.fetch():
    #     message = utils.Message(msg)
    #     message.print()

    for folder in mailbox.folder.list():
        print(folder)
