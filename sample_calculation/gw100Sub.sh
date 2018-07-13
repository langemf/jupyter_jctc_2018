#!/bin/sh

EXPECTED_ARGS=1

if [[ "$#" -ne EXPECTED_ARGS ]]; then
    echo "Usage: `$basename` moleculeList"
    exit 99
fi

while read -r line
do
    ./submit_job.sh $line def2-tzvpp ccsd none
done < $1
