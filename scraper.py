import requests
import json
from db import *
import logging

logging.basicConfig(format='%(asctime)s %(message)s', filename='run.log', level=logging.DEBUG)

se_scraper_url = "http://localhost:3000"
# proxy_url = "docker.for.mac.host.internal:8000"
proxy_url = "192.168.10.224:8000"
search_engine = "google"
keywords_num = 1
keywords_hl = "en"
keywords_start = 0
keywords_size = 10

def start():
    if not db.is_connection_usable:
        db.connect()

    logging.info("start scrape google!!!")

    keywords_ids, keywords_gl = get_keywords()
    keywords = [i[0] for i in keywords_ids]

    if keywords is not None:
        payload = {
            "browser_config": {
                "log_ip_address": False,
                "proxies": [
                    proxy_url
                ],
                "use_proxies_only": False,
                "debug_level": 1,
                "puppeteer_cluster_config": {
                    "timeout": 3 * 60 * 1000,
                    "monitor": False,
                    "concurrency": "Cluster.CONCURRENCY_BROWSER",
                    "maxConcurrency": 5,
                }
            },
            "scrape_config": {
                "search_engine": search_engine,
                "keywords": keywords,
                "num_pages": keywords_num,
                "google_settings": {
                    "gl": keywords_gl,
                    "hl": keywords_hl,
                    "start": keywords_start,
                    "num": keywords_size
                }
            }
        }

        headers = {
        'Content-Type': 'application/json'
        }
        
        try:
            response = requests.post(se_scraper_url, headers=headers, data = json.dumps(payload), timeout = 59)
        except:
            logging.warning('failure # requests time out!!!')
            if not db.is_closed:
                db.close()
            return

        res_json = response.json()

        for keyword_id in keywords_ids:
            try:
                keyword_dict = res_json['results'][keyword_id[0]]
                serps = keyword_dict['1']['results']
                for item in serps:
                    google_serp = GoogleSerp(keyword_id = keyword_id[1], keyword = keyword_id[0], rank = item['rank'], link = item['link'], snippet = item['snippet'], title = item['title'], visible_link = item['visible_link'])
                    google_serp.save()
                    logging.info("success # save serp rank " + str(item['rank']) + " of keyword " + keyword_id[0])
                logging.info("success # save keyword: " + keyword_id[0])
            except:
                logging.warning("failure # save keyword: " + keyword_id[0])
                logging.warning("failure # keyword json is: " + json.dumps(keyword_dict))
                
    if not db.is_closed:
        db.close()