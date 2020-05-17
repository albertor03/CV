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

"""d = [
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 1,
        "title": "job title #1",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 2,
        "title": "job title #2",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 3,
        "title": "job title #3",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 4,
        "title": "job title #4",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 5,
        "title": "job title #5",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 6,
        "title": "job title #6",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 7,
        "title": "job title #7",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 8,
        "title": "job title #8",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 9,
        "title": "job title #9",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 10,
        "title": "job title #10",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 11,
        "title": "job title #11",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 12,
        "title": "job title #12",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 13,
        "title": "job title #13",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 14,
        "title": "job title #14",
        "start-date": "2000-01"
    },
    {
        "city": "city name",
        "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
        "employer": "employer name",
        "end-date": "2001-01",
        "id": 15,
        "title": "job title #15",
        "start-date": "2000-01"
    }
]

db.child('employment-history').set(d)

menu = [
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
]"""


users = db.child("employment-history").get()
menu = list()
employment = list()
i = 0
li = 0

for item in users.val():
    i += 1
    print(item)
    menu.append(item)
    restro = i % 5
    if restro == 0:
        employment.append(list(menu))
        menu.clear()


"""for item in menu:
    sections = db.child('sections').child(item).get()
    section += sections.val()"""

print(employment)
