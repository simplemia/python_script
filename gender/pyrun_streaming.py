#! /usr/bin/python 

import subprocess as sub

i = "/production/userprofile/user_category_summary_merge_addrelation/subset/2012/10/01/*"

cmd = 'hadoop jar "/usr/lib/hadoop-0.20/contrib/streaming/hadoop-streaming-0.20.2-cdh3u1.jar" \
        -D mapred.reduce.tasks=100 -mapper "python gender_map.py" -reducer "python gender_reduce.py" \
        -file gender_map.py -file gender_reduce.py \
        -input %s -output %s'%(i,"/subset/2012/10/01/")
print cmd
handle = sub.Popen("%s"%cmd,stdout=sub.PIPE,shell=True)
print handle.stdout.read()
