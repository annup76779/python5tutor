from flask import Flask, render_template, request, redirect, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from uuid import uuid4
from werkzeug.utils import secure_filename

# make a Flask class instance so that we can map URL routes to python function
app = Flask(__name__)
# in flask you get a builtin dictionary for flask configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
app.config["SQLALCHEMY_ECHO"] = True

app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(__file__), 'static', 'blog_images')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', }

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# migrate helps us to make the verison of database and then move from 
# one version of database to any older verison of database while 
# development and also makes it easy to create and handle database.


from models import *


def is_allowed_file(filename):
    name, ext = filename.rsplit('.', 1) #  lasdfjsdka.png  -> name=lasdfjsdka, ext='png'
    if ext in app.config["ALLOWED_EXTENSIONS"]:
        new_filename = "%s.%s" %(str(uuid4()), ext)
        return new_filename, True
    else:
        return '', False


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
    image = request.files.get('image')
    print(request.files)
    filename = ''
    print(image)
    if image is not None:
        # process the image
        # is it's file extension is valid or not 
        filename, check = is_allowed_file(image.filename)
        if check:
            image.filename = secure_filename(filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        print(filename)
    
    #saving data to database
    blog = Blog(title = title_of_blog, image=filename, content = body_of_blog)
    db.session.add(blog)

    db.session.commit()

    return redirect("add_blog")
