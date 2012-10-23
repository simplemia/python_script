#! /usr/bin/python 

import subprocess as sub

temp_dir=["*"]
for i in temp_dir:
    handle = sub.Popen("hadoop fs -ls %s"%i,stdout=sub.PIPE,shell=True)
    print handle.stdout.read()
