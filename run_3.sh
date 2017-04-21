#rm -rf output/*

OUTPUT=rescaling_16-04-2017
OUTPUT=rescaling_16-04-2017_3
OUTPUT=rescaling_17-04-2017_3

#N=50
#N=100
#N=20
N=50

NJOBS=5
#NJOBS=10

M=0.2
M=0.5
M=1.0
M=${1}

EOS=/eos/cms/store/caf/user/mdjordje/Cirkovic
OUT="${EOS}/${OUTPUT}_${N}_${M}"

eos rm -r ${OUT}
eos mkdir ${OUT}

for i in `seq 0 ${N}`; do
    for j in `seq 0 ${N}`; do
        eos mkdir ${OUT}/${i}_${j}
    done
done

#BSUB_QUIET=1
N1=$((N-1))
N2=$((N1/NJOBS))

#for i in `seq 0 $((N-1))`; do
for i in `seq 0 $N2`; do
#for i in `seq 10 10`; do
    #for j in `seq 0 $((N-1))`; do
    for j in `seq 0 $N2`; do
    #for j in `seq 25 25`; do
#        I1=$((i * 1))
#        J1=$((j * 1))
#        I2=$((I1 + 1))
#        J2=$((J1 + 1))
#        if [[ "$i" == "$((N-1))" ]]; then I2=$((I1 + 2)); fi
#        if [[ "$j" == "$((N-1))" ]]; then J2=$((J1 + 2)); fi
        I1=$((i * NJOBS))
        J1=$((j * NJOBS))
        I2=$((I1 + NJOBS))
        J2=$((J1 + NJOBS))
        if [[ "$i" == "$N2" ]]; then I2=$((I1+NJOBS+1)); fi
        if [[ "$j" == "$N2" ]]; then J2=$((J1+NJOBS+1)); fi
        #COMMAND="python rscript.py 100 ${I1} ${I2} ${J1} ${J2}"
        #COMMAND="bsub -q 1nh batch_script.sh 50 ${I1} ${I2} ${J1} ${J2}"
        #COMMAND="bsub -q 1nh batch_script.sh ${N} ${I1} ${I2} ${J1} ${J2}"
        #COMMAND="bsub -q 1nh batch_script.sh ${N} ${M} ${I1} ${I2} ${J1} ${J2}"
        #COMMAND="bsub -q 1nh -o /dev/null batch_script.sh ${N} ${M} ${I1} ${I2} ${J1} ${J2}"
#        COMMAND="bsub -q 1nh -o /tmp/cirkovic/job_out batch_script.sh ${N} ${M} ${I1} ${I2} ${J1} ${J2}"
        #COMMAND="sh batch_script.sh ${N} ${M} ${I1} ${I2} ${J1} ${J2}"
#        echo $COMMAND
#        eval $COMMAND
        #bsub -q 1nh -o /tmp/cirkovic/job_out batch_script.sh ${N} ${M} ${I1} ${I2} ${J1} ${J2}
        #COMMAND="bsub -q 8nh -o /tmp/cirkovic batch_script_3.sh ${N} ${M} ${I1} ${I2} ${J1} ${J2} ${OUT}"
        COMMAND="bsub -q 1nh -o /tmp/cirkovic batch_script_3.sh ${N} ${M} ${I1} ${I2} ${J1} ${J2} ${OUT}"
        echo $COMMAND
        eval $COMMAND
        #exit
    done
done

