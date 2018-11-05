import os
from apiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SAMPLE_SPREADSHEET_ID = '1wguriaDRPzJaYQo4avyYn7r9A3g09NVAF-QFFwelTfc'
RANGE_NAME = 'today!A2:B' # Spreadsheet name! range

def main():
    GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', None)
    credentials = service_account.Credentials.from_service_account_file(GOOGLE_APPLICATION_CREDENTIALS, scopes=SCOPES)
    spreadsheet_service = build('sheets', 'v4', credentials=credentials)
    result = spreadsheet_service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    print(values)

if __name__ == '__main__':
    main()
