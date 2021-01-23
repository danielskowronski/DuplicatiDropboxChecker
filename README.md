# Duplicati Dropbox Checker

Simple Python script to check if backups created by Duplicati are correctly present at Dropbox (if that target was selected). 

Outputs data in format acceptable by Prometheus that include path on Dropbox and timestamp of newest file in provided directory with Duplicati backups.

## Setup
```
python3 -m pip install -r requirements.txt
```

## Usage
```
./ddc.py DROPBOX_API_TOKEN PATH_ON_DROPBOX
```

* `PATH_ON_DROPBOX` is full path to directory on Dropbox, eg. `"/Applications/Duplicati backup/COMPUTER_ONE/C_DRIVE"`
* `DROPBOX_API_TOKEN` is non-expiring read-only token to Dropbox API

### How to generate `DROPBOX_API_TOKEN`
1. Go to Dropbox App Console - https://www.dropbox.com/developers/apps
2. Click *Create App*
   1. Select *Scoped access*
   2. Select *Full Dropbox* since we will be accessing data of other application
   3. Provide some *name* - must be globally unique accross all Dropbox application, but can be random string
3. In page you are taken to after creation of application go to tab *Permissions*
   1. Navigate to *Individual Scopes*
   2. Find *Files and folders*
   3. Select checkbox `files.metadata.read`
   4. Click *Submit*
4. In the same page go to tab *Settings*
   1. Navigate to *OAuth 2*
   2. In *Access token expiration* dropdown select *No expiration* (this should be fixed in future)
   3. Find section *Generated access token*
   4. Click *Generate*
   5. Store API token in safe place

### Typical application
It was created with cron daily execution in mind that stores files consumed by `collector.textfile` in *prometheus_nodexporter*.

### Example output
```
dropbox_duplicati_latest_file{"/Applications/Duplicati backup/COMPUTER_ONE/C_DRIVE"} 1611363686
```
