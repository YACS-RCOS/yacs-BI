from .mongo_connection import * 
#error handling file
def handle(error):
    file = open('error_handle.txt','w')
    file.write(error)

def helo():
	print("Hola")

def db_report(message):
	insert_to_log({"message":message})