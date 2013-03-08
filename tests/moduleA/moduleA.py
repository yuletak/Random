#!/usr/bin/env python

from sys import path as path, argv as argv
# should be a better way to include the library code path
path += ['./testlib']

from utilities import *

from constants import * 
from moduleAconf import *
import urllib2, base64
import xml.etree.ElementTree as ET
from testcase import Testcase

jEnv = {}
jEnv = parse_jenkins_argv(argv)

VOTestReq = get_vo_req(VOUSER, VOPWD, VOTESTS)
try:
    VOTests = urllib2.urlopen(VOTestReq)
    VOTestAssets = ET.fromstring(VOTests.read())
except error:
    print 'nada!'

testcases = get_vo_testcases(VOTestAssets)
for testID, fileName, scopeName in testcases:

    # Set path to file and file name
    tcFile = TESTCASEDIR + scopeName + '/' + fileName

    # Read file parameters and get test case parameters
    tcFileParam = get_testcase_param(tcFile)
    tcParam = tcFileParam[PARAM]

    # Create the dummy testcase object, can be any of the objects we have
    # Typically should be a list of objects with list of commands to execute
    testcase = Testcase(tcParam)
    code, status, mesg = testcase.execute()
    Status = ''
    if code == 0:
        Status = '"TestStatus:129"'
    else:
        Status = '"TestStatus:155"'
        
    results = (('Attribute', 'ActualResults', mesg),
               ('Relation', 'Status', Status),
               ('Attribute', 'ExpectedResults', tcParam[OUTPUT][0]),)

    # update the info in VO
    asset = update_vo_asset(results)
    print '  attributes to update:  {0}'.format(asset)

    VOOneTestURL = VOTEST + '/' + testID 
    print 'VersionOne one test URL:  {0}'.format(VOOneTestURL)

    VOOneTestReq = get_vo_req(VOUSER, VOPWD, VOOneTestURL, asset)
    VOOneTest = urllib2.urlopen(VOOneTestReq)
    print VOOneTest.read()
