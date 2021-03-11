from time import sleep
from Mongo.mongodb_service import MongodbService
#from sklearn.preprocessing import StandardScaler
#import cgi, cgitb

def predict(dto):
	storage = MongodbService.get_instance()
	print(dto)
	storage.set_input_transaction(dto)
	result = None
	while result is None:
		sleep(0.5)
		result = storage.get_output_transaction()
	return result