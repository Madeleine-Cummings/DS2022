#!/usr/bin/bash

#fetching tarball
wget https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz

#Decompressing the compressed archive
tar -xzf https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz

# awk can remove spaces
awk '!/^[[:space:]]*$/' lab3-bundle.tar.gz

awk 'BEGIN { FS="\t"; OFS="," } {$1=$1; print}' lab3-bundle.tar.gz > lab3-bundle.tar.gz.csv

count=$(wc -l lab3-bundle.tar.gz.csv)
#count=($count-1)
echo "$count"

tar -cvf converted-archive.tar.gz lab3-bundle.tar.gz.csv
