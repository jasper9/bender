wget http://localhost:8080/api/v1/swagger.json
spectacle --target-dir static swagger.json
rm -f swagger.json
