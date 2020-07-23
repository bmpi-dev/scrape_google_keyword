import schedule
import time
import docker

def restart_scraper():
    client = docker.from_env()
    client.containers.get('se-scraper').restart()

schedule.every(2).hours.do(restart_scraper)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)