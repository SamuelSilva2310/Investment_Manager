import json


with open('../Data/data.json', 'r+') as f:
	json_data = json.load(f)
	json_data['account'][0]['balance'] = 0
	print(json_data)
	json.dump(json_data,f)
	f.close()


def get_Balance(data = json_data):
	return data['account'][0]['balance'] + 1




