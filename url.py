import urllib2, base64
import xml.etree.ElementTree as ET

IDSCOPE = '2785'
ONESCOPE = 'https://www15.v1host.com/NTTMCL/rest-1.v1/Data/Scope/'+IDSCOPE
ALLSCOPE = 'https://www15.v1host.com/NTTMCL/rest-1.v1/Data/Scope'

IDTIMEBOX = '2839'
ONETIMEBOX = 'https://www15.v1host.com/NTTMCL/rest-1.v1/Data/Timebox/'+IDTIMEBOX
ALLTIMEBOX = 'https://www15.v1host.com/NTTMCL/rest-1.v1/Data/Timebox'

HOST = 'https://www15.v1host.com/NTTMCL'
USER = 'yui'
PWD = 'v3rs!0n0n3'

base64string = base64.standard_b64encode('%s:%s' % (USER, PWD))

allScopeReq = urllib2.Request(ALLSCOPE)
allScopeReq.add_header("Authorization", "Basic %s" % base64string)   
allScope = urllib2.urlopen(allScopeReq)
allScopeAssets = ET.fromstring(allScope.read())

# all projects
print 'all scopes'
for asset in allScopeAssets.findall('Asset'):
    if asset.get('id') == 'Scope:2785':
        for attrib in asset.findall('Attribute'):
            name = attrib.get('name')
            if name == 'Name':
                print 'Scope name:  {0}'.format(attrib.text)
            if name == 'Description':
                print 'Description:  {0}'.format(attrib.text)

oneScopeReq = urllib2.Request(ONESCOPE)
oneScopeReq.add_header("Authorization", "Basic %s" % base64string)   
oneScope = urllib2.urlopen(oneScopeReq)
oneScopeAsset = ET.fromstring(oneScope.read())

print 'one scope'
for attrib in oneScopeAsset.findall('Attribute'):
    name = attrib.get('name')
    if name == 'Name':
        print 'Scope name:  {0}'.format(attrib.text)
    if name == 'Description':
        print 'Description:  {0}'.format(attrib.text)


