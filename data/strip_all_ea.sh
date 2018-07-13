#!/bin/sh

# This script will retrieve all EAs for a given method and sort by value
# Output format is FORMULA (IP QPWT CONV) with the () part repeated with number of EAs
for f in $1/*log; do 
	ea=$(echo $(grep 'EA root ' $f | awk '{print $6, $9, $12}' | sort | tr '\n' ' '))	# Grab all of the necessary EAs and sort them
    out=${f%%_*}																		# Format string to only contain formula 
    out=${f#*\/}																		# String formatting for the name, remove directory information
    out=${out%%_*}																		# String formatting for the name, only keep formula
    echo $out $ea																		# Write out formula and all EAs
done
