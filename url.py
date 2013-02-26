import urllib2, base64
import xml.etree.ElementTree as ET

URI = 'https://www15.v1host.com/NTTMCL/rest-1.v1/Data/Scope/2785'
HOST = 'https://www15.v1host.com/NTTMCL/Account.mvc/LogIn?destination=%2FNTTMCL%2F'
USER = 'yui'
PWD = 'v3rs!0n0n3'

request = urllib2.Request(URI)
base64string = base64.standard_b64encode('%s:%s' % (USER, PWD))
request.add_header("Authorization", "Basic %s" % base64string)   
scope = urllib2.urlopen(request)


tree = ET.parse(scope.read())
root = tree.getroot()
