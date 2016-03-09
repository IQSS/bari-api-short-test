from os.path import isfile
import requests
from datetime import datetime
from cred_reader import GEONODE_SERVER, GEONODE_USERNAME, GEONODE_PASSWORD

from dataverse_test_info import DataverseTestInfo

def dashes(): print '-' * 40

def upload_lat_lng_file(title, file_fullpath, lat_lng_params, use_dataverse_api=False):
    """
    use_dataverse_api = False
     -> Use the basic Datatables API endpoint

    use_dataverse_api = True
    -> Basic Datatables API endpoint + the new layer
       has associated Dataverse metadata--a new DataverseLayerMetadata object


    Example of lat_lng_params:
        { delimiter : '\t',
          lng_attribute : 'Longitude',
          lat_attribute : 'Latitude'}
    """
    assert isfile(file_fullpath), 'The file could not be found: %s' % file_fullpath

    if use_dataverse_api:
        # API endpoint
        worldmap_url = GEONODE_SERVER + '/dataverse/api/tabular/upload-lat-lng/'
    else:
        # API endpoint
        worldmap_url = GEONODE_SERVER + '/datatables/api/upload_lat_lon/'

    # Load Dataverse sample metadata
    # Still needed to load title/abstract values for non-Dataverse endpoint
    #
    dv_info = DataverseTestInfo.get_test_info_dict(title, file_fullpath)
    dv_info['datafile_content_type'] = 'text/plain'

    # Add map params to dv_info
    map_params.update(dv_info)

    files = {'uploaded_file': open( file_fullpath, 'rb')}

    dashes()
    print '-- API Params --\n', map_params
    dashes()
    print 'make request: %s' % worldmap_url
    print 'Start time:', datetime.now()
    dashes()

    r = requests.post(worldmap_url,
                data=map_params,
                files=files,
                auth=(GEONODE_USERNAME, GEONODE_PASSWORD),
                #timeout=1,
             )
    print r.text
    #open('lat_lng_err.html', 'w').write(r.text)
    dashes()
    print 'Status code:', r.status_code

    dashes()
    print 'End time:', datetime.now()

if __name__=='__main__':
    map_params = dict(delimiter='\t',
                    lng_attribute='Longitude', # col name in uploaded file
                    lat_attribute='Latitude') # col name in uploaded file

    upload_lat_lng_file('Boston social disorder',
                    'test_files/coded_data_2008_10-tab.txt',
                    map_params,
                    use_dataverse_api=True)
