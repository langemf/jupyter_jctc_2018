#!/bin/bash

# Check for proper number of command line args.

EXPECTED_ARGS=4

if [ $# -ne $EXPECTED_ARGS ]; then
    echo "Usage: `basename $0` formula basis cctype partition"
    exit 99
fi

slurmsh="slurm_$1_$2_$3_$4.sh"
sed "s/FORM/$1/g; s/BAS/$2/g; s/CC/$3/g; s/PART/$4/g;" good_slurm_template.sh > $slurmsh
sbatch $slurmsh 

