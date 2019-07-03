import pymysql.cursors
import json as json1
from flask import Blueprint, jsonify, request, Response
from flask_restplus import Resource, Api, apidoc, reqparse, fields, Model, abort
import os
import configparser



config = configparser.ConfigParser()
config.read('config.ini')



def connectDB():
    if os.environ.get('VCAP_APP_HOST'):
        #mysql v2 - pcfone and slot55
        sql_service = json1.loads(os.environ['VCAP_SERVICES'])['p.mysql'][0]['credentials']

        #mysql v1 - pcf beta
        #sql_service = json1.loads(os.environ['VCAP_SERVICES'])['p-mysql'][0]['credentials']
        db_host = str(sql_service['hostname'])
        db_user = str(sql_service['username'])
        db_pass = str(sql_service['password'])
        db_name = str(sql_service['name'])

    else:
        #local config
        db_host = config['backend']['db_host']
        db_user = config['backend']['db_user']
        db_pass = config['backend']['db_pass']
        db_name = config['backend']['db_name']


    db = pymysql.connect(host=db_host,
        user=db_user,
        password=db_pass,
        db=db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

    db.cursor()
    return(db)

def disconnectDB(db):
    db.commit()
    db.close()    
