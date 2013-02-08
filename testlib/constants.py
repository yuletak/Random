#!/usr/bin/env /usr/bin/python2.7

CONNECT = 'connect'
PASSWORD = 'xyz123'
USER = 'user'
HOST = 'host'
PWD = 'pwd'
TCID = 'tcid'
TRID = 'trid'
WAIT = 'wait'
TDMPPARAM = 'tdmpparam'
RTMPARAM = 'rtmparam'

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
