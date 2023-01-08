from flask import Flask, render_template, url_for, redirect, request
import os

app = Flask(__name__)  # flask instance


@app.route("/index")
def index():
    with open(os.path.join(os.path.dirname(__file__),"static", "stock.txt"), "r") as stock_list:
        stock=[]
        for line in stock_list.readlines():
            stock.append(line.split(","))
    return render_template("index.html", title="Index", heading="Menu", stock=stock)


@app.route("/order", methods=["POST"])
def order():
    name=request.form.get("name")
    items = request.form.get("item")
    return render_template("order.html")
