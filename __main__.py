import os
import logging
import json
from execute_from_config import exec_list_function


dict_config = {
    "path_to_data": os.path.join(os.path.dirname(
                                                os.path.realpath(__file__)), 
                                                "goods2.info"),
        
    'format_logging': '%(asctime)s %(levelname)s %(filename)s '
                          '- %(funcName)s - %(message)s',
    'level_logging': logging.INFO,
    'PASS_DB_ENV': 'CONPASS',
    'NAME_DB_ENV': 'DBNAME',
    'HOST_DB_ENV': 'DBHOST',
    'USER_NAME_DB_ENV': 'USER_NAME',
    'filemode_logging': 'a',
    'filename_logging': 'reporter.log',
    "execute_function": "exec_list_function"
}

logging.basicConfig(filename=dict_config["filename_logging"], 
                    filemode=dict_config["filemode_logging"],
                    level=dict_config["level_logging"], 
                    format=dict_config["format_logging"])

if "execute_function" in dict_config.keys():
    exec_list_function(dict_config["execute_function"])


path_to_config = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                             "config_script.json")
        
with open(path_to_config, "w") as fp:
    json.dump(dict_config, fp, indent=5)


