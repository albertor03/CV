from pkgutil import get_data

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

        firebase = pyrebase.initialize_app(firebase_config)
        self.db = firebase.database()

    def get_data(self, section):
        data = self.db.child(section).get()

        return data.val()

    def get_breadcrumbs(self, breadcrumb):
        breadcrumbs = list()
        data = self.get_data('sections')

        for item in data:
            if item['id'] == breadcrumb:
                breadcrumbs = item

        return breadcrumbs

    def get_employments(self):
        i = 0
        employments = list()
        employment_list = list()

        data = self.db.child('employment-history').get()

        for item in data.val():
            i += 1
            employments.append(item)
            if i == 5:
                employment_list.append(list(employments))
                employments.clear()
                i = 0

        return employment_list
    
    def get_last_employer(self):
        last = list()
        data = self.get_employments()

        last.append(data[-1:][0][-1:][0]['title'])
        last.append(data[-1:][0][-1:][0]['employer'])
        
        return last

    def get_user(self):
        user = self.db.child("users").get()

        return user.val()

    def get_sections(self):
        menu = list()
        sections = list()
        list_menu = self.db.child("sections").get()

        for item in list_menu.val():
            menu.append(item['name'])

        for item in menu:
            section = self.db.child("sections").child(item).get()

        return list_menu.val()

    def edit_summary(self, summary):
        data = self.get_data('professional-summary')

        data[0]['summary'] = summary
        self.db.child('professional-summary').set(data)

    def create_employment(self, title, employer, city, start, end, description):
        section = 'employment-history'
        employments = self.get_data(section)

        data = {
            "city": city,
            "description": description,
            "employer": employer,
            "end-date": end,
            "id": len(employments) + 1,
            "start-date": start,
            "title": title
        }

        employments.append(data)
        self.db.child(section).set(employments)
