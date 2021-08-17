from imap_tools import MailBox
from tinydb import TinyDB, Query
from credentialUtils import Credentials
import logging


logging.basicConfig(level=logging.DEBUG)
db = TinyDB('db.json')

credentials = Credentials.get_credentials()
logging.info("Successfully retrieved credentials")

mailbox = MailBox('imap.gmail.com').login(credentials.username, credentials.password,
                                          initial_folder="Unsubscribe")

logging.info("Logged into Gmail successfully")

for msg in mailbox.fetch():
    if db.contains(Query().email == msg.from_):
        logging.info(f"{msg.from_} already in DB")
    else:
        logging.info(f"Adding {msg.from_} to DB")
        db.insert({'email': msg.from_})

mailbox.delete([msg.uid for msg in mailbox.fetch()])

mailbox.folder.set("INBOX")

for msg in mailbox.fetch():
    logging.info(f"Checking email: {msg.from_}")
    if db.contains(Query().email == msg.from_):
        logging.info(f"Deleting email")
        mailbox.delete(msg.uid)

logging.info("Operation completed successfully")
