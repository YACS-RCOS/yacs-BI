from pymongo import MongoClient
import pprint

def decodeResult(_cursor, _attribution=None):
    results = []
    if(_attribution):
        for item in _cursor:
            results.append(item[_attribution])
            # pprint.pprint(item[_attribution])
        return results
    for item in _cursor:
        pprint.pprint(item)
    return

client = MongoClient('mongodb://yacsBI:yacsBIpass@mongo_db:27017/YacsDB')
db = client["YacsDB"]
print("This is a find all records where department_id is 170")
cursor = db.courses.find({"department_id":170})
result = decodeResult(cursor)