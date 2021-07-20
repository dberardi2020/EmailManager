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

            data = {
                "username": username,
                "password": password,
            }

            with open('credentials.json', 'w') as outfile:
                json.dump(data, outfile)
        else:
            data = json.load(open("credentials.json"))
            username = data["username"]
            password = data["password"]

        return Credentials(username, password)
