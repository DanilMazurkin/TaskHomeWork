# TaskHomeWork
## Домашнее задание по курсам от компании Fogstream

Программа парсит файл goods, в нем хранится список товаров в формате: <имя товара>:<цена товара>:<количество товаров>:<дата>  
Программа работает c базой данной postgres.  
Файл goods.info находится в одной директории вместе с py файлом  

Реализованы следующие классы: GoodInfo, GoodInfoList  
GoodInfo: класс, который представляет товар в программе  
GoodInfoList: класс, который представляет список товаров в программе  

Она запускается как модуль следующей командой: python3 <имя_вашей_папки> -m  
Создается JSON файл конфига со следующими полями:  

{  
     "path_to_data": "/home/jatx/TaskHomeWork3/goods2.info",  
     "format_logging": "%(asctime)s %(levelname)s %(filename)s - %(funcName)s - %(message)s",  
     "level_logging": 20,  
     "PASS_DB_ENV": "CONPASS",  
     "NAME_DB_ENV": "DBNAME",  
     "HOST_DB_ENV": "DBHOST",  
     "USER_NAME_DB_ENV": "USER_NAME",  
     "filemode_logging": "a",  
     "filename_logging": "reporter.log",  
     "execute_function": "get_from_file",  
     "exec_all_function": false  
}  

Для запуска все функций необходимо "exec_all_function" установить как true  
В "execute_function" можно установить имя одной из функции  
[  
    "get_from_file",  
    "remove_expensive",  
    "check_date_manafucture_list",  
    "get_value_info",  
]  


Реализованы 17 тестов для БД:  
Запускаются следующим образом:  
1) Перейти в папку с проектом  
2) Запустить: python3 -m unittest good_info_tests.py  

Реализованы следующие публичные функции в GoodInfoList:  

remove_expensive (удаляет самый дорогой товар)  
check_date_manafucture_list() (проверяет срок годности товаров)  
remove_last() (удаляет последний товар)  
get_std() (получает среднеквадратичное отклонение)  
get_from_file(filedata)  (возвращает список товаров)  
remove(name) (удаляет товар по имени)  
remove_expensive() (удаляет самый дорогой товар)  
remove_last() (удаляет последний товар)  
sort(key) (сортировка списка товаров по ключам)  
get_list_most_expensive() (получает список самых дорогих товаров)  
get_list_ending_goods()  (получает спискос самых заканчивающихся товаров)  
get_value_info()  (получает информацию о среднем значении и общем количестве товаров)  
get_list_with_cheap_goods()  (получает список самых дешевых товаров)  
get_all_goods() (возвращает все товары)  
product_buy(name, amount) (покупает товар с количеством amount и именем name)  

Реализованы следующие публичные функции в FileWork:  
select_path_file() - выбрать путь для сохранения  
save_in_directory() - сохранить путь в указанную пользователем директорию  
