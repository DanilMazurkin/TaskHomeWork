import json

dict_config = {"path_to_data": "/home/jatx/TaskHomeWork2/goods2.info"}

print("test")

with open('config.json', 'w') as file_data:
    json.dump(dict_config, file_data)
