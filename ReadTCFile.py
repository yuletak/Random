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

params = eval(mystr)

dump = Tcpdump(params[TDMPPARAM])

dump.start()

sleep(5)

dump.stop()

