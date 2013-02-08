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
