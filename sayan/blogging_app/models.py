from wsgi import db
from datetime import datetime


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_of_entry = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.date_of_entry = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content
        }