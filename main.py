from scraper import *
import schedule
import time

schedule.every(30).seconds.do(start)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)