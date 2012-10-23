#! /usr/bin/python 

import subprocess as sub

#hdstreaming = "/usr/lib/hadoop-0.20/contrib/streaming/hadoop-streaming-0.20.2-cdh3u1.jar"
#log_path = "/user/root/flume/log_access"


#temp = [i.split() for i in open("todo_dir").readlines()]
temp_dir=["/production/userprofile/V3/summary/dsp/adx/tid/auto/2012/10/20/*",\
        "/production/userprofile/V3/summary/dsp/adx/tid/manual/2012/10/20/*",\
        "/production/userprofile/V3/summary/dsp/adx/tid/semiauto/2012/10/20/*",\
        "/production/userprofile/V3/summary/dsp/tanx/tid/auto/2012/10/20/*",\
        "/production/userprofile/V3/summary/dsp/tanx/tid/manual/2012/10/20/*",\
        "/production/userprofile/V3/summary/dsp/tanx/tid/semiauto/2012/10/20/*"]

for i in temp_dir:
    cmd = 'hadoop jar "/usr/lib/hadoop-0.20/contrib/streaming/hadoop-streaming-0.20.2-cdh3u1.jar" \
            -D mapred.reduce.tasks=50 -mapper "python noise.py" -reducer "cat" -file noise.py \
            -input %s -output %s'%(i,i.split("summary/")[1].split("*")[0])
    print cmd
    handle = sub.Popen("%s"%cmd,stdout=sub.PIPE,shell=True)
    print handle.stdout.read()
