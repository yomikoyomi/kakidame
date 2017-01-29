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
        path = os.path.expanduser('logic/oauth.json')

        credencials = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
        client = gspread.authorize(credencials)
        # gfile = client.open_by_key(doc_id)
        gfile = client.open('test')
        worksheet = gfile.sheet1

        return worksheet

    def send(self, oauth, text):
        now_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        worksheet = oauth
        num = 3
        
        # TODO: 挿入箇所取得ロジック改修
        while worksheet.cell(num, 2).value != '':
            num = num +
        
        worksheet.update_cell(num, 2, now_date)
        worksheet.update_cell(num, 3, text)
        
        return text

