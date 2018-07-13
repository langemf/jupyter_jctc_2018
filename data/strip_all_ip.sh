#!/bin/sh

# This script will retrieve all IPs for a given method and sort by value
# Output format is FORMULA (IP QPWT CONV) with the () part repeated with number of IPs
for f in $1/*log; do 
	ip=$(echo $(grep 'IP root ' $f | awk '{print $6, $9, $12}' | sort | tr '\n' ' '))	# Grab all of the necessary IPs and sort them
    out=${f%%_*}																		# Format string to only contain formula 
    out=${f#*\/}																		# String formatting for the name, remove directory information
    out=${out%%_*}																		# String formatting for the name, only keep formula
    echo $out $ip																		# Write out formula and all IPs
done
