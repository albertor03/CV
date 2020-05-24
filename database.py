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
d = {
    "user": user,
    "password": hashed_pass
}
"""d = [
    {
        "courses": [
            {
                "academy": "academy",
                "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit "
                               "finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla "
                               "luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris "
                               "hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh"
                               " convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. "
                               "Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer "
                               "mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt "
                               "massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi,"
                               " eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
                "end-date": "2000-01-01",
                "id": "python-course-title-1",
                "id-course": 1,
                "title": "course title #1",
                "url-certificate": "#"
            }
        ],
        "id": 1,
        "section": "python"
    },
    {
        "courses": [
            {
                "academy": "academy",
                "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit "
                               "finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla "
                               "luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris "
                               "hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh "
                               "convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. "
                               "Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer "
                               "mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt "
                               "massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, "
                               "eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
                "end-date": "2000-01-01",
                "id": "jenkins-course-title-1",
                "id-course": 1,
                "title": "course title #1",
                "url-certificate": "#"
            },
            {
                "academy": "academy",
                "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit "
                               "finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla "
                               "luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris "
                               "hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim nibh "
                               "convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. "
                               "Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer "
                               "mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt "
                               "massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi, "
                               "eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
                "end-date": "2000-01-01",
                "id": "jenkins-course-title-2",
                "id-course": 2,
                "title": "course title #2",
                "url-certificate": "#"
            }
        ],
        "id": 2,
        "section": "jenkins"
    },
    {
        "courses": [
            {
                "academy": "academy",
                "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit"
                               " finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla "
                               "luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris "
                               "hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim "
                               "nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. "
                               "Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer "
                               "mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt "
                               "massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi,"
                               " eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
                "end-date": "2000-01-01",
                "id": "angular-course-title-1",
                "id-course": 1,
                "title": "course title #1",
                "url-certificate": "#"
            },
            {
                "academy": "academy",
                "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit"
                               " finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla "
                               "luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris "
                               "hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim "
                               "nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. "
                               "Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer "
                               "mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt "
                               "massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi,"
                               " eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
                "end-date": "2000-01-01",
                "id": "angular-course-title-2",
                "id-course": 2,
                "title": "course title #2",
                "url-certificate": "#"
            },
            {
                "academy": "academy",
                "description": "Aliquam malesuada turpis non cursus vulputate. Nam finibus nulla eu sapien suscipit"
                               " finibus. Etiam id fringilla massa. Sed elementum rutrum sapien, eu gravida nulla "
                               "luctus eget. Pellentesque sed mattis justo. Pellentesque nec eleifend leo. Mauris "
                               "hendrerit s vulputate lectus, sit amet dapibus eros blandit vitae. Ut dignissim "
                               "nibh convallis hendrerit pretium. Vivamus fringilla odio et interdum ullamcorper. "
                               "Pellentesque ipsum elit, porttitor vel posuere id, semper sit amet diam. Integer "
                               "mauris orci, laoreet at viverra aliquet, malesuada non justo. Aliquam id tincidunt "
                               "massa. Nulla aliquam, felis sit amet tincidunt consectetur, lectus libero mollis mi,"
                               " eu euismod erat nulla in lacus. Donec hendrerit luctus lorem eget elementum.",
                "end-date": "2000-01-01",
                "id": "angular-course-title-3",
                "id-course": 3,
                "title": "course title #3",
                "url-certificate": "#"
            }
        ],
        "id": 3,
        "section": "angular"
    }
]

db.child('courses-certifications').set(d)

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

data = db.child("employment-history").child(14).remove()

print(data)
