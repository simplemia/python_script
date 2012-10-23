#! /usr/bin/python 

import subprocess as sub

i = "*"

cmd = 'hadoop jar "hadoop-0.20/contrib/streaming/hadoop-streaming-0.20.2-cdh3u1.jar" \
        -D mapred.reduce.tasks=100 -mapper "python gender_map.py" -reducer "python gender_reduce.py" \
        -file gender_map.py -file gender_reduce.py \
        -input %s -output %s'%(i,"/")
print cmd
handle = sub.Popen("%s"%cmd,stdout=sub.PIPE,shell=True)
print handle.stdout.read()
