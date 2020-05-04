from flask import Flask, render_template

from getData import Data

app = Flask(__name__)


@app.route("/")
def index():
    d = Data()
    info = d.get_data('data/info.json')
    summary = d.get_data('data/sections/summary.json')
    employment = d.get_data('data/sections/employment.json')
    return render_template("index.html", info=info, summary=summary, employment=employment)


app.run(debug=True)
