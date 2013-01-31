#!/usr/bin/env /usr/bin/python2.7

import sys
from time import time
from datetime import datetime
import pexpect
from utilities import create_pexpect_obj 
from constants import *
from re import compile, DOTALL

SUDO_RE = compile('\[sudo\] password for mcladmin:', DOTALL)

TCPDUMP_DIR = '/tmp/tcpdump_files/'
TCPDUMP_FILE = 'tcpdump_file-' 
SPACE = ' '
START_TCPDUMP = '/usr/bin/sudo /usr/sbin/tcpdump -evpni eth1 tcp port 179 -w' 

class Tcpdump:
    """ A class for starting and stopping tcpdump

    Attributes:
        self.cmd - list of commands/parameters to send
        self.result - results expected

        May need the below list of pre-compiled regular expressions, some
        indexes as constants would help too, i.e. index for SHOWRUN_RE = 0

        self.reList

    Methods:
        __init__ - constructor, expects the following input parameters:
            CONNECT - connection command, i.e. ssh, telnet
            USER - user name to connect as
            PWD - password to use
            HOST - IP address of host to connect to
            WAIT - length of time to capture
            TRID - test run ID
            TCID - test case ID

        execute - send commands and check results
    """

    def __init__(self, params):
        self.tcpdump = create_pexpect_obj(params[CONNECT], params[USER],
                                          params[HOST], params[PWD])
        if WAIT in params:
            self.wait = params[WAIT]
        else:
            self.wait = 5

        if TRID and TCID in params:
            stamp = 'trid' + params[TRID] + '.' + 'tcid' + params[TCID]
        else:
            stamp = datetime.today().strftime("%Y%m%d.%H:%M:%S")
        self.dumpfile = TCPDUMP_DIR + TCPDUMP_FILE + stamp

    def execute(self):
        print 'starting TCPDump code'
        self.tcpdump.sendline(START_TCPDUMP + SPACE + self.dumpfile)
        sudoMatchIndex = self.tcpdump.expect_list([SUDO_RE], TIMEOUT, 500)
        if sudoMatchIndex == 0:
            print 'got sudo prompt:  {0}'.format(self.tcpdump.match.group(0))
            self.tcpdump.sendline(PASSWORD)
        else:
            print "didn't find match"
            self.tcpdump.close()
            sys.exit('sudo prompt problems!!')

        # wait some time for BGP to run a bit
        time.wait(self.wait)
        self.tcpdump.sendintr()
        self.tcpdump.expect(SHELL_PROMPT)
        self.tcpdump.sendline(EXIT)
        self.tcpdump.close()
        print 'finishing tcpdump code'
