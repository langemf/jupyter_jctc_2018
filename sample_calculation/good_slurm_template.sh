#!/bin/sh  
#SBATCH --job-name=FORM_BAS_CC_PART
#SBATCH --output=FORM_BAS_CC_PART.log
#SBATCH --error=FORM_BAS_CC_PART.err
#SBATCH --nodes=1
#SBATCH --sockets-per-node=1
#SBATCH --cores-per-socket=1
#SBATCH --mem=30000
#SBATCH -t 3:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

export OMP_NUM_THREADS=1

fout="FORM_BAS_CC_PART.log"
python -u eomccsd.py FORM BAS CC PART > $fout
