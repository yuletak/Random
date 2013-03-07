#!/usr/bin/env /usr/bin/python2.7

from pexpect import spawn   
from constants import *
import urllib2, urllib, base64

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
        index += 2
    return var 

def get_vo_req(user, pwd, VOurl, text = None):
    base64string = base64.standard_b64encode('%s:%s' % (user, pwd))
    if text != None:
        text = urllib.urlencode(text) 
    req = urllib2.Request(url = VOurl, data = text)

    req.add_header("Authorization", "Basic %s" % base64string)
    return req

def get_vo_testcases(assets):
    ''' Retrieve test case ID and module from assets list

    Input:  list of test case assets as returned by VersionOne
    Output:  list of tuples which indicate test case number and scope name
    '''
    testcases = []
    for test in assets.findall('Asset'):
        # Get test case file name; called "Number" in VO
        fileName = ''
        scopeName = ''
        testID = test.get('id').strip('"').split(':')[1]
        
        for attrib in test.findall('Attribute'):
            name = attrib.get('name')
            if name == 'Number':
                fileName = attrib.text
            if name == 'Scope.Name':
                scopeName = attrib.text
            if testID != '' and fileName != '' and scopeName != '':
                testcases.append((testID, fileName, scopeName))
                break
        if testID == '' or fileName == '' or scopeName == '':
            raise
    return testcases

def update_vo_attrib(nameValues):
    asset = '<Asset>'
    for element,name,value in nameValues:
        asset = asset + '<' + element + SPACE + 'name=' + '"' + name + '"' + \
        SPACE + 'act="set">' + value + '</' + element + '>'
    asset = asset + '</Asset>'
    return asset
 
def get_testcase_param(tcFile):
    if tcFile == None:
        raise
    f = open(tcFile, 'r')
    lines = f.read()
    mystr = ''
    for line in lines:
        mystr = mystr + line.strip('\t\n')
    f.close()
    params = eval(mystr)
    return params
