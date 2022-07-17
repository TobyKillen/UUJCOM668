from calendar import month
from crypt import methods
from dataclasses import dataclass
from distutils.log import debug
from email.policy import default
from ipaddress import ip_address
import re
from xml import dom
from flask import Flask, abort, make_response, redirect, render_template, request, url_for, jsonify
import os
from datetime import datetime
import pandas as pandas
from pymongo import MongoClient
from werkzeug.utils import secure_filename
from datetime import datetime
from collections import Counter
from flask_cors import CORS
import csv
import json
import time
import numpy as numpy
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import dns
from dns import *
import socket
import threading
import random
from ipaddress import ip_address
from unicodedata import name
import requests
import time
import socket
from dns import resolver









app = Flask(__name__)
CORS(app)
client = MongoClient("mongodb://127.0.0.1:27017")

DOMAIN_CSV_FOLDER =  str(os.getcwd()) + '/domain_information/'
app.config['DOMAIN_CSV_FOLDER'] = DOMAIN_CSV_FOLDER

mongo_database = client.Domain
mongo_domain = mongo_database.Domain
mongo_configuration = mongo_database.Configuration



Last_Three_Months = date.today() + relativedelta(months=-3)


current_DateTime = datetime.datetime.now()
current_date = current_DateTime.date()
current_year = str(current_date.strftime("%Y"))



@app.route("/status", methods=["GET"])
def application_status():
    time_now = datetime.now()
    payload = {
        "Status" : "Web Server is running",
        "Time" : time_now
    }
    return make_response(jsonify(payload), 200)


@app.route("/", methods=["GET"])
def index():
    return make_response(jsonify(), 200)


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


@app.route("/api/v1/domain-threat-analysis")
def domain_threat_analysis():
    if request.method == "GET":
        domains = []
        payload = []
        dta_domain = []
        for domain in mongo_domain.find():
            domain['_id'] = str(domain['_id'])
            if "DTA - High Risk" in domain['Tags']:
                domains.append(domain['Domain'])

        try: 
            dta_domain.append(random.sample(domains, 6))
            for domain in dta_domain[0]:
                for domain_name in mongo_domain.find({"Domain": domain}):
                    domain_name['_id'] = str(domain_name['_id'])
                    payload.append(domain_name)
        except: 
            print("No Domains with DTA - High Risk Tag")

                  
    return make_response(jsonify(payload), 200)


@app.route("/api/v1/domain-time-series")
def domain_time_serise():
    if request.method == "GET":
        start_date = str(request.args.get('start')).strip()
        end_date = str(request.args.get('end')).strip()

        # start_date_time_frame = datetime.datetime.strptime(start_date, "%d-%m-%Y").strftime("%Y-%m-%d")
        # end_date_time_frame = datetime.datetime.strptime(end_date, "%d-%m-%Y").strftime("%Y-%m-%d")

        start_date_time_frame = str(datetime.datetime.strptime(start_date, "%Y-%m-%d"))
        end_date_time_frame = str(datetime.datetime.strptime(end_date, "%Y-%m-%d"))

        domain_dates = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if domain['Registered Date'] != "":
                domain_registered_date = domain['Registered Date'].split(" ")[0]
                if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                    domain_dates.append(domain['Registered Date'].split(" ")[0])
        AllDomainValues = Counter(domain_dates).values()

        domain_values = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if domain['Registered Date'] != "":
                domain_registered_date = domain['Registered Date'].split(" ")[0]
                if domain['Registered Date'] not in domain_values:
                    domain_registered_date = domain['Registered Date'].split(" ")[0]
                    if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                        domain_values.append(domain['Registered Date'].split(" ")[0])
        AllDomainDates = Counter(domain_values).keys()


        dta_domain_dates = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "DTA - High Risk" in domain['Tags']:
                if domain['Registered Date'] != "":
                    domain_registered_date = domain['Registered Date'].split(" ")[0]
                    if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                        dta_domain_dates.append(domain['Registered Date'].split(" ")[0])
        DTADomainDates = Counter(dta_domain_dates).keys()

        dta_domain_values = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "DTA - High Risk" in domain['Tags']:
                if domain['Registered Date'] != "":
                    if domain['Registered Date'] not in dta_domain_values:
                        domain_registered_date = domain['Registered Date'].split(" ")[0]
                        if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                            dta_domain_values.append(domain['Registered Date'].split(" ")[0])
        DTADomainValues = Counter(dta_domain_values).values()

        live_domain_dates = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "Live" in domain['State']:
                if domain['Registered Date'] != "":
                    domain_registered_date = domain['Registered Date'].split(" ")[0]
                    if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                        live_domain_dates.append(domain['Registered Date'].split(" ")[0])
        LiveDomainDates = Counter(live_domain_dates).keys()

        live_domain_values = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "Live" in domain['State']:
                if domain['Registered Date'] != "":
                    if domain['Registered Date'] not in live_domain_values:
                        domain_registered_date = domain['Registered Date'].split(" ")[0]
                        if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                            live_domain_values.append(domain['Registered Date'].split(" ")[0])
        LiveDomainValues = Counter(live_domain_values).values()

        down_domain_dates = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "Down" in domain['State']:
                if domain['Registered Date'] != "":
                    domain_registered_date = domain['Registered Date'].split(" ")[0]
                    if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                        down_domain_dates.append(domain['Registered Date'].split(" ")[0])
        DownDomainDates = Counter(down_domain_dates).keys()


        down_domain_values = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "Down" in domain['State']:
                if domain['Registered Date'] != "":
                    if domain['Registered Date'] not in down_domain_values:
                        domain_registered_date = domain['Registered Date'].split(" ")[0]
                        if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                            down_domain_values.append(domain['Registered Date'].split(" ")[0])
        DownDomainValues = Counter(down_domain_values).values()




        mx_domain_dates = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "Yes" in domain['MX Record']:
                if domain['Registered Date'] != "":
                    domain_registered_date = domain['Registered Date'].split(" ")[0]
                    if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                        mx_domain_dates.append(domain['Registered Date'].split(" ")[0])
        MXDomainDates = Counter(mx_domain_dates).keys()

        mx_domain_values = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "Yes" in domain['MX Record']:
                if domain['Registered Date'] != "":
                    if domain['Registered Date'] not in mx_domain_values:
                        domain_registered_date = domain['Registered Date'].split(" ")[0]
                        if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                            mx_domain_values.append(domain['Registered Date'].split(" ")[0])
        MXDomainValues = Counter(mx_domain_values).values()



        spf_domain_dates = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if domain['SPF Record'] != "":
                if domain['Registered Date'] not in spf_domain_dates:
                        domain_registered_date = domain['Registered Date'].split(" ")[0]
                        if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                            spf_domain_dates.append(domain['Registered Date'].split(" ")[0])
        SPFDomainDates = Counter(spf_domain_dates).keys()

        spf_domain_values = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if domain['SPF Record'] != "":
                if domain['Registered Date'] not in spf_domain_values:
                        domain_registered_date = domain['Registered Date'].split(" ")[0]
                        if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                            spf_domain_values.append(domain['Registered Date'].split(" ")[0])
        SPFDomainValues = Counter(spf_domain_values).values()
        
        virtual_takedown_dates_0 = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "Takedown Successful" in domain['Tags']:
                if domain['Registered Date'] != "":
                    domain_registered_date = domain['Registered Date'].split(" ")[0]
                    if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                        virtual_takedown_dates_0.append(domain['Registered Date'].split(" ")[0])
        VirtualTakedownDatesSuccessful = Counter(virtual_takedown_dates_0).keys()

        virtual_takedown_values_0 = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "Takedown Successful" in domain['Tags']:
                if domain['Registered Date'] != "":
                    domain_registered_date = domain['Registered Date'].split(" ")[0]
                    if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                        virtual_takedown_values_0.append(domain['Registered Date'].split(" ")[0])
        VirtualTakedownValuesSuccessful = Counter(virtual_takedown_values_0).values()


        virtual_takedown_dates_1 = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "Takedown Unsuccessful" in domain['Tags']:
                if domain['Registered Date'] != "":
                    domain_registered_date = domain['Registered Date'].split(" ")[0]
                    if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                        virtual_takedown_dates_1.append(domain['Registered Date'].split(" ")[0])
        VirtualTakedownDatesUnsuccessful = Counter(virtual_takedown_dates_1).keys()

        virtual_takedown_values_1 = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "Takedown Unsuccessful" in domain['Tags']:
                if domain['Registered Date'] != "":
                    domain_registered_date = domain['Registered Date'].split(" ")[0]
                    if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                        virtual_takedown_values_1.append(domain['Registered Date'].split(" ")[0])
        VirtualTakedownValuesUnsuccessful = Counter(virtual_takedown_values_1).values()

        virtual_takedown_dates_2 = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "Takedown Pending" in domain['Tags']:
                if domain['Registered Date'] != "":
                    domain_registered_date = domain['Registered Date'].split(" ")[0]
                    if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                        virtual_takedown_dates_2.append(domain['Registered Date'].split(" ")[0])
        VirtualTakedownDatesPending = Counter(virtual_takedown_dates_2).keys()

        virtual_takedown_values_2 = []
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if "Takedown Pending" in domain['Tags']:
                if domain['Registered Date'] != "":
                    domain_registered_date = domain['Registered Date'].split(" ")[0]
                    if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                        virtual_takedown_values_2.append(domain['Registered Date'].split(" ")[0])
        VirtualTakedownValuesPending = Counter(virtual_takedown_values_2).values()





        domain_down = 0
        domain_live = 0
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if domain['Registered Date'] != "":
                domain_registered_date = domain['Registered Date'].split(" ")[0]
                if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                    if "Live" in domain['State']:
                        domain_live += 1

                    if "Down" in domain['State']:
                        domain_down += 1

        takedown_pending = 0
        takedown_successful = 0
        takedown_unsuccessful = 0
        for domain in mongo_domain.find().sort("Registered Date", -1):
            if domain['Registered Date'] != "":
                domain_registered_date = domain['Registered Date'].split(" ")[0]
                if domain_registered_date >= start_date_time_frame and domain_registered_date <= end_date_time_frame:
                    if "Pending" in domain['Tags']:
                        takedown_pending += 1

                    if "Successful" in domain['Tags']:
                        takedown_successful += 1
                    
                    if "Unsuccessful" in domain['Tags']:
                        takedown_unsuccessful += 1
        # print(takedown_successful, takedown_unsuccessful, takedown_unsuccessful)

        payload = json.dumps({'AllDomainDates': list(AllDomainDates), 'AllDomainValues': list(AllDomainValues), 'DTADomainDates': list(DTADomainDates), 'DTADomainValues': list(DTADomainValues), 'LiveDomainDates': list(LiveDomainDates), 'LiveDomainValues': list(LiveDomainValues), "DownDomainDates": list(DownDomainDates), "DownDomainValues": list(DownDomainValues), 'MXDomainDates': list(MXDomainDates), 'MXDomainValues': list(MXDomainValues), 'SPFDomainDates': list(SPFDomainDates), "SPFDomainValues": list(SPFDomainValues), 'VirtualTakedownDatesSuccessful': list(VirtualTakedownDatesSuccessful), "VirtualTakedownValuesSuccessful": list(VirtualTakedownValuesSuccessful), "VirtualTakedownDatesUnsuccessful": list(VirtualTakedownDatesUnsuccessful), "VirtualTakedownValuesUnsuccessful": list(VirtualTakedownValuesUnsuccessful), "VirtualTakedownDatesPending": list(VirtualTakedownDatesPending), "VirtualTakedownValuesPending": list(VirtualTakedownValuesPending), "LiveDomainCount": [domain_live], "DownDomainCount": [domain_down], "TakedownPending": takedown_pending, "TakedownSuccessful": takedown_successful, "TakedownUnsuccessful": takedown_unsuccessful})
        return make_response(jsonify(payload),200)













@app.route("/api/v1/domain/<string:Domain>", methods=["GET"])
def get_single_domain(Domain):
    if request.method == "GET":
        data_to_return = []
        for Domain_Object in mongo_domain.find({"Domain": Domain}).sort("Risk Score", -1):
            if Domain_Object != "":
                Domain_Object["_id"] = str(Domain_Object["_id"])
                data_to_return.append(Domain_Object)
        return make_response(jsonify(data_to_return), 200)


@app.route("/api/v1/configuration", methods=["POST"])
def create_customer_configuration():
    if request.method == "POST":
        if request.form:
            existing_user = mongo_configuration.find({"customer_configuration_name": request.form['customer_configuration_name']}).count()
            if existing_user == 0:
                new_configuration = {
                "customer_configuration_name": request.form['customer_configuration_name'],
                "score_top_level_domain": request.form['score_top_level_domain'],
                "score_close_match": request.form['score_close_match'], 
                "score_look_alike": request.form['score_look_alike'],
                "score_email_activity": request.form['score_email_activity'],
                "score_domain_state": request.form['score_domain_state'],
                "score_mx_record": request.form['score_mx_record'],
                "score_spf_record": request.form['score_spf_record'],
                "dashboard_percentage": request.form['dashboard_percentage'],

                }
                mongo_configuration.insert_one(new_configuration)
                return make_response(jsonify({"Success!": "Customer Configuration Added"}), 200)
            else:
                return make_response(jsonify({"Alert!": "Customer Configuration Already Exists. Change Customer Name and Try Again."}), 400)
        else:
            return make_response(jsonify({"ALERT": "Missing Form Data"}), 400)


@app.route("/api/v1/configuration/<string:customer_configuration_name>", methods=["PUT"])
def update_customer_configuration(customer_configuration_name):
    if request.method == "PUT":
        if request.form:
            Configuration_Object = mongo_configuration.update_one({"customer_configuration_name": customer_configuration_name}, 
            {
                "$set": {
                "customer_configuration_name": request.form['customer_configuration_name'],
                "score_top_level_domain": request.form['score_top_level_domain'],
                "score_close_match": request.form['score_close_match'], 
                "score_look_alike": request.form['score_look_alike'],
                "score_email_activity": request.form['score_email_activity'],
                "score_domain_state": request.form['score_domain_state'],
                "score_mx_record": request.form['score_mx_record'],
                "score_spf_record": request.form['score_spf_record'],
                "dashboard_percentage": request.form['dashboard_percentage']
                }
                }
            )
            if Configuration_Object.matched_count == 1:
                return make_response(jsonify({"SUCCESS!": "Successfully Updated Configuration"}), 200)
            else:
                return make_response( jsonify( { "ALERT!":"Invalid Customer Configuration Name" } ), 404)
        else:
            return make_response( jsonify( {"ALERT!":"Missing Form Data"} ), 404)


@app.route("/api/v1/configuration/<string:customer_configuration_name>", methods=["DELETE"])
def delete_customer_configuration(customer_configuration_name):
    if request.method == "DELETE":
        Configuration_Object = mongo_configuration.delete_one({"customer_configuration_name": customer_configuration_name})
        if Configuration_Object.deleted_count == 1:
            return make_response(jsonify( {} ), 204)
        else:
            return make_response( jsonify({ "ALERT!" : "Invalid Customer Configuration Name. Please Try Again." } ), 404)
    
@app.route("/api/v1/configuration/<string:customer_configuration_name>", methods=["GET"])
def get_single_customer_configuration(customer_configuration_name):
    payload = []
    Configuration_Object = mongo_configuration.find({"customer_configuration_name": customer_configuration_name})
    if Configuration_Object != "":
        for config in Configuration_Object:
            config["_id"] = str(config['_id'])
            payload.append(config)
        return make_response(jsonify(payload), 200)
    else:
        return make_response(jsonify({"ALERT!": "Configuration not found."}), 404)
        


@app.route("/api/v1/configuration", methods=["GET"])
def get_all_customer_configuration():
    if request.method == "GET":
        payload = []
        Configuration_Object = mongo_configuration.find()
        for config in Configuration_Object:
            config["_id"] = str(config['_id'])
            payload.append(config)
        
        return make_response(jsonify(payload), 200)


@app.route("/api/v1/configuration-dropdown", methods=["GET"])
def get_configuration_UUID():
    if request.method == "GET":
        payload = []
        Configuration_Object = mongo_configuration.find()
        for config in Configuration_Object:
            config["_id"] = str(config['_id'])
            payload.append(config['customer_configuration_name'])
    
        return make_response(jsonify(payload), 200)

        

    











@app.route("/api/v1/domain", methods=["GET"])
def get_all_domain():
    if request.method == "GET":
        data_to_return = []
        for Domain_Object in mongo_domain.find().sort("Risk Score", -1):
            Domain_Object["_id"] = str(Domain_Object["_id"])
            data_to_return.append(Domain_Object)
        
        return make_response(jsonify(data_to_return), 200)

@app.route("/api/v1/domain/<string:Domain_Name>", methods=["DELETE"])
def delete_one_domain(Domain_Name):
    if request.method == "DELETE":
        Domain_Object = mongo_domain.delete_one({"Domain": Domain_Name })
        if Domain_Object.deleted_count == 1:
            return make_response( jsonify( {} ), 204)
        else:
            return make_response( jsonify({ "ALERT!" : "Invalid Domain. Please Try Again." } ), 404)

@app.route("/api/v1/domain/upload", methods=["POST"])
def upload_domain_csv():
    if request.method == "POST":
        if "Domain_CSV" in request.files:
            file_information = request.files["Domain_CSV"]
            path_of_csv = os.path.join(app.config["DOMAIN_CSV_FOLDER"], file_information.filename)
            file_information.save(path_of_csv)
            try:
                UploadDomainInformation(path_of_csv) 

                thread_process_0 = threading.Thread(target=InsertFields)
                thread_process_0.start()
                
                thread_process_2 = threading.Thread(target=FetchMXRecord)
                thread_process_2.start()

                thread_process_3 = threading.Thread(target=FetchSPFRecord)
                thread_process_3.start()


            except:
                pass
            return make_response(jsonify({"SUCCESS!": "File was Found"}), 200)
        else:
            return make_response(jsonify({"HEHE": "Something went wrong"}), 404)

@app.route("/api/v1/domain", methods=["DELETE"])
def delete_all_domain():
    if request.method == "DELETE":
        mongo_domain.delete_many({})
        return make_response(jsonify({"SUCCESS!": "Successfully Dropped All Domain's"}))

@app.route("/api/v1/risk_score/compute/<string:customer_configuration_name>", methods=["GET"])
def risk_score_compute(customer_configuration_name):
    if request.method == "GET":
        try:
            Domain_Risk_Score(customer_configuration_name)
            return make_response(jsonify({"SUCCESS!": "Risk Score Successfully Ran"}))
        except:
            return make_response(jsonify({"ALERT!":"Something went wrong running Risk Score"}))
    

@app.route("/api/v1/risk_score", methods=["GET"])
def get_risk_score():
    if request.method == "GET":
        Risk_Score_Object = []
        for Risk_Object in mongo_configuration.find({"risk_score_name": "risk_score"}):
            Risk_Object["_id"] = str(Risk_Object["_id"])
            Risk_Score_Object.append(Risk_Object)
            
        return make_response(jsonify(Risk_Score_Object))


# @app.route("/api/v1/risk_score", methods=["PUT"])
# def update_risk_score():
#     if request.method == "PUT":
#         if "score_tld" in request.form and "score_close_match" in request.form and "score_look_alike" in request.form and "score_email" in request.form and "score_state" in request.form and "score_mx" in request.form and "dashboard_percentage" in request.form:
#             Risk_Score_Object = mongo_configuration.update_one({"risk_score_name": "risk_score"},
#             {
#                 "$set": {
#                     "score_top_level_domain": request.form["score_tld"],
#                     "score_close_match": request.form["score_close_match"],
#                     "score_look_alike": request.form["score_look_alike"],
#                     "score_email_activity": request.form["score_email"],
#                     "score_domain_state": request.form["score_state"],
#                     "score_mx_record": request.form["score_mx"],
#                     "score_spf_record": request.form["score_spf"],
#                     "risk_score_margin": request.form["dashboard_percentage"]
#                 }})

#             if Risk_Score_Object.matched_count == 1:
#                 return make_response(jsonify({"SUCCESS!": "Successfully Updated Settings"}), 200)
#             else:
#                 return make_response(jsonify({"ALERT!": "Something went wrong!"}), 404)
#         else:
#             return make_response(jsonify({"ALERT!": "Missing Form Data"}), 404)






# @app.route("/", methods=["GET"])
# def dashboard():
#     if request.method == "GET":
#         Domain_Date = []
#         Domain_Values = []
#         for Domain_Object in mongo_domain.find():
#             Domain_Object = Domain_Object["Registered Date"]
#             if Domain_Object != "":
#                 Date_Object_0 = Domain_Object.split(" ")[0]
#                 Date_Object = Date_Object_0.split("-")
#                 Day = str(Date_Object[2])
#                 Month = str(Date_Object[1])
#                 Year = str(Date_Object[0])
#                 Domain_Date_0 = str(Month+"/"+Day+"/"+Year)
#                 Panda_Date = pandas.to_datetime(Domain_Date_0).strftime('%m/%d/%Y')
#                 Domain_Date.append(Panda_Date)
        
#         Domain_Dates = sorted(list(dict.fromkeys(Domain_Date)))
#         domain_count = Counter(Domain_Date).values()
#         for value in domain_count:
#             Domain_Values.append(value)

#         return render_template("application_home.html", date_data=Domain_Dates, domain_count=Domain_Values)



def Domain_Risk_Score(customer_configuration_name):
    print("Running Risk Score Parser for: {}".format(customer_configuration_name))
    Customer_Configuration = []
    for Risk_Score_Object in mongo_configuration.find({"customer_configuration_name": customer_configuration_name}):
        Customer_Configuration.append(Risk_Score_Object)

    for Domain_Document in mongo_domain.find():
        Domain_Risk_Score = 0
        Domain_Classification = Domain_Document["Classifications"]
        Domain_Channels = Domain_Document["Channels"]
        Domain_State = Domain_Document["State"]
        Domain_MX_Record = Domain_Document["MX Record"]
        Domain_SPF_Record = Domain_Document['SPF Record']

        if "TLD Attack" in Domain_Classification:
            Domain_Risk_Score += int(Customer_Configuration[0]["score_top_level_domain"])
        
        if "Close Match" in Domain_Classification:
            Domain_Risk_Score += int(Customer_Configuration[0]["score_close_match"])
        
        if "Lookalike Domain" in Domain_Classification:
            Domain_Risk_Score += int(Customer_Configuration[0]["score_look_alike"])

        if "Email" in Domain_Channels:
            Domain_Risk_Score += int(Customer_Configuration[0]["score_email_activity"])
        
        if "Live" in Domain_State:
            Domain_Risk_Score += int(Customer_Configuration[0]["score_domain_state"])
        
        if "Yes" in Domain_MX_Record:
            Domain_Risk_Score += int(Customer_Configuration[0]["score_mx_record"])

        if Domain_SPF_Record != "":
            Domain_Risk_Score += int(Customer_Configuration[0]["score_spf_record"])

        mongo_domain.update_one({"Domain":Domain_Document["Domain"]}, {"$set":{"Risk Score": Domain_Risk_Score}}, False)
    print("FINISHED - Running Risk Score Parser for: {}".format(customer_configuration_name))



def UploadDomainInformation(File_Path):
    with open(File_Path, "r", encoding="utf-8") as Domain_Information:
        csv_reader = csv.DictReader(Domain_Information)
        header = csv_reader.fieldnames
        for each in csv_reader:
            row={}
            for feild_name in header:
                row[feild_name]=each[feild_name]
                      
            Domain_Check = mongo_domain.find({"Domain": row["Domain"]}).count()
            if Domain_Check > 0:
                pass
            else:
                mongo_domain.insert_one(row)
        
        Domain_Information.close()



            
def FetchSPFRecord():
    print("Running SPF Record Parser")
    Domain_Object = mongo_domain.find()
    for domain in Domain_Object:
        try:
            dns_record = dns.resolver.resolve(domain['Domain'], 'TXT')
            for record in dns_record:
                if "spf1" in str(record):
                    print(record)
                    spf_record = record
        except:
            spf_record = ""

        print(spf_record)
        
        mongo_domain.update_one({"Domain": domain['Domain']}, {"$set": {"SPF Record": str(spf_record)}})
    print("FINISHED - Running SPF Record Parser")


def FetchMXRecord():
    print("Running MX Record Parser")
    Domain_Object = mongo_domain.find()
    for domain in Domain_Object:
        host_name = domain['Domain']
        mx_record_data = []
        try: 
            for record in dns.resolver.resolve(host_name, "MX"):
                mx_record_data.append(record.to_text())
                print(record)
        except:
            mx_record_data.append("")
    
        mongo_domain.update_one({"Domain": host_name}, {"$set": {"MX Record Data": mx_record_data }})
    print("FINISHED - Running MX Record Parser")
    


def InsertFields():
    print("Running Field Generator")
    Domain_Object = mongo_domain.find()
    for domain in Domain_Object:
        mongo_domain.update_one({"Domain": domain['Domain']}, {"$set": {"SPF Record": ""}})

    print("FINISHED - Running Field Generator")




@app.route("/api/v1/testing", methods=['GET'])
def EndpointTesting():
    start_date = str(request.args.get('start')).strip()
    end_date = str(request.args.get('end')).strip()

    payload = []
    Domain_Object = mongo_domain.find()
    for domain in Domain_Object:
        domain['_id'] = str(domain['_id'])
        if domain["Registered Date"] != "":
            registered_date = domain['Registered Date'].split(" ")[0]
            payload.append(registered_date)
            # new_registered_date = '%Y-%m-%d'
            # new_registered_date_1 = datetime.datetime.strptime(registered_date, new_registered_date)
            # payload.append(str(new_registered_date_1.month()))

    sample_data = '{"January": 19, "Febuary": 10, "March": 29}'
    payload_1 = json.loads(sample_data)

    return make_response(jsonify(payload_1), 200)
        




if __name__ == "__main__":
    # FetchMXRecord()
    # FetchSPFRecord()
    app.run(debug=True)