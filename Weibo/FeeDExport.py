import datetime
import json

#"ABC"+"_"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class FeedExp(object):
	"""docstring for FeedExp"""
	# def __init__(self):

	def tojson(self, json_data):
		fimename = "WeboData_"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+".json"
		fimename = fimename.replace(' ', '')
		fimename = fimename.replace(':', '')
		fimename = fimename.replace('-', '')
		print("\nwrite data to file now.....")
		with open(fimename, 'w') as f:
			json.dump(json_data, f)
			f.close()
	
    

