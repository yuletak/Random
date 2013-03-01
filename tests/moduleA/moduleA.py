#!/usr/bin/env python

# should be a better way to include the library code path
path += ['./testlib']

from sys import path as path, argv as argv
from utilities import parse_jenkins_argv as pja
from utilities import get_testcase_param as gtp
from utilities import get_vo_req as gvr
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
    tcFile = ''
    for attrib in test.findall('Attribute'):
        name = attrib.get('name')
        if name == 'Number':
            tcFile = attrib.text
            break
    if tcFile == '':
        raise
    tcInput = gtp(tcFile)
    tcParam = tcInput[PARAM]
    testcase = Testcase(tcParam)
    code, mesg = testcase.execute()
    print '{0}:  {1}'.format(code, mesg)

    # update the info in VO

