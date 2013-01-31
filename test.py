#!/usr/bin/env /usr/bin/python2.7

from tcpdumplib import Tcpdump
from constants import *

params = {
            CONNECT:  '/usr/bin/ssh',
            USER:  'mcladmin',
            HOST:  '216.69.72.141',
            PWD:  'xyz123',
            WAIT:  5
         }

dump = Tcpdump(params)

dump.execute()


