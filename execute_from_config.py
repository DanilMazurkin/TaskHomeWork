import good_info
import logging
from file_work import FileWork



def exec_list_function():
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
        
        dict_with_functions["get_from_file"](file_data)
        dict_with_functions["remove_expensive"]()
        
        mean = dict_with_functions["get_value_info"]()["mean"]
        print("Среднее значение {mean}".format(mean=mean))
        
        dict_with_functions["check_date_manafucture_list"]()