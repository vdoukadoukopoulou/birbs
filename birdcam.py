import schedule
import time
from goprohero import GoProHero

def job():
    print("I'm working...")
    camera = GoProHero(password='florentijn')
    print("I'm doing job...")
    camera.command('power', 'on')
    time.sleep(30)
    camera.command('record', 'on')
    time.sleep(7200)
    camera.command('record', 'off')
    camera.command('power', 'sleep')
    print("I did job...")

schedule.every().day.at("05:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)









