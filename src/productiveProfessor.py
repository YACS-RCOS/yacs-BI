from pymongo import MongoClient
import pprint

def decodeResult(_cursor, _attribution=None):
    results = []
    if(_attribution):
        for item in _cursor:
            results.append(item[_attribution])
        return results
    for item in _cursor:
        pprint.pprint(item)
    return


client = MongoClient('mongodb://yacsBI:yacsBIpass@mongo_db:27017/YacsDB')
db = client["YacsDB"]

all_sections_in_Fall16 = db.sections.find({"semester_id":85366})
profs = dict()

for section in all_sections_in_Fall16:
	prof = section["section_times"][0]["instructor"]
	if prof in profs.keys():
		profs[prof] += 1
	else:
		profs[prof] = 1

for x in sorted(profs):
    print(x, profs[x])