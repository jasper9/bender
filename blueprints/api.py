import pymysql.cursors
import json as json1
from flask import Blueprint, jsonify, request, Response
from flask_restplus import Resource, Api, apidoc, reqparse, fields, Model, abort
from common import *

api_v1 = Blueprint('api', 'api', url_prefix='/api/v1')

api = Api(api_v1,
        version='1.1',
        title='Bender',
        description='descr here',
        doc='/doc/')


# ENDPOINTS ############################################################################################################
# ######################################################################################################################
@api.route('/vmware/vcenter')
class vmware_vcenter(Resource):
    def get(self):
        '''List all uses cases for users'''
        #log_debug('ENTERING :: /useCases')
        db = connectDB()

        txt = ["vcenters"]
        with db.cursor() as cursor:
            sql = "select fullName, build, releaseDate, osType, releaseNotes from vmware_vcenter"
            cursor.execute(sql)
            for row in cursor:
                txt.append(row)
        disconnectDB(db)
        return jsonify(txt)

@api.route('/vmware/vcenter/<osType>/<build>')
class vmware_vcenter_specific(Resource):
    def get(self, osType, build):
        '''List all uses cases for users'''
        #log_debug('ENTERING :: /useCases')
        db = connectDB()

        txt = ["vcenters"]
        with db.cursor() as cursor:
            sql = "select fullName, build, build2, releaseDate, osType, releaseNotes from vmware_vcenter where osType=%s and (build=%s or build2=%s)"
            cursor.execute(sql, (osType, build, build))
            for row in cursor:
                txt.append(row)
        disconnectDB(db)
        return jsonify(txt)