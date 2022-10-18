import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from sheets_pivot_tables import pivot_tables

# Connect to Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("prueba-tecnica-365722-182adf42880e.json", scope)
client = gspread.authorize(credentials)
SHEET_ID = '1DRD97TAw2WIuTCG0Nh6BW-aVvDKAgY1wvJb38V-3vU8'
SHEET_NAME = 'Reto1'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

pivot_tables(url)

df = pd.read_csv(url)
print(df)