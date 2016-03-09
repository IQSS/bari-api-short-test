from os.path import isfile
import requests
from datetime import datetime
from cred_reader import GEONODE_SERVER, GEONODE_USERNAME, GEONODE_PASSWORD

from dataverse_test_info import DataverseTestInfo

def dashes(): print '-' * 40

def classify_layer(classify_params):
    """
    Send classification params to an existing layer
    """
    worldmap_url = GEONODE_SERVER + '/dataverse/api/classify-layer/'

    dashes()
    print '-- API Params --\n', classify_params
    dashes()
    print 'make request: %s' % worldmap_url
    print 'Start time:', datetime.now()
    dashes()

    r = requests.post(worldmap_url,
              data=classify_params,
              auth=(GEONODE_USERNAME, GEONODE_PASSWORD))

    print r.text
    print r.status_code

    dashes()
    print 'End time:', datetime.now()

if __name__=='__main__':
    classify_params = dict(layer_name='j_cbg_ann_boston',
                dataverse_installation_name='http://localhost:8000',
                datafile_id=67193,
                attribute='housing_2010',
            	ramp='Blue',
            	intervals=5,
            	startColor='#f7fbff',
            	endColor='#08306b',
            	method='quantile',
                reverse=False)

    classify_params = dict(layer_name='social_dis_v51',
                dataverse_installation_name='https://RAD-rprasad.harvard.edu',
                datafile_id=1237,
                attribute='Alcohol_21',
            	ramp='Custom',
            	intervals=5,
            	startColor='#fff5eb',
            	endColor='#f16913',
            	method='jenks',#'uniqueInterval',
                reverse=False)

    classify_layer(classify_params)
