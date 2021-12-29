import find
import datetime
import settings
import requests

def main():
    dt_now = datetime.datetime.now()
    day = dt_now.strftime("%Y年%m月%d日")
    res = find.finder()
    notification_message ="\n"+settings.horse+"\n"+day
    for r in res:
        notification_message =notification_message+ "\n"+ r 
    send_line_notify(notification_message)



def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = 'sqeTArSjsznpEiyaixwSsJkMxW9iXxcuKmF77AZK38Q'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)
    
if __name__ == "__main__":
    main()