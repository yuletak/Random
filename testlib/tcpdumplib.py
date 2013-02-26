#!/usr/bin/env /usr/bin/python2.7

import sys
from time import sleep
from datetime import datetime
import pexpect
from utilities import create_pexpect_obj 
from constants import *
from re import compile, DOTALL


TCPDUMP_DIR = '/tmp/tcpdump_files/'
TCPDUMP_FILE = 'tcpdump_file-' 
SPACE = ' '
START_TCPDUMP = '/usr/bin/sudo /usr/sbin/tcpdump -evpni IFACE tcp port 179 -w FILE' 

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

        start - start tcpdump

        stop - stop tcpdump

    """

    def __init__(self, params):
        self.tcpdump = create_pexpect_obj(params[CONNECT], params[USER],
                                          params[HOST], params[PWD])

        try:
            self.user = params[USER]
            self.pwd = params[PWD]
            self.SUDO_RE = compile('\[sudo\] password for '+self.user+':', DOTALL)
        except KeyError:
            raise

        if TRID and TCID in params:
            stamp = 'trid' + params[TRID] + '.' + 'tcid' + params[TCID]
        else:
            stamp = datetime.today().strftime("%Y%m%d.%H:%M:%S")
        self.dumpfile = TCPDUMP_DIR + TCPDUMP_FILE + stamp

        try:
            self.dumpCmd = START_TCPDUMP
            self.dumpCmd = self.dumpCmd.replace('IFACE', params[IFACE])
        except KeyError:
            raise

        self.dumpCmd = self.dumpCmd.replace('FILE', self.dumpfile)

    def start(self):
        # Check for existence of directory to store tcpdump files
        # Create directory if necessary.
        self.tcpdump.sendline("if [ ! -d " + TCPDUMP_DIR + " ]; " \
            "then mkdir -p " + TCPDUMP_DIR + "; fi")
        self.tcpdump.sendline(self.dumpCmd)
        sudoMatchIndex = self.tcpdump.expect_list([self.SUDO_RE], TIMEOUT, 500)
        if sudoMatchIndex == 0:
            self.tcpdump.sendline(self.pwd)
        else:
            self.tcpdump.close()
            sys.exit('sudo prompt problems!!')

    def stop(self):
        self.tcpdump.sendintr()
        self.tcpdump.expect(SHELL_PROMPT)
        self.tcpdump.sendline(EXIT)
        self.tcpdump.close()
