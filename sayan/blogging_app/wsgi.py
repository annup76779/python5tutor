from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# make a Flask class instance so that we can map URL routes to python function
app = Flask(__name__)
# in flask you get a builtin dictionary for flask configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# migrate helps us to make the verison of database and then move from 
# one version of database to any older verison of database while 
# development and also makes it easy to create and handle database.


from models import *


# write view function
@app.route("/")
def index():
    all_blogs = Blog.query.all() # select * from blog;
    return render_template("index.html", title="Blog List", blogs = [
        blog.to_dict() for blog in all_blogs
    ])


@app.route("/add_blog")
def add_blog():
    return render_template("add_blog.html", form_title="Add blog")


@app.route("/upload_blog", methods=["POST"])
def update_blog():
    title_of_blog = request.form.get("title")
    body_of_blog = request.form.get("body")
    
    #saving data to database
    blog = Blog(title = title_of_blog, content = body_of_blog)
    db.session.add(blog)

    db.session.commit()

    return redirect("add_blog")
