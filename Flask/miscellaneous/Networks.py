from ipaddress import ip_address
from unicodedata import name
from xmlrpc.client import TRANSPORT_ERROR
import requests
import time
import socket
from crypt import methods
from dataclasses import dataclass
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
from xmlrpc.client import TRANSPORT_ERROR
import requests
import time
import socket

client = MongoClient("mongodb://127.0.0.1:27017")
mongo_database = client.Domain
mongo_domain = mongo_database.Domain
mongo_configuration = mongo_database.Configuration


common_port_numbers = [20, 21, 25, 53, 80, 123, 179, 443, 500, 3389]

class PortKnocking:
    def main(Domain_Name):
        for port_number in common_port_numbers:
            full_domain_name = str("www." + str(Domain_Name))
            domain_ip_address = socket.gethostbyname(full_domain_name)
            domain_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            domain_socket.settimeout(0.1)
            print("Domain Name: {} | Attempting To Knock Port Number: {}".format(Domain_Name, port_number))
            end_node = (domain_ip_address, port_number)
            result = domain_socket.connect_ex(end_node)
            if result == 0:
                # print("True")
                print("Port Number: {} is open! " .format(port_number))
            else:
                pass

    def name(name):
        if name != "Toby":
            return False
        else:
            return True





if __name__ == "__main__":
    Status = PortKnocking.name("Toby")
    print(Status)
    # for domain in mongo_domain.find():
    #     domain['_id'] = str(domain['_id'])
    #     if domain['Domain'] != "":
    #         print(domain['Domain'])
    #         try:
    #             PortKnocking.main(domain['Domain'])
    #         except:
    #             print("Error - Script Not Knocking Domain Name {}".format(domain['Domain']))


