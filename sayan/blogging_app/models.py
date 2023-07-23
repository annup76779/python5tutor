from wsgi import db, current_app
from datetime import datetime

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image=db.Column(db.String(80))
    date_of_entry = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, image, content):
        self.title = title
        self.content = content
        self.image=image
        self.date_of_entry = datetime.now()

    def to_dict(self):
        if self.image is not None:
            image = "/static/blog_images/%s" % self.image
        else:
            image = "https://thumbs.dreamstime.com/b/blog-information-website-concept-workplace-background-text-view-above-127465079.jpg"
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            'image': image,
        }