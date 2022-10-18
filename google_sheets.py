import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from sheets_pivot_tables import pivot_tables

# Connect to Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("prueba-tecnica-365722-61ca5f29dbac.json", scope)
client = gspread.authorize(credentials)
SHEET_ID = '1DRD97TAw2WIuTCG0Nh6BW-aVvDKAgY1wvJb38V-3vU8'
SHEET_NAME = 'Reto1'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

breakpoint()

gc = gspread.authorize(credentials)
wb = gc.open_by_url(url) # A URL of your workbook.
sheet1 = wb.worksheet(SHEET_NAME) # Enter your sheet name.
original_df = sheet1.get_all_values()
df = pd.DataFrame(original_df)
df.head()
source_sheet_id = sheet1.get('replies')[0].get('addSheet').get('properties').get('sheetId')
target_sheet_id = sheet1.get('replies')[1].get('addSheet').get('properties').get('sheetId')
requests = []
pivot_tables(SHEET_ID)

df = pd.read_csv(SHEET_ID)
print(df)