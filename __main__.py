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
    'filemode_logging': 'a',
    'filename_logging': 'reporter.log',
        
    "list_function": {
        "calculate_mean": "get_value_info",
        "add_from_file_in_database": "get_from_file",
        "remove_expensive_good": "remove_expensive",
        "remove_overdue_goods": "check_date_manafucture_list",
        "execute_list_function": "exec_list_function"
    },

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


if "exec_list_function" in dict_config["list_function"].values():
    exec_list_function(dict_config)


path_to_config = os.path.join(os.path.dirname(os.path.\
                                            realpath(__file__)),
                                            "config_script.json")
        
with open(path_to_config, "w") as fp:
    json.dump(dict_config, fp, indent=5)


