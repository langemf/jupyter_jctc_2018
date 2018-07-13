#!/bin/bash 
#SBATCH --time=12:00:00 
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=1 
#SBATCH --mem-per-cpu=3G 
#SBATCH --job-name=nb-tunnel-general 
#SBATCH --output=nb-log-%J.out 
#SBATCH --error=nb-log-%J.err 
#SBATCH --partition=sandyb 


ip=$(/sbin/ip route get 8.8.8.8 | awk '{print $NF;exit}') 
port=$((10000+ $RANDOM % 20000)) 
echo "http://"$ip":"$port"/" 
jupyter notebook --no-browser --ip=$ip --port=$port --log-level='ERROR'
