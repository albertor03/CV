import datetime

from flask import Flask, render_template, request, redirect, url_for, flash, session, escape
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from werkzeug.security import generate_password_hash, check_password_hash

from getData import Data

# App initialization
app = Flask(__name__)
Breadcrumbs(app=app)

# Data
d = Data()
info = d.get_values('info')
employment = d.get_employments()

# Variables
date = datetime.datetime.now().strftime("%Y")

app.secret_key = '12345'


# Routes
@app.route("/")
def index():
    last_employment = d.get_last_employer()
    education = d.get_data('education')
    course = d.get_data('course')
    skill = d.get_data('skills')

    return render_template("index.html", info=info[0], employment=employment, last=last_employment,
                           education=education, course=course, skill=skill, date=date)


@app.route("/jobs")
@app.route("/jobs/")
def jobs():
    return render_template("jobs.html", info=info[0], jobs=employment, date=date)


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
        fixed = True
        return render_template("/admin/admin_login.html", info=info, fix=fixed, date=date)

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
@register_breadcrumb(app, '.', 'Dashboard')
def dashboard():
    return redirect(url_for('dashboard_section'))


@app.route("/dashboard/sections")
@app.route("/dashboard/sections/")
@register_breadcrumb(app, '.Dashboard', 'Sections')
def dashboard_section():
    if "username" in session:
        value = d.get_sections()
        return render_template("/admin/dashboard/admin_dashboard.html", info=info, date=date, sections=value)

    flash("You muss log in first.", "danger")
    return render_template("/admin/admin_login.html", info=info)


def view_section(*args, **kwargs):
    section = request.view_args['section']
    name = d.get_section(section)
    return [{'text': name[0]['section']}]


@app.route("/dashboard/sections/<string:section>")
@app.route("/dashboard/sections/<string:section>/")
@register_breadcrumb(app, '.Dashboard.Sections', '', dynamic_list_constructor=view_section)
def sections(section):
    menu = d.get_sections()
    name = d.get_section(section)
    values = d.get_values(name[0]['id'])
    return render_template("/admin/dashboard/sections/admin_section.html", info=info, sections=menu, value=values,
                           date=date)


if __name__ == "__main__":
    app.run(debug=True)
