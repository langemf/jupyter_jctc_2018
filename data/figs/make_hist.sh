#!/bin/bash

# This script uses the information provided by the eomccsd_analysis.py script to plot a scatter/bar plot
# This can be done for any method, use of this script: ./make_hist.sh [method_approx] (ie. ccsd_none)

# Check for the correct number of inputs
EXPECTED_ARGS=1
if [ $# -ne $EXPECTED_ARGS ]; then
    echo "Usage: `basename $0` method_approx"
    exit 99
fi

awk '{print $4,$5}' "../"$1"/"$1"_ip_errors.dat" | head --lines=-26 > "../"$1"/"$1"_scatter.dat"  	# Take the CCSD(T) IP value and error for each molecule for scatter plot

# This section pulls out the ME and MAE for printing onto the plot
me=$(grep 'mean error' "../"$1"/"$1"_ip_errors.dat" | awk '{print $5}')
mae=$(grep 'mean abs error' "../"$1"/"$1"_ip_errors.dat" | awk '{print $6}')
me=$(printf "%.3f" $me)
mae=$(printf "%.3f" $mae)

# Make sure the gnuplot script grabs the correct files to plot
histfile="../"$1"/"$1"_ip_errors.dat"
scatterfile="../"$1"/"$1"_scatter.dat"

cp ./gw100hist_hor_12.gp ./temp.gp																	# Make sure you're not overriding template gnuplot script
sed "s|SCATTER_FILE|$scatterfile|g" ./gw100hist_hor_12.gp > ./t1.gp									# Call correct scatter plot data
sed "s|HIST_FILE|$histfile|g" ./t1.gp > ./t2.gp														# Call correct bar plot data
sed "s|MEVAL|$me|g" ./t2.gp > ./t1.gp																# Print MAE, ME, NAME
sed "s|MAEVAL|$mae|g" ./t1.gp > ./t2.gp
sed "s|TITLE|$2|g" ./t2.gp > ./t1.gp
mv ./t1.gp ./gw100hist_hor_12.gp
chmod +x ./gw100hist_hor_12.gp											
sh ~/utils/gnuplot/plot.sh ./gw100hist_hor_12 &														# Plot the gnuplot
mv ./gw100hist_hor_12.eps $1"_ip_sidehist.eps"														# Clean up intermediate files
mv ./gw100hist_hor_12.pdf $1"_ip_sidehist.pdf"
#
mv ./temp.gp ./gw100hist_hor_12.gp
