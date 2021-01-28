import good_info
import logging
from file_work import FileWork


def exec_list_function(dict_config):

    info_list = good_info.GoodInfoList()

    if "add_from_file_in_database" in dict_config["list_function"]:
    
        file_goods = FileWork()
        file_data = file_goods.select_path_file()

        if len(file_data) > 0:
            file_goods.save_in_directory()
            info_list.get_from_file(file_data)
        else:
            return -1
    
    else:
        logging.error("В конфиге нет функции для загрузки из файла в базу")
    
    if "calculate_mean" in dict_config["list_function"]:
        info_list.get_value_info()['mean']
    else:
        logging.error("В конфиге нет функции для расчета среднего")
    
    if "remove_expensive" in dict_config["list_function"]:
        info_list.remove_expensive()
    else:
        logging.error("В конфиге нет функции для удаления дорогого товара")

    if "remove_overdue_goods" in dict_config["list_function"]:
        info_list.check_date_manafucture_list()
    else:
        logging.error("В конфиге нет функции для удаления просроченных товаров")