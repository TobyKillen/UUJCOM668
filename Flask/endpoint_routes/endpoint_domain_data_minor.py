from __main__ import app
from flask import make_response, jsonify, request
from pymongo import MongoClient
import os
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta





client = MongoClient("mongodb://127.0.0.1:27017")
DOMAIN_CSV_FOLDER =  str(os.getcwd()) + '/domain_information/'
app.config['DOMAIN_CSV_FOLDER'] = DOMAIN_CSV_FOLDER
Last_Three_Months = date.today() + relativedelta(months=-3)

current_DateTime = datetime.datetime.now()
current_date = current_DateTime.date()
current_year = str(current_date.strftime("%Y"))

mongo_database = client.Domain
mongo_domain = mongo_database.Domain
mongo_configuration = mongo_database.Configuration

@app.route("/api/v1/domain-data-minor", methods=["GET"])
def get_domain_data_minor():
    if request.method == "GET":
        live_domain = 0
        mx_record_domain = 0
        spf_record = 0
        dta_domain = 0
        total_domain = 0
        registered_ytd = 0
        

        for domain in mongo_domain.find():
            total_domain += 1
            if "Live" in domain['State']:
                live_domain += 1

            if "Yes" in domain['MX Record']:
                mx_record_domain += 1

            if "DTA - High Risk" in domain['Tags']:
                dta_domain += 1

            if current_year in domain['Registered Date']:
                registered_ytd += 1

            if domain['SPF Record'] != "":
                spf_record += 1
 
        domain_data = {"live_domain": str(live_domain),
            "mx_record_domain" :str(mx_record_domain),
            "spf_record_domain": str(spf_record),
            "total_domain": str(total_domain),
            "registered_ytd": str(registered_ytd),
            "dta_domain": str(dta_domain)}
        
        return make_response(jsonify(domain_data), 200)