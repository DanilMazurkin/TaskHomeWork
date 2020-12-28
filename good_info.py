from math import sqrt
from datetime import datetime, timedelta
import logging 


class GoodInfo:
    """
    Represents good info

    Attributes:

    name (str): name product
    price (float): price product
    amount (int): amount product
    date_import (datetime): date import
    shelf_life (int) (shelf_life): shelf life

    Methods:

    __init__(str, float, int)
    __str__()

    """

    def __init__(self, name, price, amount, date_import, shelf_life):
        """
        Initialize name, price, amount, date_import, shellf_life

        :param name: name product
        :type name: string
        :param price: price product
        :type price: Number
        :param amount: amount product
        :type amount: Number
        :param date_import: string with date
        :type date_import: string
        :param shell_life: Shell life good
        :type shell_life: Integer
        """
        self.name = name
        self.price = price
        self.amount = amount
        self.date_import = date_import
        self.shelf_life = shelf_life

    def __str__(self):
        """
        Function make string with represents good
        :return: string represents good
        :rtype: string
        """
        return "{name} : (Количество) {amount} (Цена) {price} \n \
                (Дата) {date} (Срок годности) {shelf_life} \n".format(
                name=self.name,
                amount=self.amount,
                price=self.price,
                date=self.date_import,
                shelf_life=self.shelf_life
        )

    @staticmethod
    def check_product_data(name, price, amount, date_import, shelf_life):
        """
        Check format data product from list with products
        
        :param name: name good
        :type name: string

        :param price: price good
        :type price: integer
        
        :param price: price good
        :type price: string
        
        :param amount: amount good
        :type amount: string
        
        :param date_import: string with date
        :type date_import: string
        
        :param shelf_life: shelf life good
        :type shelf_life: string
        
        :return: Return True if format right else return
        false if format not right
        :rtype: Return bool value
        """
        
        if name == "":
            return False

        if (not price.isdigit() and not amount.isdigit() and 
            not shelf_life.isdigit()):
            return False
        
        shelf_life = int(shelf_life)
        price = int(price)
        amount = int(amount)

        if (shelf_life > 0 and price > 0 
            and amount > 0 and GoodInfo.__check_date(date_import)):
            return True
        
        return False

    @staticmethod
    def __check_date(good_date):
        """
        Check date on right format
        :param good_date: string with date 
        :type good_date: string
        :return: true if date of delivery less then 
        current date, else false
        :rtype: bool 
        """

        date_import =  datetime.strptime(good_date, "%Y-%m-%d")
        today = datetime.today()

        if date_import < today:
            logging.error("Дата поставки меньше текущей!")
            return False
        else:
            return True
    
    @staticmethod
    def check_shell_life_good(good_date, shelf_life):
        """
        Check shell life
        :param good_date: str with date
        :type good_date: string
        :param shelf_life: shelf life of date
        :type shelf_life:
        :return: return true if shelf life end and return
        False if shelf life not end
        """

        shelf_life = timedelta(days=int(shelf_life))
        ending_shelf_life = good_date + shelf_life
        today = datetime.today()

        if today > ending_shelf_life:
            return True
        else:
            return False


class GoodInfoList:
    """
    Represents good info

    Attributes:

    list_with_goods (list(GoodInfo)): list of goods

    Methods:

    __init__(str, float, int)
    __str__()
    add(name, price, amount)
    get_from_file(filename)
    add_goods_in_list(list_with_products)
    __check_product_data(good_data)
    remove(name)
    remove_expensive()
    get_list_most_expensive()
    get_list_ending_goods()
    sort(key)
    __getitem__(name)
    get_value_info()
    get_list_with_cheap_goods()

    """

    def __init__(self):
        """ 
        Initiliaize empty list with no goods
        """
        self.list_with_goods = list()

    def __str__(self):
        """
        Function make string with represents GoodInfo
        :return: string represents GoodInfo
        :rtype: string
        """
        
        string_with_list = ""

        for elem in self.list_with_goods:
            string_with_list += str(elem) + '\n'

        return string_with_list

    def __len__(self):
        """
        Return length GoodInfoList
        """

        logging.info("Длина списка: {len}".format(len=len(self.list_with_goods)))

        return len(self.list_with_goods)

    def remove_last(self):
        """
        Function remove last good in ListGoods
        :return: Nothing return
        """

        logging.info("Удаление последнего товара из списка")

        index_last_good = len(self.list_with_goods) - 1
        last_good = self.list_with_goods[index_last_good]

        self.remove(last_good.name)

    def get_std(self):
        """
        Function calculate standard deviation
        :return: standard deviation
        :rtype: float
        """

        value_info = self.get_value_info()
        mean = value_info['mean']
        squared_deviations = list()
        

        for good_data in self.list_with_goods:
            squared_deviations.append((good_data.price - mean) ** 2)
        
        dispersion = sum(squared_deviations) / len(self.list_with_goods)
        logging.info("Стандартное отклонение: {std}".format(std=sqrt(dispersion)))

        return sqrt(dispersion)
        
    def add(self, good_info):
        """"
        Add GoodInfo in GoodInfoList
        :param good_info: object GoodInfo
        :type good_info: GoodInfo
        :return: function nothing return
        """
        self.list_with_goods.append(good_info)

    def get_from_file(self, list_from_file):
        """
        Forms GoodInfoList of goods from file data
        :param list_from_file: data from file
        :type list_from_file: list
        :return: Function return False if list_from_file empty
        """

        logging.info("Формирование списка GoodInfoList")

        if len(list_from_file) == 0:
            logging.error("После прочтений из файла получился пустой список")
            return False

        for product in list_from_file:
            product_data = product.split(":")
            
            if len(product_data) != 5:
                logging.error("Следующая строка не была обработана: {product}".format(
                              product=product))
                continue

            if GoodInfo.check_product_data(product_data[0], 
                                           product_data[1], 
                                           product_data[2], 
                                           product_data[3], 
                                           product_data[4]):

                name_product = product_data[0]
                price_product = int(product_data[1])
                product_amount = int(product_data[2])
                product_date =  datetime.strptime(product_data[3], "%Y-%m-%d")
                shelf_life = int(product_data[4])
                
                self.add(GoodInfo(name_product, 
                                  price_product, 
                                  product_amount, 
                                  product_date, 
                                  shelf_life))
            else:
                logging.error("Следующая строка не была обработана: {product}".format(
                              product=product))
            
    def check_date_import_list(self):
        """
        If the expiration in list date has expired, then the product is removed
        :return: GoodInfoList with removing goods
        :rtype: GoodInfoList
        """

        logging.info("Проверка на истечение срока годности")

        list_of_removing_goods = GoodInfoList()

        for good in self.list_with_goods:
            if GoodInfo.check_shell_life_good(good.date_import, good.shelf_life):

                list_of_removing_goods.add(GoodInfo(good.name, 
                                                    good.price, 
                                                    good.amount, 
                                                    good.date_import, 
                                                    good.shelf_life))
                self.remove(good.name)
    
        return list_of_removing_goods
        
    def remove(self, name):
        """
        Remove object with name
        :param name: name good
        :type name: string
        """

        logging.info("Удаление объекта с именем: {name}".format(name=name))

        for good in self.list_with_goods:
            if good.name == name:
                logging.info("Удаленный товар: {good}".format(good=good))
                self.list_with_goods.remove(good)

    def remove_expensive(self):
        """
        Remove object with maximum price
        """

        logging.info("Удаление из списка самого дорогого товара")

        most_expensive = self.get_list_most_expensive()
        max_price = most_expensive[0].price

        for good in self.list_with_goods:
            if good.price == max_price:
                self.list_with_goods.remove(good)

    def get_list_most_expensive(self):
        """
        Get list with most expensive goods
        :return: list with most expensive goods
        :rtype: list
        """

        logging.info("Получение списка с самыми дорогими товарами")

        most_expensive_goods = list()
        max_price = 0

        for good in self.list_with_goods:
            if good.price > max_price:
                max_price = good.price

        for good in self.list_with_goods:
            if good.price == max_price:
                most_expensive_goods.append(good)

        return most_expensive_goods

    def get_list_with_cheap_goods(self):
        """
        Get list with most cheapset goods
        :return: list with most cheapset goods
        :rtype: list
        """

        logging.info("Получение списка с самыми дешевыми товарами")

        most_cheapset = list()
        min_price = 9999

        for good in self.list_with_goods:
            if good.price < min_price:
                min_price = good.price
        
        for good in self.list_with_goods:
            if good.price == min_price:
                most_cheapset.append(good)
        
        return most_cheapset

    def get_list_ending_goods(self):
        """
        Get list with ending goods
        :return: list with enging goods
        :rtype: list
        """
        
        logging.info("Получение списка с заканчивающимися товарами")

        ending_goods = list()

        for good in self.list_with_goods:
            if good.amount < 5:
                ending_goods.append(good)
        
        return ending_goods

    def sort(self, key):
        """
        Sort list with goods by key
        :param key: name field by which need sort
        :type key: string
        :return: sorted list with goods
        :rtype: list
        """

        logging.info("Сортировка по ключу {key}".format(key=key))

        if key == "price":
            sort_list = sorted(
                                self.list_with_goods,
                                key=lambda good: good.price)
            return sort_list
        elif key == "amount":
            sort_list = sorted(
                                self.list_with_goods,
                                key=lambda good: good.amount)
            return sort_list
        elif key == "name":
            sort_list = sorted(
                                self.list_with_goods,
                                key=lambda good: good.name)
            return sort_list
        else:
            raise AttributeError

    def __getitem__(self, name):
        """
        receiving  by []
        :param key: name in list with goods
        :type key: string
        :return: object by key
        :rtype: object good from list with goods if exsits good by
        key, else raise KeyError
        """
        
        logging.info("Получение из GoodInfoList по ключу {key}".format(key=name))

        list_of_goods = GoodInfoList()

        for good in self.list_with_goods:
            if good.name == name:
                list_of_goods.add(GoodInfo(good.name, good.price, good.amount, 
                                           good.date_import, good.shelf_life))
        
        if len(list_of_goods) == 0:
            raise KeyError
        else:
            return list_of_goods

    def get_value_info(self): 
        """ 
        Function get values about products
        :return: Function return dictionary with 
        amount products and mean value
        if list_with_goods is empty function return -1
        :rtype: Return dictionary with key:amount and key:mean and
        :amount=(Number)
        :mean=(float Number)
        """

        if len(self.list_with_goods) == 0:
            return -1

        total_price = 0
        amount_product = 0

        for good in self.list_with_goods:
            total_price += good.price
            amount_product += 1
            
        mean = total_price / amount_product
        
        logging.info("Количество {amount}, средняя цена {mean}".format(
                                                                amount=amount_product,
                                                                mean=mean))


        return {'amount': amount_product, 'mean': mean}
