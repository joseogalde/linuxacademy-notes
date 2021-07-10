#!/bin/bash

# Backing up our files

# We can take user input as the log file
LOGFILE=$1
BACKUP_LOC="/home/$USER/Downloads/*"
BACKUP_TARGET="./backup"

function init {
    echo "Creating backup directory "&& mkdir $BACKUP_TARGET 2> /dev/null || echo "Directory already exists"
    echo "" > $LOGFILE
    CLOUDGURU=37
}

copyfiles () {
    echo "Copying files" && cp -v $BACKUP_LOC $BACKUP_TARGET >> $LOGFILE 2>&1
    local $MYLOCAL=420
}

# override tail to simplify its calling
# for that we use 'command' inside to specify the tail linux command

tail () {
    command tail -n $1
}

init
copyfiles

grep -i denied $LOGFILE | tail 2

echo $CLOUDGURU
echo $MYLOCAL

exit 127
