import datetime

from flask import Flask, render_template, request, redirect, url_for, flash, session, escape
from werkzeug.security import generate_password_hash, check_password_hash

from getData import Data

# App initialization
app = Flask(__name__)

# Data
d = Data()
info = d.get_data('https://cv-flask.firebaseio.com/info.json')
employment = d.get_data('https://cv-flask.firebaseio.com/employment.json')

# Variables
date = datetime.datetime.now().strftime("%Y")

app.secret_key = '12345'


# Routes
@app.route("/")
def index():

    last_employment = d.get_last_employment('https://cv-flask.firebaseio.com/employment.json')
    education = d.get_data('https://cv-flask.firebaseio.com/education.json')
    course = d.get_data('https://cv-flask.firebaseio.com/course.json')
    skill = d.get_data('https://cv-flask.firebaseio.com/skills.json')

    return render_template("index.html", info=info, employment=employment, last=last_employment,
                           education=education, course=course, skill=skill, date=date)


@app.route("/jobs")
@app.route("/jobs/")
def jobs():
    return render_template("jobs.html", info=info, jobs=employment, date=date)


@app.route("/admin", methods=['GET', 'POST'])
@app.route("/admin/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = d.get_user()
        user = request.form['InputUser'] == users['user']

        if user and check_password_hash(users['password'], request.form['InputPassword']):
            session["username"] = users['user']
            flash("You're logged in.", "success")
            return redirect(url_for('dashboard_section'))

        flash("Your credentials are invalid, check and try again.", "danger")
        return render_template("/admin/admin_login.html", info=info, date=date)

    if "username" in session:
        return redirect(url_for('dashboard_section'))
    fixed = True
    return render_template("/admin/admin_login.html", info=info, fix=fixed, date=date)


@app.route("/logout")
@app.route("/logout/")
def logout():
    session.pop("username", None)
    return redirect(url_for('login'))


@app.route("/dashboard/")
@app.route("/dashboard")
def dashboard():
    return redirect(url_for('dashboard_section'))


@app.route("/dashboard/sections")
@app.route("/dashboard/sections/")
def dashboard_section():
    if "username" in session:
        value = d.get_sections()
        return render_template("/admin/admin_dashboard.html", info=info, sections=value)

    flash("You muss log in first.", "danger")
    return render_template("/admin/admin_login.html", info=info)


@app.route("/dashboard/sections/<string:section>")
@app.route("/dashboard/sections/<string:section>/")
def sections(section):
    menu = d.get_sections()
    value = d.get_section(section)
    fixed = True
    return render_template("/admin/admin_section.html", info=info, sections=menu, fix=fixed)


if __name__ == "__main__":
    app.run(debug=True)
