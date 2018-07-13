#!/bin/sh

# This script strips the first EA from the log files
# Will give printout with format NAME VALUE
# Pipe output of this script to desired file


for f in $1/*log; do 
    n=`grep "EA root" $f | awk '{print $6}'`; 	# Grep for the EAs and only retrieve the values with awk
    m=`echo $n`; 								
    ea=`python -c "print min('$m'.split())"`	# Find the smallest of the EAs
    out=${f#*\/}								# String formatting for the name, remove directory information
    out=${out%%_*}								# String formatting for the name, only keep formula
    echo $out $ea								# Print out NAME VALUE
done
