#!/usr/bin/env python

from sys import path as path, argv as argv
# should be a better way to include the library code path
path += ['./testlib']

from utilities import update_vo_asset
from utilities import *

from constants import * 
from moduleAconf import *
import urllib2, base64

VOOneTestURL = VOTEST + '/' + '2849'
#print 'VersionOne one test URL:  {0}'.format(VOOneTestURL)
results = (('Relation', 'Status', '"TestStatus:155"'),)
# update the info in VO
asset = update_vo_asset(results)
#print '  attributes to update:  {0}'.format(asset)
VOOneTestReq = get_vo_req(VOUSER, VOPWD, VOOneTestURL, asset)
VOOneTest = urllib2.urlopen(VOOneTestReq)
print VOOneTest.read()
