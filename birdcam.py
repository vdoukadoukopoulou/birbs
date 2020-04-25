from dotenv import load_dotenv
import os
import schedule
import time
from goprohero import GoProHero

localtime = time.asctime( time.localtime(time.time()) )
print(localtime,"I set up camera...")
load_dotenv()
your_password = os.getenv("KEY")
camera = GoProHero(password=your_password)
print(localtime,"I did set up camera...")

def job():
    print(localtime,"I'm working...")
    print(localtime,"I'm doing job...")
    camera.command('power', 'on')
    time.sleep(30)
    camera.command('record', 'on')
    time.sleep(7200)
    camera.command('record', 'off')
    camera.command('power', 'sleep')
    print(localtime,"I did job...")

schedule.every().day.at("05:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)









