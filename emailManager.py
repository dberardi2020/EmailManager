from imap_tools import MailBox
from tinydb import TinyDB, Query
from credentialUtils import Credentials
from stats import Stats
import logging

# Set up logging, db, and stats
logging.basicConfig(level=logging.DEBUG)
db = TinyDB('db.json')
stats = Stats()

# For debugging docker
logging.info("Start of Execution")

# Load credentials, obtain if needed
credentials = Credentials.get_credentials()
logging.info("Successfully retrieved credentials")

# Initialize Unsubscribe mailbox
mailbox = MailBox('imap.gmail.com').login(credentials.username, credentials.password,
                                          initial_folder="Unsubscribe")
# Local cache for messages
mail = mailbox.fetch()

logging.info("Logged into Gmail successfully")

# Populate db with new email addresses to unsub from
for msg in mail:
    mailbox.delete(msg.uid)
    if db.contains(Query().email == msg.from_):
        logging.info(f"{msg.from_} already in DB")
    else:
        logging.info(f"Adding {msg.from_} to DB")
        db.insert({'email': msg.from_})
        stats.incUnsubsAdded()

# Set current mailbox folder to Inbox
mailbox.folder.set("INBOX")

mail = mailbox.fetch()

# Delete all emails in inbox if they match
# any email address found in the db
for msg in mail:
    logging.info(f"Checking email: {msg.from_}")
    stats.incEmailsChecked()
    if db.contains(Query().email == msg.from_):
        logging.info(f"Deleting email")
        mailbox.delete(msg.uid)
        stats.incEmailsDeleted()

stats.report()

logging.info("Operation completed successfully")
