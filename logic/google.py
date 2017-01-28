from datetime import datetime


class Google:
    def test(self):
        now_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    
        return now_date
    
    def send(self, text):
        return text
