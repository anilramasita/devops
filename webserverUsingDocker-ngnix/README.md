#Commands to run the server

notepad docker-compose.yaml

docker-compose up -d --force-recreate

#If any errors
docker-compose down
docker-compose up -d --force-recreate