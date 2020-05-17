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
      "address": "Quito, Ecuador",
      "cell-phone": [{
        "number": "+593 96 273 7459",
        "url": "https://api.whatsapp.com/send?phone=593962737459&text=Hola%20te%20contacto%20desde%20tu%20sitio%20web,%20quisiera%20hacerte%20una%20consulta."
      }],
      "email": "alberto.zapata.orta@gmail.com",
      "first-name": "Alberto Jose",
      "github": "https://www.github.com/albertor03/",
      "id": 1,
      "last-name": "Zapata Orta",
      "linkedin": "https://www.linkedin.com/in/alberto-zapata-orta",
      "skype" :"albertor03",
      "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam a eros commodo, consectetur nibh faucibus, egestas orci. Curabitur tincidunt diam quam, nec sollicitudin magna pharetra sed. Vivamus accumsan egestas libero a finibus. Maecenas nec eros a orci tempor pretium et et nulla. Mauris sit amet enim in ligula tempor laoreet. Donec aliquam, sapien at eleifend laoreet, arcu tellus iaculis sem, tincidunt consectetur lacus mauris id odio. Fusce egestas nisl leo. Ut sagittis ante luctus nibh efficitur commodo. Sed sed mauris lorem. Aenean diam urna, sollicitudin at augue a, volutpat pulvinar neque. Vivamus facilisis tellus fringilla augue commodo luctus ut et augue. Sed convallis ipsum id dolor dignissim iaculis. Donec enim elit, viverra nec sollicitudin non, hendrerit ac massa."
    }
]
db.child('info').set(d)

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
