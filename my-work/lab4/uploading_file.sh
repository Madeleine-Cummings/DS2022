#!/usr/bin/bash

aws configure

curl -o red_panda.jpg https://as1.ftcdn.net/v2/jpg/01/44/18/18/1000_F_144181825_p7HhZ2EKMoDjs6kx24WJFJRd5HGw2Iah.jpg 
aws s3 cp red_panda.jpg s3://ds2022-uwg9at/
URL=$(aws s3 presign s3://ds2022-uwg9at/red_panda.jpg --expires-in 604800)
echo "$URL"

chmod +x uploading_file.sh
