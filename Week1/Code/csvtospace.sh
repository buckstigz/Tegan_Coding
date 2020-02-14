#!/bin/bash
# Author: Tegan Beale teganbeale@gmail.com
# Script: csvtospace.sh
# Description: takes comma seperated values and converts to a space seperated values file
# Arguments: 1 -> space seperated value file
# Date: Feb 2020

cat $1 | tr -s "," " " >> $1.txt

# exit