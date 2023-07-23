from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# make an instance of Flask to use in development API
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"

db = SQLAlchemy(app)


class ToDoTask(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.TEXT)
    due_to = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, due_to, description=""):
        if isinstance(description, str):
            if description.strip() != "":
                self.description = description.strip()
            else:
                self.description = None

        self.title = title.strip()
        self.due_to = datetime.strptime(due_to, "%Y-%m-%d")
        self.created_at = datetime.now()

    @property
    def end_date(self):
        return self.due_to.strftime("%d-%m-%Y")

    @property
    def is_due(self):
        return self.due_to >= datetime.now()


@app.route("/")
def index():
    task = ToDoTask.query.order_by(ToDoTask.created_at.desc()).all()
    return render_template('home.html', title="Home Page", tasks=task)


@app.route("/post_task", methods=['POST'])
def post_task():
    title = request.form.get("title")
    desc = request.form.get("desc", '')
    date  = request.form.get("date")
    try:
        task = ToDoTask(title, date, desc)
        db.session.add(task)
        db.session.commit()
    except Exception as error:
        print(error)
    return redirect('/')
