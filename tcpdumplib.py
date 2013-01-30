#!/usr/bin/env /usr/bin/python2.7

import sys
import time
import pexpect
from re import compile, DOTALL

CONNECT = 'ssh mcladmin@216.69.72.141'
PASSWORD = 'xyz123'

TCPDUMP_DIR = '/tmp/tcpdump_files/'
TCPDUMP_FILE = 'tcpdump_file-testcase' 
SPACE = ' '
START_TCPDUMP = '/usr/bin/sudo /usr/sbin/tcpdump -evpni eth1 tcp port 179 -w' \
    + SPACE + TCPDUMP_DIR + TCPDUMP_FILE
START_ROUTEM = '/home/mcladmin/cisco-routem/routem -i -f ' \
    + '/home/mcladmin/cisco-routem/routem.cfg'
EXIT = 'exit'
SHELL_PROMPT = '\$ '
ROUTEM_PROMPT = 'bgp0\>'
SUDO_PROMPT = '[sudo] password for mcladmin: '
TIMEOUT = 2
SHOWRUN_RE = compile('#bgp_[0-9](.*)#bgp_[0-9]', DOTALL)
SUDO_RE = compile('\[sudo\] password for mcladmin:', DOTALL)
CONNECT = 'connect'
USER = 'user'
HOST = 'host'
PWD = 'pwd'
WAIT = 'wait'

def create_pexpect_obj(cmd, user, host, pwd):
    connect = cmd + SPACE + user + '@' + host
    try:
        pObj = pexpect.spawn(connect)
    except OSError, e:                                                                                          
        raise
    pObj.expect('password:')
    pObj.sendline(pwd)
    return pObj

class Tcpdump:
    """ A class for starting and stopping tcpdump

    Attributes:
        self.cmd - list of commands/parameters to send
        self.result - results expected

    Methods:
        __init__ - constructor

        execute - send commands and check results
    """

    def __init__(self, params):
        self.tcpdump = create_pexpect_obj(params(CONNECT), params(USER),
                                          params(HOST), params(PWD))
        self.wait = params(WAIT)
    def execute(self):
        print 'starting TCPDump code'
        self.tcpdump.sendline(START_TCPDUMP)
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
