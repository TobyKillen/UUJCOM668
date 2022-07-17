from flask import Flask, abort, make_response, redirect, render_template, request, url_for, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os



app = Flask(__name__)
CORS(app)
client = MongoClient("mongodb://127.0.0.1:27017")
DOMAIN_CSV_FOLDER =  str(os.getcwd()) + '/domain_information/'
app.config['DOMAIN_CSV_FOLDER'] = DOMAIN_CSV_FOLDER

mongo_database = client.Domain
mongo_domain = mongo_database.Domain
mongo_configuration = mongo_database.Configuration



from endpoint_routes import template
from endpoint_routes import test_route
from endpoint_routes import endpoint_domain_data_minor


if __name__ == "__main__":
    app.run(debug=True)



