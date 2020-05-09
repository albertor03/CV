import json
import requests
import pyrebase


class Data:

    def __init__(self):
        firebase_config = {
            "apiKey": "AIzaSyCHfMchjhqW_m9ARFGuxdzE2b0pABi1Bps",
            "authDomain": "cv-flask.firebaseapp.com",
            "databaseURL": "https://cv-flask.firebaseio.com",
            "projectId": "cv-flask",
            "storageBucket": "cv-flask.appspot.com",
            "messagingSenderId": "594310230679",
            "appId": "1:594310230679:web:3eebc3f3fa3ff7a7b5efd2",
            "measurementId": "G-E2FZJVPSFE",
            "serviceAccount": "database/cv-flask-firebase-adminsdk-hh9s9-f13a390c3e.json"
        }

        self.firebase = pyrebase.initialize_app(firebase_config)

    @staticmethod
    def get_data(path):
        x = requests.get(path).text

        data = json.loads(x.replace("null,", ""))

        return data

    def get_last_employment(self, path):
        data = self.get_data(path)
        last = list()
        employment = list()

        for items in data:
            for item in items['section']:
                last += item.values()

        employment.append(last[-2])
        employment.append(last[-5])

        return employment

    def get_user(self):

        db = self.firebase.database()
        user = db.child("users").get()

        return user.val()['admin']
