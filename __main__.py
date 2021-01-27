import os
import good_info
import logging
from file_work import FileWork
from datetime import datetime
from db_worker import DB_Worker
import json


info_list = good_info.GoodInfoList()
    
file_goods = FileWork()
file_data = file_goods.select_path_file()

file_goods.save_in_directory()

if len(file_data) > 0:
    
    json_dict_for_logging = {
        'format_logging': '%(asctime)s %(levelname)s %(filename)s '
                          '- %(funcName)s - %(message)s',
        'level_logging': logging.INFO,
        'filemode_logging': 'a',
        'filename_logging': 'reporter.log'
    }

    logging.basicConfig(filename=json_dict_for_logging["filename_logging"], 
                        filemode=json_dict_for_logging["filemode_logging"],
                        level=json_dict_for_logging["level_logging"], 
                        format=json_dict_for_logging["format_logging"])

    info_list.get_from_file(file_data)


    json_config_script = {
        "path_to_file": os.path.join(os.getcwd(), "goods2.info"),
        "list_functions": {
            "get_from_file": info_list.get_from_file(file_data),
            "get_value": info_list.get_value_info()['mean'],
            "remove_expensive": info_list.remove_expensive(),
            "check_date_manafucture_list": info_list.\
                                             check_date_manafucture_list(),
        },    
        "command_for_execute": 'python3 '
                               '{directory_with_script} -m'.\
                                format(
                                    directory_with_script=os.getcwd()
                                ),
        "logging_settings": json_dict_for_logging
    }

    with open("config_script.json", "w") as data_file:
        json.dump(json_config_script, data_file)



