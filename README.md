# scrape google keyword

## How To Start

0. install dependencies

```
pip install -r requirements.txt
npm install
```

1. start proxy server

```
node proxy.js
```

2. start se-scraper

```
docker run --name se-scraper -m 2gb --restart always -p 3000:3000 tschachn/se-scraper:latest
```

3. start mysql DB

```
docker run --name bf-mysql -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 -d mysql:latest
```

- create database `bf`

- execute sql in `bf.sql`

- execute `python excel2db.py` to migrate data from excel to database

- execute `remove_duplicate.sql` to remove duplicate keyword in table

4. start main function

```
python main.py
```

5. restart docker `se-scraper` container every 2 hours

```
python task.py
```
