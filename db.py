from peewee import *

GOOGLE_SERP_TABLE_NAME = 'google_serp_202007'
LIMIT_SIZE = 10

db = MySQLDatabase("bf", host="127.0.0.1", port=3306, user="root", passwd="123456")

class BaseModel(Model):
    class Meta:
        database = db

db.connect()

class Keyword(BaseModel):
    id = IntegerField(unique=True)
    keyword = CharField(unique=True)
    country = CharField(null=True)
    type = CharField(null=True)
    class Meta:
        table_name = 'keyword'

class GoogleSerp(BaseModel):
    id = IntegerField(unique=True)
    keyword_id = IntegerField(unique=True)
    keyword = CharField(unique=False)
    rank = IntegerField(null=True)
    link = CharField(null=True)
    snippet = CharField(null=True)
    title = CharField(null=True)
    visible_link = CharField(null=True)
    class Meta:
        table_name = GOOGLE_SERP_TABLE_NAME

def get_keywords():
    sql = 'select k.keyword, k.id, k.country from keyword k left join ' + GOOGLE_SERP_TABLE_NAME + ' g on k.id = g.keyword_id where g.keyword_id is null order by k.country limit ' + str(LIMIT_SIZE) + ';'
    cursor = db.execute_sql(sql)
    res = cursor.fetchall()
    if res is None:
        return None, None
    return [(i[0], i[1]) for i in res], res[0][2]