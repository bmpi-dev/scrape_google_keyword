import xlwings as xw

# parse excel

wb = xw.Book('all_tag_store.xlsx')

s1 = wb.sheets['tag_merged']
s2 = wb.sheets['store']

k1 = s1.range('B2:B20087').value
c1 = s1.range('D2:D20087').value
c1 = list(map(lambda x: 'uk' if x == 'gb' else x, c1))
k2 = s2.range('B2:B18539').value
c2 = s2.range('D2:D18539').value
c2 = list(map(lambda x: 'uk' if x == 'gb' else x, c2))

# connect db

from peewee import *

db = MySQLDatabase("bf", host="127.0.0.1", port=3306, user="root", passwd="123456")

class BaseModel(Model):
    class Meta:
        database = db

db.connect()

class Keyword(BaseModel):
    keyword = CharField(unique=True)
    country = CharField(null=True)
    type = CharField(null=True)

i1 = 0
for k in k1:
    x = Keyword(keyword = k, country = c1[i1], type = 'tag')
    x.save()
    i1 = i1 + 1

i2 = 0
for k in k2:
    x = Keyword(keyword = k, country = c2[i2], type = 'store')
    x.save()
    i2 = i2 + 1