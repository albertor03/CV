import datetime

from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

from getData import Data

# App initialization
app = Flask(__name__)

# Data
d = Data()
info = d.get_data('https://cv-flask.firebaseio.com/info.json')
employment = d.get_data('https://cv-flask.firebaseio.com/employment.json')
last_employment = d.get_last_employment('https://cv-flask.firebaseio.com/employment.json')
education = d.get_data('https://cv-flask.firebaseio.com/education.json')
course = d.get_data('https://cv-flask.firebaseio.com/course.json')
skill = d.get_data('https://cv-flask.firebaseio.com/skills.json')

# Variables
date = datetime.datetime.now().strftime("%Y")


# Routes
@app.route("/")
def index():
    return render_template("index.html", info=info, employment=employment, last=last_employment,
                           education=education, course=course, skill=skill, date=date)


@app.route("/jobs")
def jobs():
    return render_template("jobs.html", info=info, jobs=employment)


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        users = d.get_user()
        user = request.form['InputUser'] == users['user']

        if user and check_password_hash(users['password'], request.form['InputPassword']):
            return render_template("/admin/admin_login.html", info=info, alert_d="", alert_s="You're logged in.")
        return render_template("/admin/admin_login.html", info=info,
                               alert_d="Your credentials are invalid, check and try again.")
    return render_template("/admin/admin_login.html", info=info, alert_d='', alert_s='')


@app.route("/dashboard")
def dashboard():
    return render_template("/admin/admin_dashboard.html", info=info)

if __name__ == "__main__":
    app.run(debug=True)
