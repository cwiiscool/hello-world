from pymongo import MongoClient


c = MongoClient("mongodb://cwi:123@127.0.0.1:27017")
table = c['car']['info']
link = []
name = []
for i in list(table.find()):
    link.append(i['link'])
print(li)
