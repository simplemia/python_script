#! /bin/sh

hdstreaming="hadoop-0.20/contrib/streaming/hadoop-streaming.jar"
log_path=""
#pre_day="`date -d '1 days ago' +%Y/%m/%d`"
outputdir="${1}"
mapfile="$2"
redfile="$3"

if [ "${#@}" -lt 2 ]
then
	echo "Usage : ./run_shellstreaming_py.sh inputdir outputdir mapfile redfile"
	exit
fi

if [ -z "${redfile}" ];then
	echo hadoop jar ${hdstreaming} -mapper "python ${mapfile}" -reducer "cat" -file ${mapfile} \
    -file part-m-00000 -input ""\
    -output ${outputdir}
else
	hadoop jar ${hdstreaming} -D mapred.reduce.tasks=50 -mapper "python ${mapfile}" -reducer "python ${redfile}" -file ${mapfile}  -file ${redfile} -input ${inputdir} -output ${outputdir} 
fi

