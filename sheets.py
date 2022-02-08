from __future__ import print_function
from datetime import datetime

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import webbrowser

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def initialize():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            browser_available = False
            try:
                webbrowser.get()
                browser_available = True
            except:
                browser_available = False
            
            if browser_available:
                creds = flow.run_local_server(port=0)
            else:
                creds = flow.run_console()

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        return service.spreadsheets()
    except HttpError as err:
        print(err)

sheets = initialize()

def insert_speedtest_result(speedtest, spreadsheet):
    values = [
        [
            datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            speedtest.download / 1000000,
            speedtest.upload / 1000000,
            speedtest.ping
        ]
    ]
    body = {
        'values': values
    }
    sheets.values().append(
        spreadsheetId=spreadsheet,
        range = 'Speedtest',
        valueInputOption = 'USER_ENTERED',
        body = body 
    ).execute()
