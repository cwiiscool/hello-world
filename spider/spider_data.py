from pymongo import MongoClient


def spider_data():
    conn = MongoClient("mongodb://cwi:123@127.0.0.1:27017")
    table = conn['jd']
    return table.jd_data.find()

# for data in list(table.jd_data.find()):
#     print(data)
#     print(type(data))


datas = spider_data()
for i in datas:
    print(i['title'])
