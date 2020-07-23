import requests
import json
import tablib

data = tablib.Dataset()

url = 'https://scrapeulous.com/api'

payload = {
    "API_KEY": "tupQujeFZRHXW5-FhpYc8UhrSFHva4KYAb5vH-cub-I",
    "function": "https://raw.githubusercontent.com/NikolaiT/scrapeulous/master/google_scraper.js",
    "items": ["A.C. Moore Black Friday","Musician's Friend Black Friday","IKEA Black Friday","Kirkland's Black Friday","Gaffos Black Friday","Clark's Black Friday","Kelsi Dagger Brooklyn Black Friday","Ray-Ban Black Friday","PrinterPix Black Friday","Journeys Black Friday","Ribbons Black Friday","Chico's Black Friday","Kipling Black Friday","ICuracao Black Friday","Williams Sonoma Black Friday","Wigsbuy Black Friday","T.M.Lewin Black Friday","AllPosters Black Friday","Tilly's Black Friday","Jet Black Friday","Amazon Black Friday","Kohl's Black Friday","Vudu Black Friday","Newegg Black Friday","Fossil Black Friday","Woot! Black Friday","Lowes Black Friday","Sam's Club Black Friday","Macy's Black Friday","Cabelas Black Friday","Boscov's Black Friday","Proozy Black Friday","Cdkeys Black Friday","BuyDig Black Friday","Left Coast Threads Black Friday","GearBest Black Friday","13deals Black Friday","Timberland Black Friday","Dyson Black Friday","UBER Black Friday","Apple Black Friday","ThinkGeek Black Friday","SkinStore Black Friday","Udemy Black Friday"]
}

r = requests.post(url, data=json.dumps(payload))

res_json = r.json()

with open('out.json', 'wb') as f:
    f.write(json.dumps(res_json, sort_keys=True, indent=4).encode())

data.headers = ('item', 'rank', 'link', 'title', 'snippet', 'visible_link')

for item in res_json:
    if type(item['result']) is dict and item['result'].get('error_message') is not None:
        continue

    for result in item['result'][0]['results']:
        data.append([item['item'], result['rank'], result['link'], result['title'], result['snippet'], result['visible_link']])

with open('out.xls', 'wb') as f:
    f.write(data.export('xls'))
