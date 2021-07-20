from os import path
import json


class Credentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def print(self):
        print("Username: ", self.username)
        print("Password: ", self.password)

    @staticmethod
    def get_credentials():
        if not path.exists("credentials.json"):
            username = input("Username: ")
            password = input("Password: ")

            credentials = Credentials(username, password)

            with open('credentials.json', 'w') as outfile:
                json.dump(credentials.__dict__, outfile)

            return credentials
        else:
            credentials = json.load(open("credentials.json"))
            return Credentials(**credentials)
