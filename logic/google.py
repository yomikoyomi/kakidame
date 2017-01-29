import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime


class Google:
    def test(self):
        now_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    
        return now_date
    
    def oauth(self):
        scope = ['https://spreadsheets.google.com/feeds']
        path = os.path.expanduser('oauth.json')

        credencials = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
        client = gspread.authorize(credencials)
        # gfile = client.open_by_key(doc_id)
        gfile = client.open('test')
        worksheet = gfile.sheet1
        records = worksheet.get_all_values()

        # for record in records:
        #     print(record)

        return worksheet

    def send(self, oauth, text):
        now_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        worksheet = oauth()
        num = 3
        while worksheet.cell(num, 2).value != '':
            num = num + 1
        worksheet.update_cell(num, 2, now_date)
        worksheet.update_cell(num, 3, text)
        return text


