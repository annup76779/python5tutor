from flask import Flask, render_template, url_for, redirect, request
import os
from util import *

app = Flask(__name__)  # flask instance


@app.route("/index")
def index():
    stock = get_stock()
    return render_template("index.html", title="Index", heading="Menu", stock=stock)


@app.route("/order", methods=["POST"])
def order():
    name = request.form.get("name")
    items = request.form.getlist("item")
    updated_stock = list(map(float, items))
    post_update_stock, price, quantity = update_stock_list(updated_stock)
    if post_update_stock:
        update_transaction_stock(updated_stock, name, price, quantity)
        return render_template("order.html", name=name, price=price, orders=post_update_stock)
    else:
        return "Cannot place this order"
