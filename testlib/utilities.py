#!/usr/bin/env /usr/bin/python2.7

from pexpect import spawn   
from constants import *

def create_pexpect_obj(cmd, user, host, pwd):
    connect = cmd + SPACE + user + '@' + host
    try:
        pObj = spawn(connect)
    except OSError, e:                                                                                          
        raise
    pObj.expect('password:')
    pObj.sendline(pwd)
    return pObj

def parse_jenkins_argv(args):
    count = len(args)
    index = 1
    var = {}
    while arg < count:
        if args[arg] == '-bnumber':
            var[BUILDNUM] = args[arg+1]
        if args[arg] == '-bid':
            var[BUILDID] = args[arg+1]
        if args[arg] == '-burl':
            var[BUILDURL] = args[arg+1]
        if args[arg] == '-btag':
            var[BUILDID] = args[arg+1]
        if args[arg] == '-commit':
            var[GITCOMMIT] = args[arg+1]
        if args[arg] == '-branch':
            var[GITBRANCH] = args[arg+1]
    return var 
    
