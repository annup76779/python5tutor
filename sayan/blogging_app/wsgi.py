from flask import Flask, render_template

# make a Flask class instance so that we can map URL routes to python function
app = Flask(__name__)


# write view function
@app.route("/")
def index():
    return render_template("index.html", title="Blog List")