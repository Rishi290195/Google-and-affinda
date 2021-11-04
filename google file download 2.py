from __future__ import print_function
import httplib2
import io

from apiclient import discovery
#from oauth2client import client
from oauth2client import tools
#from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
import schedule
import time
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
import auth
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.getCredentials()

http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http)

def listFiles(size):
    results = drive_service.files().list(
        pageSize=size,fields="nextPageToken, files(id, name)",q="createdTime > '2021-07-27T12:00:00-08:00'" or "modifiedTime > '2021-07-27T12:00:00-08:00'").execute()
    items = results.get('files', [])
    #if not items:
    #    print('No files found.')

        #print('Files:')
    lst = []
    lsrt = []
    for item in items:
            #print('{0} ({1})'.format(item['name'], item['id']))
        if item['name'].endswith('.pdf') or item['name'].endswith('.docx') or item['name'].endswith('.doc'):
            lst.append(item['id'])
            lsrt.append(item['name'])
       # print(item)
    return lst,lsrt

#--------------------------------
'''results = service.files().list(
    pageSize=10,
    fields="nextPageToken, files(id, name)",
    q="modifiedTime > '2012-06-04T12:00:00-08:00'"
    ).execute()
items = results.get('files', [])
if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print('{0} ({1})'.format(item['name'], item['id']))'''
#--------------------------------
lst, lsrt = listFiles(1000)
print(lst)
print(lsrt)

"""def uploadFile(filename,filepath,mimetype):
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath,
                            mimetype=mimetype)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: %s' % file.get('id'))"""

def downloadFile(file_id, filepath):
    request = drive_service.files().get_media(fileId=file_id)   #get_media(fileId=file_id) #mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    with io.open(filepath,'wb') as f:
        fh.seek(0)
        f.write(fh.read())

"""def createFolder(name):
    file_metadata = {
    'name': name,
    'mimeType': 'application/vnd.google-apps.folder'
    }
    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
    print ('Folder ID: %s' % file.get('id'))

def searchFile(size,query):
    results = drive_service.files().list(
    pageSize=size,fields="nextPageToken, files(id, name, kind, mimeType)",q=query).execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(item)
            print('{0} ({1})'.format(item['name'], item['id']))"""
#uploadFile('unnamed.jpg','unnamed.jpg','image/jpeg')
def job():
    for i in range(0,len(lsrt)):
        downloadFile(lst[i],lsrt[i])
#createFolder('Google')
#searchFile(10,"name contains 'Getting'")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("11:45").do(job)

while 1:
    schedule.run_pending()
    time.sleep(0)

