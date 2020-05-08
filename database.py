import firebase_admin
from firebase_admin import credentials
import requests

cred = credentials.Certificate("database/cv-flask-firebase-adminsdk-hh9s9-f13a390c3e.json")
firebase_admin.initialize_app(cred)

x = requests.get('https://cv-flask.firebaseio.com/course.json').text
print(x)
