#!/bin/sh
# Some common shell stuff.

echo "Importing from common.sh"

DB=frontierDB
USER=mmc9967
CONNECT_STR="mongodb+srv://frontier.5dsrn7a.mongodb.net/"
# f'mongodb+srv://mmc9967:{password}@frontier.5dsrn7a.mongodb.net/{USER_DB}?retryWrites=true&w=majority
if [ -z $DATA_DIR ]
then
    DATA_DIR=/Users/marcchiu/Documents/NYU/Senior_Year/Software_Engineering/Class_Project/Frontier/data
fi
BKUP_DIR=$DATA_DIR/bkup
EXP=/usr/local/bin/mongoexport
IMP=/usr/local/bin/mongoimport

if [ -z $MONGO_PASSWORD ]
then
    echo "You must set MONGO_PASSWD in your env before running this script."
    exit 1
fi

declare -a FrontierCollections=("users groups restaurants")