#!/bin/bash

# Backing up our files

LOGFILE="./log_file"
BACKUP_LOC="/home/$USER/Downloads/*"
BACKUP_TARGET="./backup"

echo "Creating backup directory "&& mkdir $BACKUP_TARGET 2> /dev/null || echo "Directory already exists"

echo "Copying files" && cp -v $BACKUP_LOC $BACKUP_TARGET > $LOGFILE 2>&1

grep -i denied $LOGFILE | tail -n 2

exit 127
