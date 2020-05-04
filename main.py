from flask import Flask, render_template

from getData import Data

app = Flask(__name__)


@app.route("/")
def index():
    d = Data()
    info = d.get_data('data/info.json')
    summary = d.get_data('data/sections/summary.json')
    employment = d.get_data('data/sections/employment.json')
    education = d.get_data('data/sections/education.json')
    skill = d.get_data('data/sections/skills.json')
    return render_template("index.html", info=info, summary=summary, employment=employment, education=education,
                           skill=skill)


app.run(debug=True)
