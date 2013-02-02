#!/usr/bin/env /usr/bin/python2.7

from tcpdumplib import Tcpdump
from constants import *
from time import sleep 
from routemlib import Routem

tcid = 'tc-00-00-01'
tcpdumpParams = {
            CONNECT:  '/usr/bin/ssh',
            USER:  'mcladmin',
            HOST:  '216.69.72.141',
            PWD:  'xyz123',
            WAIT:  5
         }

dump = Tcpdump(tcpdumpParams)
route = Routem(tcpdumpParams)
dump.start()
route.execute()
sleep(5)
dump.stop()


