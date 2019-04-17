# MISSION TO ~M A R S~ FLASK SITE

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()
    print(f'Mars data is... {mars_data}')
    # Return template and data
    return render_template("mars.html", mars_mongo=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function // 
    mars_mongo = mission_to_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_mongo, upsert=True)

    # Redirect back to home page
    return render_template('mars.html', mars_mongo=mars_mongo)


if __name__ == "__main__":
    app.run(debug=True)