import datetime

from flask import Flask, render_template

from getData import Data

# App initialization
app = Flask(__name__)

# Data
d = Data()
info = d.get_data('data/info.json')
summary = d.get_data('data/sections/summary.json')
employment = d.get_data('data/sections/employment.json')
last_employment = d.get_last_employment('data/sections/employment.json')
education = d.get_data('data/sections/education.json')
course = d.get_data('data/sections/courses.json')
skill = d.get_data('data/sections/skills.json')

# Variables
date = datetime.datetime.now().strftime("%Y")


# Routes
@app.route("/")
def index():
    return render_template("index.html", info=info, summary=summary, employment=employment, last=last_employment,
                           education=education, course=course, skill=skill, date=date)


@app.route("/jobs")
def jobs():
    return render_template("jobs.html", info=info, jobs=employment)


app.run(debug=True)
