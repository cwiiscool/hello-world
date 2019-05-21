from pymongo import MongoClient

table = None
c = None


def connent_server(data):
    global table,c
    c = MongoClient("mongodb://cwi:123@127.0.0.1:27017")
    id = data['id']
    print(id)
    table = c[str(id)]['car_info']


def insert_data(data):
    if not table:
        connent_server(data)
    table.insert(data)


# if __name__ == '__main__':
#     insert_data({"user":"cwi"})