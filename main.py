import find
import datetime
import settings
import scraping
import requests

def main():
    dt_now = datetime.datetime.now()
    race = scraping.syussou()
    day = dt_now.strftime("%Y年%m月%d日")
    notification_message = "\n"+ day
    for (h,f) in zip(settings.horse, settings.horse_F):
        res = find.finder(h, race)
        notification_message =notification_message +"\n"+h+"\n"+f
        for r in res:
            notification_message =notification_message+ "\n"+ r 
    send_line_notify(notification_message)



def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = '自分のtoken'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)
    
if __name__ == "__main__":
    main()
