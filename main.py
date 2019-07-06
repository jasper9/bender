from flask import Flask, send_from_directory, current_app,  Blueprint, render_template, url_for, redirect, request, send_file, g
from flask_restplus import Resource, Api, apidoc, reqparse, fields, Model, abort
import pymysql.cursors
import json as json1
from common import *
from flask_table import Table, Col, LinkCol, OptCol

app = Flask(__name__, static_folder="static", static_url_path='')
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

config = configparser.ConfigParser()
config.read('config.ini')

from blueprints.api_v1 import api_v1
app.register_blueprint(api_v1)


@app.route("/doc")
def doc():
    return current_app.send_static_file('index.html')

@app.route("/")
def home():
    
    message = "Coming soon...<br><br>"
    message += "<a href='/api/v1/swagger'>Swagger UI</a><br><br>"
    message += "<a href='/doc'>Spectacle UI</a><br><br>"
    title = "Title"
    return render_template("message.html", message=message, title=title)



class vCenterTable(Table):
    fullName    = Col('fullName')
    build       = Col('build')
    releaseDate = Col('releaseDate')

class esxiTable(Table):
    releaseName    = Col('releaseName')
    build       = Col('build')
    releaseDate = Col('releaseDate')

@app.route('/vmware/vcenter')
def ui_vmware_vcenter():
    db = connectDB()
    with db.cursor() as cursor:
        sql = "select fullName, build, releaseDate, osType, releaseNotes from vmware_vcenter"
        cursor.execute(sql)
        data = cursor.fetchall()
    disconnectDB(db)
    table = vCenterTable(data)
    title = "vCenter Releases"
    return render_template('table.html', table=table, title=title)

@app.route('/vmware/esxi')
def ui_vmware_esxi():
    db = connectDB()
    with db.cursor() as cursor:
        sql = "select * from vmware_esxi where releaseName is not null order by releaseDate desc"
        cursor.execute(sql)
        data = cursor.fetchall()
    disconnectDB(db)
    table = esxiTable(data)
    title = "ESXi Releases"
    return render_template('table.html', table=table, title=title)


# @app.route('/<path:path>')
# def serve_page(path):
#     return send_from_directory('static', path)
    
# This only runs when invoked by python directly
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
