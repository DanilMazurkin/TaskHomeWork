from math import sqrt
from dateutil.parser import parse
from datetime import datetime, timedelta
from operator import attrgetter
from db_worker import DB_Worker
import logging 
from db_models import Good, Provider, Delivery, Shelf
from sqlalchemy import func, and_


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
        self.database = DB_Worker()

    def remove_expensive(self):
        """
        Remove most expensive good from 
        table goods in database
        """
        self.database.remove_goods_with_max_price()
    
    def check_date_manafucture_list(self):
        """
        If the expiration in list date has expired, then the product is removed
        :return: GoodInfoList with removing goods
        :rtype: GoodInfoList
        """

        logging.info("Проверка на истечение срока годности")
        list_goods = self.database.get_list_by_date_and_shelf()

        for good, shelf, delivery in list_goods:
            date_manufacture = str(delivery.date_delivery)

            if DB_Worker.check_shell_life_good(date_manufacture, 
                                              shelf.shelf_life):
                self.database.remove(good.name)
    
    def remove_last(self):
        """
        Remove last good from goods
        from table goods in database
        """
        self.database.remove_last()
    
    def get_std(self):
        """
        Calculate standart deviation
        by price
        :return: standart deviation
        :rtype: Number 
        """

        price_goods = self.database.get_sort_goods_by_price()
        
        n = self.database.get_count_goods()

        values = self.get_value_info()
        mean = values['mean']

        deviations = [(good.price - mean) ** 2 for good in price_goods]
        variance = sum(deviations) / n
        
        return sqrt(variance)

    def get_list_ending_goods(self):
        """
        Get list where amount less five
        :return: goods from database
        :rtype: list Query 
        """
        goods = self.database.get_goods_ending()

        return goods
    
    def get_list_most_expensive(self):
        """
        Get list with most 
        expensive goods
        :return: Query list with goods expensive
        :rtype: Query list
        """
        max_price = self.database.get_max_price()

        goods_expensive = self.database.get_goods_by_price(max_price)

        return goods_expensive

    def get_list_with_cheap_goods(self):
        """
        Get list with cheap goods
        :return: Query list with cheap goods
        :rtype: Query list
        """

        min_price = self.database.get_min_price()
        cheaps_goods = self.database.get_goods_by_price(min_price)
        
        return cheaps_goods
    
    def sort(self, name):
        """
        Sort list with goods by key
        :param key: name field by which need sort
        :type key: string
        :return: sorted list with goods
        :rtype: Query list
        """

        if name == "price":
            order_by_price = self.database.get_sort_goods_by_price()            
            return order_by_price
        
        elif name == "amount":
            order_by_amount = self.database.get_sort_goods_by_amount()

            return order_by_amount

        elif name == "name":
            order_by_name = self.database.get_sort_goods_by_name()
            return order_by_name

        else:
            raise AttributeError
    
    def get_value_info(self):
        """ 
        Function get values about products
        :return: Function return dictionary with 
        amount products and mean value
        if column good price is empty 
        function return -1
        :rtype: Return dictionary with key:amount and key:mean and
        :amount=(Number)
        :mean=(float Number)
        """
        
        count = self.database.get_count_goods()
        
        if count == 0:
            return -1

        mean = self.database.get_average_goods()

        return {'amount': count, 'mean': mean}        

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

        count_product_by_name = self.database.\
                                    get_count_good_by_name(name)
        
        if count_product_by_name == 0:
            logging.info("Нет товара с именем {name}".format(name=name))
            print("Нет товара с именем {name}".format(name=name))
            return False

        goods_find_list = self.database.get_list_by_name(name)
        
        availability = any(good.amount > 0 for good in goods_find_list)

        if availability is False:
            logging.info("Товар закончился ({product}) "
                        "(выручка - None)".format(product=name))
            print("Товар закончился ({product}) "
                        "(выручка - None)".format(product=name))
            return False
        
        total_amount = sum([good.amount for good in goods_find_list])

        if count_product_by_name == 1 and total_amount < amount:
            logging.info("Количество запрашиваемых товаров больше "
                        "чем имеется в наличии (выручка - None)")
            print("Количество запрашиваемых товаров больше "
                        "чем имеется в наличии (выручка - None)")
            return False
        
        if count_product_by_name > 1:
            
            list_data = self.database.get_list_by_date_and_shelf()

            min_date = min([delivery.date_delivery 
                            for good, shelf, delivery in list_data
                            if good.amount > amount
                            ])
            earnings = 0

            for good, shelf, delivery in list_data:
                if delivery.date_delivery == min_date:
                    good.amount -= amount
                    earnings = amount * good.price
                    self.database.update_good(name, amount)

            return earnings
        
        elif count_product_by_name == 1:
            good = goods_find_list[0]
            earnings = amount * good.price
            self.database.update_good(name, amount)

            return earnings
    
    def get_from_file(self, list_from_file):
        """
        Fill database tables of goods from file data
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

            db_worker = DB_Worker()

            db_worker.add(GoodInfo(name_product, 
                              price_product, 
                              product_amount, 
                              product_date, 
                              shelf_life, 
                              date_manufacture))
        
        return True

    def remove(self, name):
        self.database.remove_by_name(name)