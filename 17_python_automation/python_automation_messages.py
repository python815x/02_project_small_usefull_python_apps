import requests
import schedule
import time


def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '', # add you phone number here
        'message': 'This is Michael Guilfoyle AKA IfMyante! The agent of the money changers!',
        'key': 'textbelt',
    })
    print(resp.json())


# schedule.every().day.at("15:00").do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)