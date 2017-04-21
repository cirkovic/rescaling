N=${1}
M=${2}
I1=${3}
I2=${4}
J1=${5}
J2=${6}
OUT=${7}

cd /afs/cern.ch/work/c/cirkovic/kLimits/CombineHarvester/CMSSW_7_4_7/src/
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/c/cirkovic/FCNC_limits/rescaling

COMMAND="python rscript_3.py ${N} ${M} ${I1} ${I2} ${J1} ${J2} ${OUT}"
echo $COMMAND
eval $COMMAND

