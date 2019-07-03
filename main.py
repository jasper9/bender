from flask import Flask, Blueprint, render_template, url_for, redirect, request, send_file, g
import pymysql.cursors
import json as json1
from flask_table import Table, Col, OptCol
import pprint
import time
from common import *

app = Flask(__name__)

# config = configparser.ConfigParser()
# config.read('config.ini')

from blueprints.api import api_v1


app.register_blueprint(api_v1)


# This only runs when invoked by python directly
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)



