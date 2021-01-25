from math import sqrt
from datetime import datetime, timedelta
from operator import attrgetter
import logging 
from db_models import Good, Provider, Delivery, Shelf
from sqlalchemy import func

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

    def __init__(self, name, price, amount, date_import, shelf_life, manufacture):
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
        self.date_manufacture = manufacture

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

    def __repr__(self):
        """
        Function make string for represents develop good
        :return: string represents good
        :rtype: string
        """
        return  ("GoodInfo('{name}', '{price}', '{amount}',"
                 "'{date}', '{shelf}', '{date}'),\n").format(
                name=self.name,
                price=self.price,
                amount=self.amount,
                shelf=self.shelf_life,
                date=self.date_import
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
        
        price = str(price)
        amount = str(amount)
        shelf_life = str(shelf_life)

        if name == "":
            return False

        if (not price.isdigit() and not amount.isdigit() and 
            not shelf_life.isdigit()):
            return False
        
        shelf_life = int(shelf_life)
        price = int(price)
        amount = int(amount)

        if (shelf_life > 0 and price > 0 and 
            amount >= 0 and GoodInfo.__check_date(date_import)):
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

        if date_import > today:
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
        good_date =  datetime.strptime(good_date, "%Y-%m-%d")
        ending_shelf_life = good_date + shelf_life
        today = datetime.today()

        if today < ending_shelf_life:
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
    
    def __repr__(self):
        """
        Function make string with represents GoodInfoList
        :return: string represents GoodInfo
        :rtype: string
        """

        list_with_goods_strings = ""

        for elem in self.list_with_goods:
            list_with_goods_strings += repr(elem)

        return list_with_goods_strings

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
        Add GoodInfo in GoodInfoList and Database
        :param good_info: object GoodInfo
        :type good_info: GoodInfo
        :return: function nothing return
        """

        if (GoodInfo.check_product_data(good_info.name, 
                                       good_info.price, 
                                       good_info.amount, 
                                       good_info.date_import, 
                                       good_info.shelf_life) and
            
            GoodInfo.check_shell_life_good(good_info.date_manufacture, 
                                           good_info.shelf_life)):

            
            self.list_with_goods.append(good_info)

            return True
        else:
            logging.error("Следующая строка не была обработана: {good_info}".format(
                                                                   good_info=good_info))
            return False

    def get_from_file(self, list_from_file):
        """
        Forms GoodInfoList of goods from file data
        :param list_from_file: data from file
        :type list_from_file: list
        :return: Function return False if list_from_file empty, else True
        """

        logging.info("Формирование списка GoodInfoList")

        if len(list_from_file) == 0:
            logging.error("После прочтений из файла получился пустой список")
            return False

        for product in list_from_file:
            product_data = product.split(":")
            
            if len(product_data) != 5:
                logging.error("Следующая строка не была обработана1: {product}".format(
                              product=product))
                continue

            name_product = product_data[0]
            price_product = product_data[1]
            product_amount = product_data[2]
            product_date =  product_data[3]
            shelf_life = product_data[4]
            date_manufacture = product_data[3]

            self.add(GoodInfo(name_product, 
                              price_product, 
                              product_amount, 
                              product_date, 
                              shelf_life, 
                              date_manufacture))
        
        return True
            
    def check_date_manafucture_list(self):
        """
        If the expiration in list date has expired, then the product is removed
        :return: GoodInfoList with removing goods
        :rtype: GoodInfoList
        """

        logging.info("Проверка на истечение срока годности")

        list_of_removing_goods = GoodInfoList()

        for good in self.list_with_goods:
            if GoodInfo.check_shell_life_good(good.date_manufacture, 
                                              good.shelf_life):

                list_of_removing_goods.add(GoodInfo(good.name, 
                                                    good.price, 
                                                    good.amount, 
                                                    good.date_import, 
                                                    good.shelf_life,
                                                    good.date_manufacture))
                self.remove(good.name)
    
        return list_of_removing_goods
        
    def remove(self, name):
        """
        Remove object by name
        :param name: name good
        :type name: string
        :return True if good was remove and False else
        :rtype: bool
        """

        logging.info("Удаление объекта с именем: {name}".format(name=name))

        for good in self.list_with_goods:
            if good.name == name:
                logging.info("Удаленный товар: {good}".format(good=good))
                self.list_with_goods.remove(good)

                return True
        
        return False

    def remove_expensive(self):
        """
        Remove object with maximum price
        :return: return name expensive good
        """

        logging.info("Удаление из списка самого дорогого товара")
        print("Удаление из списка самого дорогого товара")

        most_expensive = self.get_list_most_expensive()
        
        if len(most_expensive) > 0:
            expensive_good = most_expensive[0]

            for good in self.list_with_goods:
                if good.price == expensive_good.price:
                    self.list_with_goods.remove(good)
                    return good.name

    def get_list_most_expensive(self):
        """
        Get list with most expensive goods
        :return: list with most expensive goods
        :rtype: list
        """

        logging.info("Получение списка с самыми дорогими товарами")

        most_expensive_goods = GoodInfoList()
        max_price = 0

        for good in self.list_with_goods:
            if good.price > max_price:
                max_price = good.price

        for good in self.list_with_goods:
            if good.price == max_price:
                most_expensive_goods.add(good)

        return most_expensive_goods
    
    def __eq__(self, other):
        if isinstance(other, GoodInfoList):
            for object_self, object_other in zip(self.list_with_goods, other.list_with_goods):
                if (object_self.name == object_other.name and
                    object_self.price == object_other.price and
                    object_self.amount == object_other.amount and
                    object_self.shelf_life == object_other.shelf_life and
                    object_self.date_import == object_other.date_import and
                    object_self.date_manufacture == object_other.date_manufacture):
                    
                    return True
                else:
                    return False


    def get_list_with_cheap_goods(self):
        """
        Get list with most cheapset goods
        :return: list with most cheapset goods
        :rtype: list
        """

        logging.info("Получение списка с самыми дешевыми товарами")

        most_cheapset = GoodInfoList()
        min_price = 9999

        for good in self.list_with_goods:
            if good.price < min_price:
                min_price = good.price
        
        for good in self.list_with_goods:
            if good.price == min_price:
                most_cheapset.add(good)
        
        return most_cheapset

    def get_list_ending_goods(self):
        """
        Get list with ending goods
        :return: list with enging goods
        :rtype: list
        """
        
        logging.info("Получение списка с заканчивающимися товарами")

        ending_goods = GoodInfoList()

        for good in self.list_with_goods:
            if good.amount < 5:
                ending_goods.add(good)
        
        return ending_goods

    def sort(self, key):
        """
        Sort list with goods by key
        :param key: name field by which need sort
        :type key: string
        :return: sorted list with goods
        :rtype: GoodInfoList
        """

        logging.info("Сортировка по ключу {key}".format(key=key))
        sort_list_by_key = GoodInfoList()

        if key == "price":
            sort_list = sorted(
                                self.list_with_goods,
                                key=lambda good: good.price)

            for good in sort_list:
                sort_list_by_key.add(good)

            return sort_list_by_key
        elif key == "amount":
            sort_list = sorted(
                                self.list_with_goods,
                                key=lambda good: good.amount)

            for good in sort_list:
                sort_list_by_key.add(good)

            return sort_list_by_key
        elif key == "name":
            sort_list = sorted(
                                self.list_with_goods,
                                key=lambda good: good.name)

            for good in sort_list:
                sort_list_by_key.add(good)
            
            return sort_list_by_key
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
        
        name = str(name)
        logging.info("Получение из GoodInfoList по ключу {key}".format(key=name))

        if not name.isdigit():
            list_of_goods = GoodInfoList()

            for good in self.list_with_goods:
                if good.name == name:
                    list_of_goods.add(GoodInfo(good.name, 
                                            good.price, 
                                            good.amount, 
                                            good.date_import, 
                                            good.shelf_life,
                                            good.date_manufacture))
            
            if len(list_of_goods) == 0:
                raise KeyError
            else:
                return list_of_goods
        else:
            name = int(name)
            return self.list_with_goods[name]

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
            amount_product += good.amount
            
        mean = total_price / len(self.list_with_goods)
        
        logging.info("Количество {amount}, средняя цена {mean}".format(
                                                                amount=amount_product,
                                                                mean=mean))


        return {'amount': amount_product, 'mean': mean}

    def __iter__(self):
        return iter(self.list_with_goods)

    def product_buy(self, name, amount):
        """
        Function allows you to buy a product
        :param name: name good
        :type name: string
        :param amount: amount goods
        :type amount: integer
        :return: Function return False if total amount goods less
        then amount, function return false if goood end, function
        return earnings else
        :rtype: bool if false, else integer
        """
        
        goods_find_list = GoodInfoList()

        for good in self.list_with_goods:
            if good.name == name:
                goods_find_list.add(good)

        if len(goods_find_list) == 0:
            logging.info("Нет товара с именем {name}".format(name=name))
            print("Нет товара с именем {name}".format(name=name))
            return False

        availability = any(good.amount > 0 for good in goods_find_list)

        if availability is False:
            logging.info("Товар закончился ({product}) "
                        "(выручка - None)".format(product=name))
            print("Товар закончился ({product}) "
                        "(выручка - None)".format(product=name))
            return False
        

        total_amount = sum([good.amount for good in goods_find_list])

        if len(goods_find_list) == 1 and total_amount < amount:
            logging.info("Количество запрашиваемых товаров больше "
                        "чем имеется в наличии (выручка - None)")
            print("Количество запрашиваемых товаров больше "
                        "чем имеется в наличии (выручка - None)")
            return False
        
        if len(goods_find_list) > 1:
            
            min_date = min([good.date_manufacture for good in goods_find_list
                            if good.amount > amount
                            ])
            earnings = 0

            for good in goods_find_list:
                if good.date_manufacture == min_date:
                    good.amount -= amount
                    earnings = amount * good.price
            
            return earnings
        
        elif len(goods_find_list) == 1:
            good = goods_find_list.list_with_goods[0]
            earnings = amount * good.price
            
            return earnings
