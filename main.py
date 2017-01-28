import ui
import console
from datetime import datetime
from logic.google import Google


def send_kakidame(sender):
    v = sender.superview
    send_text = v['textview1'].text
    # send_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    ggl = Google()
    send_date = ggl.send(send_text)
    console.alert(send_date)

def clear_text(sender):
    v = sender.superview
    v['textview1'].text = ''

v = ui.load_view()
v.present('sheet')

'''
if __name__ == '__main__':
    console.alert('test')
    '''
