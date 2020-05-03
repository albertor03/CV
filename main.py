from flask import Flask, render_template

from getData import Data

app = Flask(__name__)

@app.route("/")
def index():
    d = Data()
    info = d.get_data()
    return render_template("index.html", info=info)

app.run(debug=True)
