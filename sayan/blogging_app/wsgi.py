from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# make a Flask class instance so that we can map URL routes to python function
app = Flask(__name__)
# in flask you get a builtin dictionary for flask configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)
from models import *

with app.app_context():
    db.create_all() # create all the new tables that were not already existing

# write view function
@app.route("/")
def index():
    all_blogs = Blog.query.all() # select * from blog;
    return render_template("index.html", title="Blog List", blogs = [
        blog.to_dict() for blog in all_blogs
    ])