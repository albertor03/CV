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

        return user.val()['admin']

    def get_sections(self):
        menu = list()
        sections = list()
        list_menu = self.db.child("menu").get()

        for item in list_menu.val():
            menu.append(item['name'])

        for item in menu:
            section = self.db.child("sections").child(item).get()
            sections += section.val()

        return sections

    def get_section(self, section):
        sections = self.db.child('sections').child(section).get()
        return sections.val()

    def get_values(self, section):
        if section == 'configurations' or section == 'professional-summary':
            section = 'info'

        values = self.get_data(section)
        return values

    def edit_summary(self, summary):
        data = self.get_values('professional-summary')

        data[0]['summary'] = summary
        self.db.child('info').set(data)
