#!/usr/bin/env /usr/bin/python2.7

from testlib.constants import *
from testlib.tcpdumplib import Tcpdump
from testlib.routemlib import Routem
from time import sleep 

f = open('/home/hadmin/CODE/GIT/Random/testcases/moduleA/tc-00-00-01', 'r')

lines = f.read()
mystr = ''
for line in lines:
    line = line.lstrip('\t')
    mystr = mystr + line.rstrip('\n')

f.close()

print 'mystr:  {0}'.format(mystr)

params = eval(mystr)

print params[0]
