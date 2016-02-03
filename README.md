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
- Update the ```__main__``` method to load a test file -- or other file
- Run the script:

```
cd api_scripts
python run_shapefile_script.py
```

