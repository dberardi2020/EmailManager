import logging


class Stats:
    def __init__(self):
        self._emailsChecked = 0
        self._emailsDeleted = 0
        self._unsubsAdded = 0

    def incEmailsChecked(self):
        self._emailsChecked += 1

    def incEmailsDeleted(self):
        self._emailsDeleted += 1

    def incUnsubsAdded(self):
        self._unsubsAdded += 1

    def report(self):
        logging.info(f"Total Unsubscribes: {self._unsubsAdded}")
        logging.info(f"Total Emails Checked: {self._emailsChecked}")
        logging.info(f"Total Emails Deleted: {self._emailsDeleted}")

