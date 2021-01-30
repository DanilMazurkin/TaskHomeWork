import good_info
import logging
from file_work import FileWork

info_list = good_info.GoodInfoList()

dict_with_functions = {
    "get_from_file": info_list.get_from_file,
    "remove_expensive": info_list.remove_expensive,
    "check_date_manafucture_list": info_list.check_date_manafucture_list,
    "get_value_info": info_list.get_value_info
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

def exec_all_function(config_data):
    """
    If in config set exec_all_function as True
    then function execute all functions from
    dict_with_functions
    :param config_data: dictionary with config
    from JSON file
    :type config_data: dictionary
    :return: return False if exec_all_function
    is False
    :rtype: bool
    """

    if config_data["exec_all_function"]:
        file_goods = FileWork()
        file_data = file_goods.select_path_file()

        if len(file_data) > 0:
            file_goods.save_in_directory()
            dict_with_functions["get_from_file"](file_data)
        
        dict_with_functions["remove_expensive"]()
        dict_with_functions["check_date_manafucture_list"]()
        dict_with_functions["get_value_info"]()
    else:
        return False
