from typing import Counter
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import os

# creating Flask app instance
app = Flask(__name__)


# http://127.0.0.1:5000/index/first
@app.route("/index")
def index():
    return render_template("index.html")

# this is the upload route where we will submit aur image
@app.route("/upload", methods=["POST"])
def upload():
    # this line will take image uploaded
    file = request.files["image"] # it is just checking for a input named image
    if file:
        filename = secure_filename(file.filename) # remove all the unwanted things in the file
        file.save(os.path.join(
            os.path.dirname(__file__), 'static', filename
        ))
        return 'file saved successfully, go back to index page <a href="http://127.0.0.1:5000/index"> Index </a>'
    else:
        return 'Please select a file.<a href="http://127.0.0.1:5000/index"> Index </a>'


@app.route("/view", methods=["GET"]) 
def view():

    img_list = os.listdir(
        os.path.join(
            os.path.dirname(__file__), "static"
        )
    )
    # E:\Python's Tutor\python\chilion_classes\image_uploader_web_app\static

    ref = 0 # reference
    new_img_lst = []
    counter = 0

    # if the number of images in the static folder is less than 3 then new_img_lst = [["Signature.jpg", "wallpaper.jpg"]]
    while img_list != []:
        sub_img = []
        while len(sub_img) < 3 and img_list != []:
            sub_img.append(img_list.pop(0))
            counter += 1
        new_img_lst.append(sub_img)

    print(img_list)
    print(new_img_lst)

    return render_template("view.html", img_list = new_img_lst)



if __name__ == '__main__':
    app.run(debug=True)
