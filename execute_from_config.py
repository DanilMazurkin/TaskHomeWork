import good_info
import logging
from file_work import FileWork



def exec_list_function(dict_config):
    """
    Function read dict_config and call function
    proceeding from dict_config
    :return: function return -1, if in config
    not need function
    :rtype: Integer
    """

    info_list = good_info.GoodInfoList()
    file_goods = FileWork()
    file_data = file_goods.select_path_file()

    dict_with_functions = {
        "get_from_file": info_list.get_from_file,
        "remove_expensive": info_list.remove_expensive,
        "check_date_manafucture_list": info_list.check_date_manafucture_list,
        "get_value_info": info_list.get_value_info
    }

    if len(file_data) > 0:
        file_goods.save_in_directory()
        
        dict_config["execute_function"] = "get_from_file"
        dict_with_functions[dict_config["execute_function"]](file_data)
        
        dict_config["execute_function"] = "remove_expensive"
        dict_with_functions[dict_config["execute_function"]]()
        
        dict_config["execute_function"] = "get_value_info"
        mean = dict_with_functions[dict_config["execute_function"]]()["mean"]
        print("Среднее значение {mean}".format(mean=mean))
        
        dict_config["execute_function"] = "check_date_manafucture_list"
        dict_with_functions[dict_config["execute_function"]]()