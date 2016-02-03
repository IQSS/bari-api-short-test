"""
Load up the Worldmap server url and creds
"""

import json
from os.path import basename, dirname, isfile, join, realpath

GEONODE_CREDS_FNAME = join(dirname(realpath(__file__)), 'server_creds.json')

assert isfile(GEONODE_CREDS_FNAME), 'Server credentials file not found: %s' % GEONODE_CREDS_FNAME

try:
    GEONODE_CREDS_JSON = json.loads(open(GEONODE_CREDS_FNAME, 'r').read())
except:
    raise Exception('Could not parse tabular credentials JSON file: %s' % 'server_creds.json')

GEONODE_SERVER = GEONODE_CREDS_JSON['SERVER_URL']
GEONODE_USERNAME = GEONODE_CREDS_JSON['USERNAME']
GEONODE_PASSWORD = GEONODE_CREDS_JSON['PASSWORD']
