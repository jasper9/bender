from flask import Flask, Blueprint, render_template, url_for, redirect, request, send_file, g
from flask_restplus import Resource, Api, apidoc, reqparse, fields, Model, abort
import pymysql.cursors
import json as json1
from common import *

config = configparser.ConfigParser()
config.read('config.ini')

api_v1 = Blueprint('api', 'api', url_prefix='/api/v1')

api = Api(api_v1,
        version='1.0',
        title='Bender: The robot that drinks and knows things',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        contact="@jasper9",
        doc="/swagger")

model = api.model('Model', {
    'name': fields.String,
})

# ENDPOINTS ############################################################################################################
# ######################################################################################################################

@api.route('/vmware/vcenter')
class vmware_vcenter(Resource):
    @api.response(200, 'Success', model)
    def get(self):
        '''GET vCenter Releases'''
        db = connectDB()

        txt = ["vcenters"]
        with db.cursor() as cursor:
            sql = "select fullName, build, releaseDate, osType, releaseNotes from vmware_vcenter"
            cursor.execute(sql)
            for row in cursor:
                row['releaseDate'] = row['releaseDate'].strftime("%Y-%m-%d")
                txt.append(row)
        disconnectDB(db)
        return jsonify(txt)

# ######################################################################################################################

@api.route('/vmware/vcenter/<osType>')
@api.doc(params={'osType': 'OS type, `linux` or `windows`'})
class vmware_vcenter_specific_os(Resource):
    @api.response(200, 'Success', model)
    def get(self, osType):
        '''GET vCenter Releases by OS'''
        db = connectDB()

        txt = ["vcenters"]
        with db.cursor() as cursor:
            sql = "select fullName, build, build2, releaseDate, osType, releaseNotes from vmware_vcenter where osType=%s"
            cursor.execute(sql, (osType))
            for row in cursor:
                row['releaseDate'] = row['releaseDate'].strftime("%Y-%m-%d")
                txt.append(row)
        disconnectDB(db)
        return jsonify(txt)

# ######################################################################################################################

@api.route('/vmware/vcenter/<osType>/<build>')
@api.doc(params={
                    'osType': 'OS type, `linux` or `windows`',
                    'build': 'Build number of the release. Can be either `VAMI` or `client/MOB` types.  See here: https://kb.vmware.com/s/article/2143838'
            })
class vmware_vcenter_specific_os_build(Resource):
    @api.response(200, 'Success', model)
    def get(self, osType, build):
        '''GET vCenter Release by OS and build'''
        db = connectDB()

        txt = ["vcenters"]
        with db.cursor() as cursor:
            sql = "select fullName, build, build2, releaseDate, osType, releaseNotes from vmware_vcenter where osType=%s and (build=%s or build2=%s)"
            cursor.execute(sql, (osType, build, build))
            for row in cursor:
                row['releaseDate'] = row['releaseDate'].strftime("%Y-%m-%d")
                txt.append(row)
        disconnectDB(db)
        return jsonify(txt)

# ######################################################################################################################

@api.route('/vmware/esxi')
class vmware_esxi(Resource):
    @api.response(200, 'Success', model)
    def get(self):
        '''GET ESXi Releases'''
        db = connectDB()

        txt = ["esxi"]
        with db.cursor() as cursor:
            sql = "select releaseDate, build, releaseName, imageprofile, fullName, releaseNotes from vmware_esxi"
            cursor.execute(sql)
            for row in cursor:
                row['releaseDate'] = row['releaseDate'].strftime("%Y-%m-%d")
                txt.append(row)
        disconnectDB(db)
        return jsonify(txt)

# ######################################################################################################################

@api.route('/vmware/esxi/<build>')
@api.doc(params={
                    'build': 'Build number of the release.'
            })
class vmware_esxi_specific_build(Resource):
    @api.response(200, 'Success', model)
    def get(self, build):
        '''GET ESXi Releases by build number'''
        db = connectDB()

        txt = ["esxi"]
        with db.cursor() as cursor:
            sql = "select releaseDate, build, releaseName, imageprofile, fullName, releaseNotes from vmware_esxi where build=%s"
            cursor.execute(sql, (build))
            for row in cursor:
                row['releaseDate'] = row['releaseDate'].strftime("%Y-%m-%d")
                txt.append(row)
        disconnectDB(db)
        return jsonify(txt)