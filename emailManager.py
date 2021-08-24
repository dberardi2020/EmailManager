from imap_tools import MailBox
from tinydb import TinyDB, Query
from credentialUtils import Credentials
import logging

# Set up logging and db
logging.basicConfig(level=logging.DEBUG)
db = TinyDB('db.json')

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
    if db.contains(Query().email == msg.from_):
        logging.info(f"{msg.from_} already in DB")
    else:
        logging.info(f"Adding {msg.from_} to DB")
        db.insert({'email': msg.from_})

# Purge Unsub folder
mailbox.delete([msg.uid for msg in mail])

# Set current mailbox folder to Inbox
mailbox.folder.set("INBOX")

mail = mailbox.fetch()

# Delete all emails in inbox if they match
# any email address found in the db
for msg in mail:
    logging.info(f"Checking email: {msg.from_}")
    if db.contains(Query().email == msg.from_):
        logging.info(f"Deleting email")
        mailbox.delete(msg.uid)

logging.info("Operation completed successfully")
