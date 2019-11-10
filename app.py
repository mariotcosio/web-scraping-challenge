from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scraper():
    mars = mongo.db.mars_data
    mars_data = mars.scrape()
    mars.update({}, mars_data, upset=True)
    return redirect("https://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)