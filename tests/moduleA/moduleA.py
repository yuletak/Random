#!/usr/bin/env python

from sys import path as path, argv as argv
# should be a better way to include the library code path
path += ['./testlib']

from utilities import parse_jenkins_argv as pja
from utilities import get_testcase_param as gtp
from utilities import get_vo_req as gvr
from utilities import update_vo_attrib as uva

from constants import * 
from moduleAconf import *
import urllib2, base64
import xml.etree.ElementTree as ET
from testcase import Testcase

jEnv = {}
jEnv = pja(argv)

VOTestReq = gvr(VOUSER, VOPWD, VOTESTS)
try:
    VOTests = urllib2.urlopen(VOTestReq)
    VOTestAssets = ET.fromstring(VOTests.read())
except error:
    print 'nada!'

for test in VOTestAssets.findall('Asset'):
    # Get test case file name; called "Number" in VO
    fileName = ''
    scopeName = '' 
    for attrib in test.findall('Attribute'):
        name = attrib.get('name')
        if name == 'Number':
            fileName = attrib.text
        if name == 'Scope.Name':
            scopeName = attrib.text
        if fileName != '' and scopeName != '':
            break
    if fileName == '' or scopeName == '':
        raise
    tcFile = TESTCASEDIR + scopeName + '/' + fileName
    tcInput = gtp(tcFile)
    tcParam = tcInput[PARAM]
    testcase = Testcase(tcParam)
    code, status, mesg = testcase.execute()
    results = (('Attribute', 'Status.Name', status),
               ('Attribute', 'ActualResults', mesg),
               ('Attribute', 'ExpectedResults', tcParam[OUTPUT][0]),)

    # update the info in VO
    asset = uva(results)
    print asset
