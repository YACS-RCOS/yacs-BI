from pymongo import MongoClient

def insert_to_log(json_message):
	client = MongoClient('mongodb://yacsBI:yacsBIpass@mongo_db:27017/YacsDB')
	db = client["YacsDB"]
	db.log.insert_one(json_message)


