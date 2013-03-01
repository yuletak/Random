#!/usr/bin/env /usr/bin/python2.7

from pexpect import spawn   
from constants import *
import urllib2, base64

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
    while index < count:
        if args[index] == '-bnumber':
            var[JBUILDNUM] = args[index+1]
        if args[index] == '-bid':
            var[JBUILDID] = args[index+1]
        if args[index] == '-burl':
            var[JBUILDURL] = args[index+1]
        if args[index] == '-btag':
            var[JBUILDID] = args[index+1]
        if args[index] == '-commit':
            var[JGITCOMMIT] = args[index+1]
        if args[index] == '-branch':
            var[JGITBRANCH] = args[index+1]
        index += 1
    return var 

def get_vo_req(USER, PWD, URL):
    base64string = base64.standard_b64encode('%s:%s' % (USER, PWD))
    req = urllib2.Request(URL)
    req.add_header("Authorization", "Basic %s" % base64string)
    return req

def get_testcase_param(testcase):
    if testcase == None:
        raise
    f = open('./testcases/moduleA/' + testcase, 'r')
    lines = f.read()
    mystr = ''
    for line in lines:
        mystr = mystr + line.strip('\t\n')
    f.close()
    params = eval(mystr)
    return params
