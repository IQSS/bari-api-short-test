import hashlib
import json
from os.path import basename, dirname, isfile, join
import requests
from datetime import datetime
from cred_reader import GEONODE_SERVER, GEONODE_USERNAME, GEONODE_PASSWORD

from dataverse_test_info import DataverseTestInfo

def dashes(): print '-' * 40

def upload_shapefile(title, file_fullpath):
    assert isfile(file_fullpath), 'The file could not be found: %s' % file_fullpath

    dv_info = DataverseTestInfo.get_test_info_dict(title, file_fullpath)

    worldmap_url = GEONODE_SERVER + '/dataverse/import-shapefile/'

    files = {'file': open( file_fullpath, 'rb')}

    dashes()
    print '-- Dataverse Information: --\n', dv_info
    dashes()
    print 'make request: %s' % worldmap_url
    print 'Start time:', datetime.now()
    dashes()

    r = requests.post(worldmap_url,
                data=dv_info,
                files=files,
                auth=(GEONODE_USERNAME, GEONODE_PASSWORD),
                #timeout=1,
             )
    print r.text
    dashes()
    print 'Status code:', r.status_code

    dashes()
    print 'End time:', datetime.now()

if __name__=='__main__':
    #upload_shapefile('Fukushima', 'test_files/fukushima-food-radiation.zip')
    upload_shapefile('Boston social disorder', 'test_files/social_disorder_in_boston.zip')
    #upload_shapefile('Boston income', 'test_files/income_in_boston_gui.zip')
