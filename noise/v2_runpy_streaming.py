#! /usr/bin/python 

import subprocess as sub



#temp = [i.split() for i in open("todo_dir").readlines()]
temp_dir=[""]

for i in temp_dir:
    cmd = 'hadoop jar "hadoop-0.20/contrib/streaming/hadoop-streaming.jar" \
            -D mapred.reduce.tasks=50 -mapper "python noise.py" -reducer "cat" -file noise.py \
            -input %s -output %s'%(i,i.split("summary/")[1].split("*")[0])
    print cmd
    handle = sub.Popen("%s"%cmd,stdout=sub.PIPE,shell=True)
    print handle.stdout.read()
