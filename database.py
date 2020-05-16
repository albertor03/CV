import pyrebase
from werkzeug.security import generate_password_hash, check_password_hash

firebaseConfig = {
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

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

user = 'admin'
p = '12345678'

hashed_pass = generate_password_hash(p, method="sha256")

d = [
    {
      "id": 1,
      "level": "25%",
      "title": "skill title #1"
    },
    {
      "id": 2,
      "level": "50%",
      "title": "skill title #2"
    },
    {
      "id": 3,
      "level": "75%",
      "title": "skill title #3"
    },
    {
      "id": 4,
      "level": "100%",
      "title": "skill title #4"
    },
    {
      "id": 5,
      "level": "95%",
      "title": "skill title #5"
    }
]
db.child('professional-summary').set(d)

"""menu = [
    {
        "name": "professional-summary"
    },
    {
        "name": "employment-history"
    },
    {
        "name": "education"
    },
    {
        "name": "courses-certifications"
    },
    {
        "name": "skills"
    },
    {
        "name": "configurations"
    }
]


users = db.child("menu").get()
menu = list()
section = list()

for item in users.val():
    menu.append(item['name'])

for item in menu:
    sections = db.child('sections').child(item).get()
    section += sections.val()

print(section)"""
