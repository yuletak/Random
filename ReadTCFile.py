#!/usr/bin/env /usr/bin/python2.7

from testlib.constants import *
from testlib.tcpdumplib import Tcpdump
from testlib.routemlib import Routem
from time import sleep 

f = open('/home/hadmin/CODE/GIT/Random/testcases/moduleA/tc-00-00-01', 'r')

lines = f.read()
mystr = ''
for line in lines:
    mystr = mystr + line.strip(' \t\n')

f.close()

print 'processed mystr:  {0}'.format(mystr)

#mystr = '{TCID:"00-00-01",CONNECT:"/usr/bin/ssh",USER:"mcladmin",HOST:"216.69.72.141",PWD:"xyz123",WAIT:5}'

#print 'raw mystr:  {0}'.format(mystr)

params = eval(mystr)

print params[TDMPPARAM][CONNECT]
