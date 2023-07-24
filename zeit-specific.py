# python run code at specific time
# search of the library
# schedule



import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


'''
import schedule
import time

def job():
    print("I am anas")

schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
'''