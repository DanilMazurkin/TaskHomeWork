import good_info
import logging
from file_work import FileWork

dict_with_functions = {
    "from_file_in_database": "get_from_file",
    "remove_expensive": "remove_expensive",
    "remove_overdue_goods": "check_date_manafucture_list",
    "calculate_mean": "get_value_info"
}

def exec_list_function(key_name_function):
    """
    Function read dict_config and call function
    proceeding from dict_config
    :param dict_config: dict with configures
    :type dict_config: dictionary
    :param key_name_function: name function
    :type key_name_function: string
    :return: function return -1, if in config
    not need function
    :rtype: Integer
    """

    info_list = good_info.GoodInfoList()
    file_goods = FileWork()
    file_data = file_goods.select_path_file()

    if len(file_data) > 0:
        file_goods.save_in_directory()

        if "get_from_file" in dict_with_functions.values():    
            info_list.get_from_file(file_data)

        if "get_value_info" in dict_with_functions.values():
            mean = info_list.get_value_info()['mean']
            print("Среднее значение {mean}".format(
                                                mean=mean
            ))
        
        if "remove_expensive" in dict_with_functions.values():
            info_list.remove_expensive()

        if "calculate_mean" in dict_with_functions.values():
            info_list.check_date_manafucture_list()