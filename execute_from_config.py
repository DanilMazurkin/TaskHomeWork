import good_info
import logging
from file_work import FileWork


def exec_list_function():
    """
    Function read dict_config and call function
    proceeding from dict_config
    :param dict_config: dict with configures
    :type dict_config: dictionary
    :return: function return -1, if in config
    not need function
    :rtype: Integer
    """

    info_list = good_info.GoodInfoList()
    
    list_function = [
        "get_from_file",
        "get_value_info",
        "remove_expensive",
        "check_date_manafucture_list"
    ]

    if "get_from_file" in list_function:
    
        file_goods = FileWork()
        file_data = file_goods.select_path_file()

        if len(file_data) > 0:
            file_goods.save_in_directory()
            info_list.get_from_file(file_data)
    
    else:
        logging.error("В конфиге нет функции для"\
                      "загрузки из файла в базу")
        return -1


    if "get_value_info" in list_function:
        mean = info_list.get_value_info()['mean']
        print("Среднее значение {mean}".format(
                                        mean=mean
        ))
    else:
        logging.error("В конфиге нет функции для расчета среднего")
        return -1


    if "remove_expensive" in list_function:
        info_list.remove_expensive()
    else:
        logging.error("В конфиге нет функции для удаления дорогого товара")
        return -1


    if "check_date_manafucture_list" in list_function:
        info_list.check_date_manafucture_list()
    else:
        logging.error("В конфиге нет функции для удаления"\
                      "просроченных товаров")
