#!/usr/bin/env python

from sys import path as path, argv as argv
# should be a better way to include the library code path
path += ['./testlib']

from utilities import update_vo_attrib as uva
from utilities import *

from constants import * 
from moduleAconf import *
import urllib2, base64
import xml.etree.ElementTree as ET
from testcase import Testcase

VOOneTestURL = VOTEST + '/' + '2849'
print 'VersionOne one test URL:  {0}'.format(VOOneTestURL)
results = (('Attribute', 'ExpectedResults', 'test output!!!'),)
# update the info in VO
asset = update_vo_attrib(results)
print '  attributes to update:  {0}'.format(asset)
VOOneTestReq = get_vo_req(VOUSER, VOPWD, VOOneTestURL, asset)
VOOneTest = urllib2.urlopen(VOOneTestReq)
print VOOneTest.read()
