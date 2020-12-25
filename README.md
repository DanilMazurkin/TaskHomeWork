# TaskHomeWork
## Домашнее задание по курсам от компании Fogstream

Программа парсит файл goods, в нем хранится список товаров в формате: <имя товара>:<цена товара>:<количество товаров>:<дата>  
Точка запуска программа происходит через модуль reporter, необходимо запускать именно этот модуль  
Файл goods.info находится в одной директории вместе с py файлом  

Реализованы следующие классы: GoodInfo, GoodInfoList  
GoodInfo: класс, который представляет товар в программе  
GoodInfoList: класс, который представляет список товаров в программе  

Реализованы следующие публичные функции в GoodInfoList:  

add(name, price, amount) (добавляет файл в список)  
get_from_file(filename)  (возвращает список товаров)  
add_goods_in_list(list_with_products) (добавляется товар в список)  
remove(name) (удаляет товар по имени)  
remove_expensive() (удаляет самый дорогой товар)  
remove_last() (удаляет последний товар)  
sort(key) (сортировка списка товаров по ключам)  
get_list_most_expensive() (получает список самых дорогих товаров)  
get_list_ending_goods()  (получает спискос самых заканчивающихся товаров)  
get_value_info()  (получает информацию о среднем значении и общем количестве товаров)  
get_list_with_cheap_goods()  (получает список самых дешевых товаров)  
get_std() (получает стандартное отклонение по цене товаров)  
len() (возвращает длину списка)  
check_date_import_list() (удаляет товары у которых кончился срок годности)

Реализованы следующие публичные функции в FileUser:  
select_path_file() - выбрать путь для сохранения
save_by_directory() - сохранить путь в указанную пользователем директорию
