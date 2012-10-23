#! /usr/bin/python 

import subprocess as sub

temp_dir=["/production/userprofile/V3/summary/dsp/adx/pyid/auto/2012/10/17/p*", "/production/userprofile/V3/summary/dsp/adx/pyid/manual/2012/10/17/p*", "/production/userprofile/V3/summary/dsp/adx/pyid/semiauto/2012/10/17/p*", "/production/userprofile/V3/summary/dsp/tanx/pyid/auto/2012/10/17/p*", "/production/userprofile/V3/summary/dsp/tanx/pyid/manual/2012/10/17/p*", "/production/userprofile/V3/summary/dsp/tanx/pyid/semiauto/2012/10/17/p*", "/production/userprofile/V3/summary/opt/advertiser/auto/2012/10/17/p*", "/production/userprofile/V3/summary/opt/advertiser/manual/2012/10/17/p*", "/production/userprofile/V3/summary/opt/advertiser/semiauto/2012/10/17/p*", "/production/userprofile/V3/summary/opt/media/auto/2012/10/17/p*", "/production/userprofile/V3/summary/opt/media/manual/2012/10/17/p*", "/production/userprofile/V3/summary/opt/media/semiauto/2012/10/17/p*"]
for i in temp_dir:
    handle = sub.Popen("hadoop fs -ls %s"%i,stdout=sub.PIPE,shell=True)
    print handle.stdout.read()
