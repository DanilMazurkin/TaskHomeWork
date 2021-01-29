import good_info
import logging
from file_work import FileWork


def exec_list_function(dict_config, key_name_function):
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

    if key_name_function in dict_config.values():
        info_list = good_info.GoodInfoList()
        file_goods = FileWork()
        file_data = file_goods.select_path_file()

        if len(file_data) > 0:
            file_goods.save_in_directory()
            info_list.get_from_file(file_data)

            mean = info_list.get_value_info()['mean']
            print("Среднее значение {mean}".format(
                                            mean=mean
            ))
            info_list.remove_expensive()
            info_list.check_date_manafucture_list()
    else:
        logging.error("В конфиге нет этой функции")
        print("В конфиге нет этой функции")
        return -1