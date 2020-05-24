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

# Variables
date = datetime.datetime.now().strftime("%Y")

app.secret_key = '12345'


# Routes
@app.route("/")
def index():
    info = d.get_data('info')
    employment = d.get_employments()
    last_employment = d.get_last_employer()
    summary = d.get_data('professional-summary')
    education = d.get_data('education')
    course = d.get_data('courses-certifications')
    skill = d.get_data('skills')

    return render_template("index.html", info=info[0], summary=summary[0], employment=employment, last=last_employment,
                           education=education, course=course, skill=skill, date=date)


@app.route("/jobs")
@app.route("/jobs/")
def jobs():

    info = d.get_data('info')
    employment = d.get_employments()

    return render_template("jobs.html", info=info[0], jobs=employment, date=date)


@app.route("/admin", methods=['GET', 'POST'])
@app.route("/admin/", methods=['GET', 'POST'])
def login():
    info = d.get_data('info')

    if request.method == 'POST':
        users = d.get_user()
        user = request.form['InputUser'] == users['user']

        if user and check_password_hash(users['password'], request.form['InputPassword']):
            session["username"] = users['user']
            flash("You're logged in.", "success")
            return redirect(url_for('dashboard_section'))

        flash("Your credentials are invalid, check and try again.", "danger")
        fixed = True
        return render_template("/admin/admin_login.html", info=info[0], fix=fixed, date=date)

    if "username" in session:
        return redirect(url_for('dashboard_section'))
    fixed = True
    return render_template("/admin/admin_login.html", info=info[0], fix=fixed, date=date)


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
    info = d.get_data('info')

    if "username" in session:
        value = d.get_sections()
        return render_template("/admin/dashboard/admin_dashboard.html", info=info[0], date=date, sections=value)

    flash("You muss log in first.", "danger")
    return render_template("/admin/admin_login.html", info=info[0])


def view_section(*args, **kwargs):
    section = request.view_args['section']
    name = d.get_breadcrumbs(section)
    return [{'text': name['name']}]


@app.route("/dashboard/sections/<string:section>")
@app.route("/dashboard/sections/<string:section>/")
@register_breadcrumb(app, '.Dashboard.Sections', '', dynamic_list_constructor=view_section)
def sections(section):
    info = d.get_data('info')

    menu = d.get_sections()

    value = d.get_data(section)
    if section == 'settings':
        value = []

    return render_template("/admin/dashboard/sections/admin_section.html", info=info[0], sections=menu, value=value,
                           date=date)


@app.route("/api/v1/edit-summary/", methods=["POST"])
def edit_summary():
    if request.form['summary'] != '':
        d.edit_summary(request.form['summary'])
        flash("Professional Summary was Updated", "success")
        return redirect(url_for('sections', section='professional-summary'))


@app.route("/api/v1/add-employment/", methods=["POST"])
def add_employment():
    if request.form['jobTitle'] != '' and request.form['employerName'] != '' and request.form['cityName'] != '' \
            and request.form['startDate'] != '' and request.form['endDate'] != '' and request.form['description'] != '':
        d.create_employment(request.form['jobTitle'], request.form['employerName'], request.form['cityName'],
                            request.form['startDate'], request.form['endDate'], request.form['description'])

        flash("The " + request.form['jobTitle'] + " was added", "success")
        return redirect(url_for('sections', section='employment-history'))


if __name__ == "__main__":
    app.run(debug=True)
