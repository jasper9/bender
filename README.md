# bender

This is just mostly notes until I get a bit further along...

https://bender.apps.pcfone.io/example


curl https://bender.apps.pcfone.io/api/v1/vmware/vcenter/linux/13010631

["vcenters", {
	"build": "13010631",
	"build2": "13007421",
	"fullName": "vCenter Server 6.7 Update 2",
	"osType": "linux",
	"releaseDate": "Thu, 11 Apr 2019 00:00:00 GMT",
	"releaseNotes": ""
}]

curl https://bender.apps.pcfone.io/api/v1/vmware/esxi/9484548
["esxi", {
	"build": "9484548",
	"fullName": "ESXi 6.7 EP 03",
	"imageprofile": "ESXi-6.7.0-20180804001-standard",
	"releaseDate": "Tue, 14 Aug 2018 00:00:00 GMT",
	"releaseName": "ESXi670-201808001",
	"releaseNotes": "https://kb.vmware.com/kb/56535"
}]



Links to document:
https://www.virten.net/vmware/vcenter-release-and-build-number-history/#linux
https://kb.vmware.com/s/article/2143838
https://esxi-patches.v-front.de/
https://kb.vmware.com/s/article/2143832


Tools:
https://apiguide.readthedocs.io/en/latest/build_and_publish/documentation.html
https://github.com/Swagger2Markup/swagger2markup
https://github.com/sourcey/spectacle

npm install -g spectacle-docs

wget http://localhost:8080/api/v1/swagger.json
spectacle --target-dir static swagger.json
rm -f swagger.json

http://localhost:8080/api/v1/doc/

http://localhost:8080/api/v1/swagger.json

