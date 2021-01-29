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
    'PASS_DB': os.environ.get('CONPASS'),
    'filemode_logging': 'a',
    'filename_logging': 'reporter.log',
    "execute_function": "exec_list_function",
    "run __main__": 'python3 '
                    '{directory_with_script} -m'.\
                            format(
                                directory_with_script=os.path.\
                                                        dirname(os.path.\
                                                        realpath(__file__))
                            )
}

logging.basicConfig(filename=dict_config["filename_logging"], 
                    filemode=dict_config["filemode_logging"],
                    level=dict_config["level_logging"], 
                    format=dict_config["format_logging"])


if "exec_list_function" in dict_config.values():
    exec_list_function()


path_to_config = os.path.join(os.path.dirname(os.path.\
                                            realpath(__file__)),
                                            "config_script.json")
        
with open(path_to_config, "w") as fp:
    json.dump(dict_config, fp, indent=5)


