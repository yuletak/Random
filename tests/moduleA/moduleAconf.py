VOHOST = 'https://www15.v1host.com/NTTMCL'
VOUSER = 'yui'
VOPWD = 'v3rs!0n0n3'
VOSCOPENAME = 'moduleA'
VOSCOPEID = '2785'
VOTIMEBOX = '2839'

VOSPRINTNAME = 'moduleA - Sprint 1'
VOSPRINTID = '2839'
VORESTPATH = '/rest-1.v1/Data'
VOREST = VOHOST + VORESTPATH
VOSCOPE = VOREST + '/Scope'
VOSPRINT = VOREST + '/Timebox'
VOSTORY = VOREST + '/Story'
VOTASK = VOREST + '/Task'
VOTEST = VOREST + '/Test'

VOTESTS = VOTEST + '?where=Timebox=\'Timebox:' + VOTIMEBOX + '\''

TESTCASEDIR = '../testcases/moduleA/'
