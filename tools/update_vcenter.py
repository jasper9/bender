

import json
import pymysql.cursors
import sys

sys.path.append(".")
from common import *


# using this file   https://www.virten.net/vmware/vcenter-release-and-build-number-history/#linux
# and from here https://kb.vmware.com/s/article/2143838

db = connectDB()
with db.cursor() as cursor:
    with open("vcenterReleases.json", 'r') as json_file:
        data = json.load(json_file)
        for rel in data["data"]["vcenterReleases"]:
            #print(rel)

            sql = "select * from vmware_vcenter where build=%s"
            cursor.execute(sql, (rel['build']))
            
            if cursor.rowcount == 0:
                print("Not found, adding...")
                sql = "insert into vmware_vcenter (build, fullName, releaseDate, osType, releaseNotes) values (%s,%s,%s,%s,%s)"
                cursor.execute(sql, (rel['build'],rel['fullName'],rel['releaseDate'],rel['osType'],rel['releaseNotes']))


disconnectDB(db)