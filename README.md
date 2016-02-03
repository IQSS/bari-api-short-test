# bari-api-short-test
Simple script to send files to the WorldMap API

## Quick setup

### Install requirements

```
pip install -r requirements.txt
```

### Create/Update the creds file

- Within the ```api_scripts``` dirctory:
  - Copy the ```server_creds_template.json``` to ```server_creds.json```
  - Edit ```server_creds.json``` with a valid WorldMap account and url

## Run shapefile api script

- Edit file: ```api_scripts/run_shapefile_script.py```
- Update the ```__main__``` method to load a test shapefile file, from ```test_files```, or elsewhere
- Run the script:

```
cd api_scripts
python run_shapefile_script.py
```

- Example output (with WorldMap timeout):
```
$ python run_shapefile_script.py 
----------------------------------------
-- Dataverse Information: --
{'datafile_label': 'social_disorder_in_boston.zip', 'abstract': 'Abstract for Boston social disorder', 'shapefile_name': 'Neighborhoods_BRA_1.tiff', 'dataset_description': 'Description for Dataset Boston social disorder', 'return_to_dataverse_url': 'http://localhost:8080/dataset.xhtml?id=62', 'datafile_content_type': 'application/zip', 'dataset_id': 745, 'dataverse_id': 18, 'title': 'Boston social disorder', 'dv_user_email': 'dvuser@harvard.edu', 'dv_username': 'BARI', 'dataverse_installation_name': 'http://localhost:8000', 'datafile_create_datetime': '2014-09-30 10:00:54.544', 'dv_user_id': 1, 'dataset_version_id': 9, 'dataverse_name': 'Dataverse Boston social disorder', 'datafile_expected_md5_checksum': 'FREI8CV12H41DF0ZOV8DC9Y88LI4Y40B', 'datafile_download_url': 'http://localhost:8080/api/access/datafile/59525', 'dataset_semantic_version': 'V9', 'dataset_citation': 'BARI, 2015, "Demographics for 2009 American Community Survey", http://hdl.handle.net/1902.1/15586, Harvard Dataverse, V3', 'datafile_filesize': 1106432, 'datafile_id': 59525, 'dataverse_description': 'Description for Dataverse Boston social disorder', 'dataset_name': 'Dataset Boston social disorder'}
----------------------------------------
make request: http://worldmap.harvard.edu/dataverse/import-shapefile/
Start time: 2016-02-03 12:00:13.711327
----------------------------------------
<html>
<head><title>504 Gateway Time-out</title></head>
<body bgcolor="white">
<center><h1>504 Gateway Time-out</h1></center>
<hr><center>nginx/1.8.0</center>
</body>
</html>

----------------------------------------
Status code: 504
----------------------------------------
End time: 2016-02-03 12:00:44.092127
```

