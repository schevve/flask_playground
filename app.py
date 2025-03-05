from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    db = sqlite3.connect("db/catalogue.db")
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    catalogue = cur.execute("SELECT * FROM catalogue")
    return render_template("index.html", catalogue=catalogue)

@app.route("/addnewitem", methods=["POST"])
def add_new_item():
    db = sqlite3.connect("db/catalogue.db")

    values = request.form
    name = values["name"]
    price = values["price"]
    data = (name, price)
    cur = db.cursor()
    cur.execute("INSERT INTO catalogue (name, price, stock) VALUES (?,?, 0)", data)
    db.commit()
    return redirect("/")
