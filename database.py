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
        "id": "professional-summary",
        "section": "professional summary",
        "icon": "fas fa-user-alt"
    },
    {
        "id": "employment-history",
        "section": "employment history",
        "icon": "fas fa-briefcase"
    },
    {
        "id": "education",
        "section":  "education",
        "icon": "fas fa-user-graduate"
    },
    {
        "id": "courses-certifications",
        "section":  "courses & certifications",
        "icon": "fas fa-certificate"
    },
    {
        "id": "skills",
        "section":  "skills",
        "icon": "fas fa-user-alt"
    }
]

db.child('sections').set(d)

# users = db.child("sections").child("employment").get()
# print(users.val()['section'])
