import schedule
import time
import requests

r = requests.get('http://127.0.0.1:5000/download')

def job():
    print("I'm working...")
    r = requests.get('http://127.0.0.1:5000/download')

schedule.every(3).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)