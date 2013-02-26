#!/usr/bin/env /usr/bin/python2.7

import sys
import time
import pexpect
from re import compile, DOTALL
from utilities import create_pexpect_obj 
from constants import *

SHOWRUN_RE = compile('#bgp_[0-9](.*)#bgp_[0-9]', DOTALL)



SPACE = ' '
START_ROUTEM = '/home/mcladmin/cisco-routem/routem -i -f ' \
    + '/home/mcladmin/cisco-routem/routem.cfg'
EXIT = 'exit'
SHELL_PROMPT = '\$ '
ROUTEM_PROMPT = 'bgp0\>'
SUDO_PROMPT = '[sudo] password for mcladmin: '
TIMEOUT = 2

class Routem:
    """ A class for sending commands to Routem

    Attributes:
        self.cmd - list of commands to send
        self.result - results expected
        
        May need the below list of pre-compiled regular expressions, some
        indexes as constants would help too, i.e. index for SHOWRUN_RE = 0

        self.reList

    Methods:
        __init__ - constructor

        execute - send commands and check results
    """

    def __init__(self, rtmparam, tdmpparam):
        self.routem = create_pexpect_obj(rtmparam[CONNECT], rtmparam[USER],
                                         rtmparam[HOST], rtmparam[PWD])

    def execute(self):
        print 'starting routem code'
        self.routem.expect(SHELL_PROMPT)
        self.routem.sendline(START_ROUTEM)
        self.routem.expect(ROUTEM_PROMPT, TIMEOUT)
        self.routem.sendline('show run')
        routemMatchIndex = self.routem.expect_list([SHOWRUN_RE], TIMEOUT, 500)
        
        if routemMatchIndex == 0:
            print '{0}'.format(self.routem.match.group(0))
        else:
            print "didn't find match"
        self.routem.expect(ROUTEM_PROMPT, TIMEOUT)
        self.routem.sendline(EXIT)
        self.routem.expect(SHELL_PROMPT)
        self.routem.sendline(EXIT)
        self.routem.close()
        print 'finishing routem code'
        
