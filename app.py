#Import Dependencies
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

#Setup Mongo
conn = "mongodb://localhost:27017"
client=pymongo.MongoClient(conn)

#Connect to Mongo db and collection
db = client.mars_db
collection = db.info

#Create Instance for Flask app
app = Flask(__name__)

#Create route that renders index.html
@app.route("/")
def index():
    info=list(collection.find())
    return render_template("index.html", info=info)

@app.route("/scrape")
def scraper():
    collection.drop()
    mars_info = scrape_mars.scrape()
    collection.insert_one(mars_info)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)