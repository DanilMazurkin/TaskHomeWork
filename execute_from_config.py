import good_info
import logging
from file_work import FileWork


info_list = good_info.GoodInfoList()

def exec_all_function():
    file_goods = FileWork()
    file_data = file_goods.select_path_file()

    if len(file_data) > 0:
        file_goods.save_in_directory()
        info_list(file_data)
        
    info_list.remove_expensive()
    info_list.check_date_manafucture_list()
    info_list.get_value_info()

dict_with_functions = {
    "get_from_file": info_list.get_from_file,
    "remove_expensive": info_list.remove_expensive,
    "check_date_manafucture_list": info_list.check_date_manafucture_list,
    "get_value_info": info_list.get_value_info,
    "exec_all_functions": exec_all_function
}    

def exec_function(dict_config):
    """
    Function read dict_config and call function
    proceeding from dict_config
    :return: function return -1, if in config
    not need function
    :rtype: Integer
    """

    if dict_config["execute_function"] == "get_from_file":
        
        file_goods = FileWork()
        file_data = file_goods.select_path_file()

        if len(file_data) > 0:
            file_goods.save_in_directory()
            dict_with_functions[dict_config["execute_function"]](file_data)
    
    elif dict_config["execute_function"] in dict_with_functions.values():
        dict_with_functions[dict_config["execute_function"]]()
    else:
        return False
