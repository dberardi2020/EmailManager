from beeprint import pp

class Mailbox:
    def __init__(self):

class Message:
    def __init__(self, msg):
        self.subject = msg.subject.encode("ascii", "ignore").decode()
        self.from_ = msg.from_
        self.headers = msg.headers
        self.flags = msg.flags

    def print(self):
        print(self.from_, " -- ", self.subject, "\n")
        pp(self.flags)
