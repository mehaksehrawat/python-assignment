import schedule
import time
import datetime

def job():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print( str(TNOW) +" spanish speaker")

def support():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print( str(TNOW) +" support")


def sales():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print( str(TNOW) +" sales")


def operation():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print( str(TNOW) +" operation")

def minjob():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print('\n' + str(TNOW) +" This prints every min \n")

schedule.every(1).minutes.do(minjob)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(support)
schedule.every().minute.at(":17").do(sales)
schedule.every().minute.at(":05").do(support)
schedule.every().minute.at(":10").do(operation)
schedule.every().minute.at(":15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
