from flask import Flask, render_template

from getData import Data

app = Flask(__name__)


d = Data()
info = d.get_data('data/info.json')
summary = d.get_data('data/sections/summary.json')
employment = d.get_data('data/sections/employment.json')
education = d.get_data('data/sections/education.json')
course = d.get_data('data/sections/courses.json')
skill = d.get_data('data/sections/skills.json')


@app.route("/")
def index():
    return render_template("index.html", info=info, summary=summary, employment=employment, education=education,
                           course=course, skill=skill)


@app.route("/jobs")
def jobs():
    return render_template("jobs.html", info=info, jobs=employment)


app.run(debug=True)
