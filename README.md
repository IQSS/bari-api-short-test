# bari-api-short-test

Simple script to send files to the WorldMap API.  For quick testing/debugging.

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

### Example output (with WorldMap timeout):

#### Bad Run

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

#### Good Run

```
$ python run_shapefile_script.py
----------------------------------------
-- Dataverse Information: --
{'datafile_label': 'social_disorder_in_boston.zip', 'abstract': 'Abstract for Boston social disorder', 'shapefile_name': 'Neighborhoods_BRA_1.tiff', 'dataset_description': 'Description for Dataset Boston social disorder', 'return_to_dataverse_url': 'http://localhost:8080/dataset.xhtml?id=62', 'datafile_content_type': 'application/zip', 'dataset_id': 479, 'dataverse_id': 81, 'title': 'Boston social disorder', 'dv_user_email': 'dvuser@harvard.edu', 'dv_username': 'BARI', 'dataverse_installation_name': 'http://localhost:8000', 'datafile_create_datetime': '2014-09-30 10:00:54.544', 'dv_user_id': 1, 'dataset_version_id': 2, 'dataverse_name': 'Dataverse Boston social disorder', 'datafile_expected_md5_checksum': 'Z8KSV55PU4MRJ2AUVKMTBQHSWMYW3ITY', 'datafile_download_url': 'http://localhost:8080/api/access/datafile/80767', 'dataset_semantic_version': 'V2', 'dataset_citation': 'BARI, 2015, "Demographics for 2009 American Community Survey", http://hdl.handle.net/1902.1/15586, Harvard Dataverse, V3', 'datafile_filesize': 1106432, 'datafile_id': 80767, 'dataverse_description': 'Description for Dataverse Boston social disorder', 'dataset_name': 'Dataset Boston social disorder'}
----------------------------------------
make request: http://23.21.172.243/dataverse/import-shapefile/
Start time: 2016-02-03 12:36:41.913726
----------------------------------------
{"message": "Shapefile successfully imported", "data": {"embed_map_link": "http://23.21.172.243/maps/embed/?layer=geonode:neighborhoods_bra_1_tiff_i8w", "download_links": "{\"zip\": \"http://23.21.172.243/download/wfs/118/zip?outputFormat=SHAPE-ZIP&service=WFS&request=GetFeature&format_options=charset%3AUTF-8&typename=geonode%3Aneighborhoods_bra_1_tiff_i8w&version=1.0.0\", \"gml\": \"http://23.21.172.243/download/wfs/118/gml?outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&service=WFS&request=GetFeature&format_options=charset%3AUTF-8&typename=geonode%3Aneighborhoods_bra_1_tiff_i8w&version=1.0.0\", \"tiff\": \"http://23.21.172.243/download/wms/118/tiff?layers=geonode%3Aneighborhoods_bra_1_tiff_i8w&width=655&bbox=-71.1914644962%2C42.2272481395%2C-70.9861620286%2C42.3994625741&service=WMS&format=image%2Fgeotiff&srs=EPSG%3A4326&request=GetMap&height=550\", \"KML\": \"http://23.21.172.243/download/wms_kml/118/kml?layers=geonode%3Aneighborhoods_bra_1_tiff_i8w&mode=refresh\", \"jpg\": \"http://23.21.172.243/download/wms/118/jpg?layers=geonode%3Aneighborhoods_bra_1_tiff_i8w&width=655&bbox=-71.1914644962%2C42.2272481395%2C-70.9861620286%2C42.3994625741&service=WMS&format=image%2Fjpeg&srs=EPSG%3A4326&request=GetMap&height=550\", \"json\": \"http://23.21.172.243/download/wfs/118/json?outputFormat=json&service=WFS&request=GetFeature&format_options=charset%3AUTF-8&typename=geonode%3Aneighborhoods_bra_1_tiff_i8w&version=1.0.0\", \"pdf\": \"http://23.21.172.243/download/wms/118/pdf?layers=geonode%3Aneighborhoods_bra_1_tiff_i8w&width=655&bbox=-71.1914644962%2C42.2272481395%2C-70.9861620286%2C42.3994625741&service=WMS&format=application%2Fpdf&srs=EPSG%3A4326&request=GetMap&height=550\", \"csv\": \"http://23.21.172.243/download/wfs/118/csv?outputFormat=csv&service=WFS&request=GetFeature&format_options=charset%3AUTF-8&typename=geonode%3Aneighborhoods_bra_1_tiff_i8w&version=1.0.0\", \"xls\": \"http://23.21.172.243/download/wfs/118/xls?outputFormat=excel&service=WFS&request=GetFeature&format_options=charset%3AUTF-8&typename=geonode%3Aneighborhoods_bra_1_tiff_i8w&version=1.0.0\", \"png\": \"http://23.21.172.243/download/wms/118/png?layers=geonode%3Aneighborhoods_bra_1_tiff_i8w&width=655&bbox=-71.1914644962%2C42.2272481395%2C-70.9861620286%2C42.3994625741&service=WMS&format=image%2Fpng&srs=EPSG%3A4326&request=GetMap&height=550\"}", "worldmap_username": "dvuser", "attribute_info": "[{\"type\": \"long\", \"display_name\": \"Objectid\", \"name\": \"OBJECTID\"}, {\"type\": \"double\", \"display_name\": \"Area\", \"name\": \"AREA\"}, {\"type\": \"double\", \"display_name\": \"Perimeter\", \"name\": \"PERIMETER\"}, {\"type\": \"string\", \"display_name\": \"State\", \"name\": \"STATE\"}, {\"type\": \"string\", \"display_name\": \"County\", \"name\": \"COUNTY\"}, {\"type\": \"string\", \"display_name\": \"Tract\", \"name\": \"TRACT\"}, {\"type\": \"string\", \"display_name\": \"Blockgroup\", \"name\": \"BLOCKGROUP\"}, {\"type\": \"string\", \"display_name\": \"Bg_Id\", \"name\": \"BG_ID\"}, {\"type\": \"string\", \"display_name\": \"Ct_Id\", \"name\": \"CT_ID\"}, {\"type\": \"int\", \"display_name\": \"Blk_Count\", \"name\": \"BLK_COUNT\"}, {\"type\": \"string\", \"display_name\": \"Logrecno\", \"name\": \"LOGRECNO\"}, {\"type\": \"double\", \"display_name\": \"Dry_Acres\", \"name\": \"DRY_ACRES\"}, {\"type\": \"double\", \"display_name\": \"Dry_Sqmi\", \"name\": \"DRY_SQMI\"}, {\"type\": \"double\", \"display_name\": \"Dry_Sqkm\", \"name\": \"DRY_SQKM\"}, {\"type\": \"double\", \"display_name\": \"Shape_Area\", \"name\": \"SHAPE_AREA\"}, {\"type\": \"double\", \"display_name\": \"Shape_Len\", \"name\": \"SHAPE_LEN\"}, {\"type\": \"double\", \"display_name\": \"Hoods_Pd_I\", \"name\": \"HOODS_PD_I\"}, {\"type\": \"string\", \"display_name\": \"Nbhd\", \"name\": \"Nbhd\"}, {\"type\": \"string\", \"display_name\": \"Nbhdcrm\", \"name\": \"NbhdCRM\"}, {\"type\": \"string\", \"display_name\": \"Nsa_Id\", \"name\": \"NSA_ID\"}, {\"type\": \"string\", \"display_name\": \"Nsa_Name\", \"name\": \"NSA_NAME\"}, {\"type\": \"string\", \"display_name\": \"Bg_Id_1\", \"name\": \"BG_ID_1\"}, {\"type\": \"double\", \"display_name\": \"Homeowners\", \"name\": \"Homeowners\"}, {\"type\": \"double\", \"display_name\": \"Medincomeh\", \"name\": \"MedIncomeH\"}, {\"type\": \"double\", \"display_name\": \"Propwhite\", \"name\": \"propwhite\"}, {\"type\": \"double\", \"display_name\": \"Propblack\", \"name\": \"propblack\"}, {\"type\": \"double\", \"display_name\": \"Propasian\", \"name\": \"propasian\"}, {\"type\": \"double\", \"display_name\": \"Prophisp\", \"name\": \"prophisp\"}, {\"type\": \"double\", \"display_name\": \"Medage\", \"name\": \"medage\"}, {\"type\": \"double\", \"display_name\": \"Propcolleg\", \"name\": \"propcolleg\"}, {\"type\": \"double\", \"display_name\": \"Totalpop\", \"name\": \"TotalPop\"}, {\"type\": \"double\", \"display_name\": \"Popden\", \"name\": \"popden\"}, {\"type\": \"string\", \"display_name\": \"Type\", \"name\": \"Type\"}, {\"type\": \"int\", \"display_name\": \"Id2\", \"name\": \"ID2\"}, {\"type\": \"string\", \"display_name\": \"Bg_Id_12\", \"name\": \"BG_ID_12\"}, {\"type\": \"double\", \"display_name\": \"Socdis_201\", \"name\": \"SocDis_201\"}, {\"type\": \"double\", \"display_name\": \"Socstrife_\", \"name\": \"SocStrife_\"}, {\"type\": \"double\", \"display_name\": \"Alcohol_20\", \"name\": \"Alcohol_20\"}, {\"type\": \"double\", \"display_name\": \"Violence_2\", \"name\": \"Violence_2\"}, {\"type\": \"double\", \"display_name\": \"Guns_2010\", \"name\": \"Guns_2010\"}, {\"type\": \"double\", \"display_name\": \"Socstrife1\", \"name\": \"SocStrife1\"}, {\"type\": \"double\", \"display_name\": \"Socdis_202\", \"name\": \"SocDis_202\"}, {\"type\": \"double\", \"display_name\": \"Socstrif_1\", \"name\": \"SocStrif_1\"}, {\"type\": \"double\", \"display_name\": \"Alcohol_21\", \"name\": \"Alcohol_21\"}, {\"type\": \"double\", \"display_name\": \"Violence_3\", \"name\": \"Violence_3\"}, {\"type\": \"double\", \"display_name\": \"Guns_2011\", \"name\": \"Guns_2011\"}, {\"type\": \"double\", \"display_name\": \"Socstrif_2\", \"name\": \"SocStrif_2\"}, {\"type\": \"double\", \"display_name\": \"Socdis_203\", \"name\": \"SocDis_203\"}, {\"type\": \"double\", \"display_name\": \"Socstrif_3\", \"name\": \"SocStrif_3\"}, {\"type\": \"double\", \"display_name\": \"Alcohol_22\", \"name\": \"Alcohol_22\"}, {\"type\": \"double\", \"display_name\": \"Violence_4\", \"name\": \"Violence_4\"}, {\"type\": \"double\", \"display_name\": \"Guns_2012\", \"name\": \"Guns_2012\"}, {\"type\": \"double\", \"display_name\": \"Socstrif_4\", \"name\": \"SocStrif_4\"}]", "layer_name": "geonode:neighborhoods_bra_1_tiff_i8w", "layer_link": "http://23.21.172.243/data/geonode:neighborhoods_bra_1_tiff_i8w", "map_image_link": "http://23.21.172.243/download/wms/118/png?layers=geonode%3Aneighborhoods_bra_1_tiff_i8w&width=655&bbox=-71.1914644962%2C42.2272481395%2C-70.9861620286%2C42.3994625741&service=WMS&format=image%2Fpng&srs=EPSG%3A4326&request=GetMap&height=550", "llbbox": "[-71.19146449624893, 42.22724813947405, -70.98616202859677, 42.39946257406787]"}, "success": true}
----------------------------------------
Status code: 200
----------------------------------------
End time: 2016-02-03 12:37:09.963532
```

## Run lat/lng api script

- Edit file: ```api_scripts/run_lat_lng_script.py```
- Update the ```__main__``` method to load a test shapefile file, from ```test_files```, or elsewhere
- Run the script:

```
cd api_scripts
python run_lat_lng_script.py
```
