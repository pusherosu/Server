#!/usr/bin/python

import argparse
from googleapiclient.discovery import build, MediaFileUpload
from google.oauth2 import service_account

parser = argparse.ArgumentParser(description='Automatic backup script')
parser.add_argument('-f', required=True, type=str, help='Name of the file to be backed up')
args = parser.parse_args()

SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = './credentials2.json'
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

if __name__ == "__main__":
	file_metadata = {
		'name': args.f,
		'description': 'Scheduled server backup',
		'mimeType': 'application/tar'
	}
	service = build('drive', 'v3', credentials=creds)

	media=MediaFileUpload(args.f, mimetype='application/tar')
	cloudFile = service.files().create(body=file_metadata, media_body=media).execute()

	cloudPermissions = service.permissions().create(
		fileId=cloudFile['id'], 
		body={
			'type': 'user', 
			'role': 'reader', 
			'emailAddress': 'youraddress@gmail.com'
		}
	).execute()
