import os
from sqlalchemy import create_engine
from sqlalchemy import String, MetaData, Table, \
                        Column, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from db_models import Good, Provider, Delivery, \
                      Shelf, Base
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import Session
from math import sqrt
import logging 
from sqlalchemy import func, text, update, and_
from datetime import datetime, timedelta
from dateutil.parser import parse


class DB_Worker:
    """
    Represent Database work

    Attributes:
    DB_NAME (string): Database name
    HOST_NAME (string): Hostname database
    USER_NAME (string): Username for user database
    PASS (string): Password for database
    metadata (metadata): metadata for database
    engine (engine): engine for database
    session (session): session for database
    database (Database): Database object
    session (Session): Session object

    Methods:
    __init__()
    set_tables()
    __get_engine()
    get_session()
    __init__()
    remove_expensive()
    remove_last()
    get_std()
    remove()
    get_list_ending_goods()
    get_list_most_expensive()
    get_list_with_cheap_goods()
    sort(name)
    get_value_info()
    product_buy(name, amount)
    add(good_info)
    get_from_file()
    add_record_shelf(shelf_life)
    add_record_delivery(date_delivery)
    add_record_provider(name)
    add_record_good(name, amount, price, 
                    id_provider, id_date, id_shelf)
    get_id_provider_by_name(name)
    get_id_delivery_by_date(date_delivery):
    get_id_shelf(shelf_life)
    get_max_price()
    get_min_price()
    update_good()
    get_list_by_date_and_shelf()
    """

    def __init__(self):
        """
        Initialize DB_NAME, HOST_NAME
        USER_NAME, PASS, metadata,
        engine, session
        """
        
        self.DB_NAME = 'TestAndLearning'
        self.HOST_NAME = '127.0.0.1'
        self.USER_NAME = 'postgres'
        self.PASS = os.environ.get('CONPASS')
        self.metadata = None
        self.engine = self.__get_engine()
        self.session = Session(bind=self.engine)
        self.set_tables()
        
    def set_tables(self):
        """
        Create tables: goods, shelfs, delivery, 
        providers
        """   
        
        Base.metadata.create_all(self.engine)

    def get_session(self):
        """
        Function return session
        """

        return self.session

    def __get_engine(self):
        """
        Return engine for database
        :return: return engine for database
        :rtype: engine
        """

        self.engine = create_engine('postgresql+psycopg2://{user}:{pwd}@{host}/{dbname}'
                       .format(dbname=self.DB_NAME,
                               host=self.HOST_NAME,
                               user=self.USER_NAME,
                               pwd=self.PASS
                               ))

        self.engine.connect()

        self.metadata = MetaData(bind=self.engine)
        self.metadata.reflect()

        return self.engine

    def add(self, good_info):
        """"
        Add GoodInfo in Database table goods
        :param good_info: object GoodInfo
        :type good_info: GoodInfo
        :return: function nothing return
        """

        if (DB_Worker.__check_product_data(good_info.name, 
                                       good_info.price, 
                                       good_info.amount, 
                                       good_info.date_import, 
                                       good_info.shelf_life) and
            
            DB_Worker.__check_shell_life_good(good_info.date_manufacture, 
                                           good_info.shelf_life)):

            self.add_record_delivery(good_info.date_import)
            self.add_record_provider("Default")
            
            id_date_delivery = self.get_id_delivery_by_date(
                                                    good_info.date_import)

            self.add_record_shelf(good_info.name, 
                                good_info.shelf_life,
                                id_date_delivery
                            )
                        

            id_shelf = self.get_id_shelf(good_info.shelf_life)
            id_provider = self.get_id_provider_by_name("Default")          

            self.add_record_good(good_info.name,
                                     good_info.amount,
                                     good_info.price,
                                     id_provider, 
                                     id_shelf)
            
            return True
        else:
            logging.error("Следующая строка не была обработана: {good_info}".format(
                                                                   good_info=good_info))
            return False

    def add_record_shelf(self, name, shelf_life, id_delivery):
        """
        Add shelf life in table
        shelfs life
        :param shelf_life: shelf_life good
        :type shelf_life: Integer
        """
        shelf = Shelf(
            name=name,
            shelf_life=shelf_life,
            id_delivery=id_delivery
        )

        self.session.add(shelf)
        self.session.commit()

    def add_record_delivery(self, date_delivery):
        """
        Add record delivery in table
        delivery dates       
        :param date_delivery: date_delivery good
        :type date_delivery: Date
        """

        count_date = self.session.query(Delivery).filter(
                                    Delivery.date_delivery == date_delivery
                                ).\
                                count()
        
        if count_date == 0:
            delivery = Delivery(
                date_delivery=date_delivery
            )

            self.session.add(delivery)
            self.session.commit()

    def add_record_provider(self, name):
        """
        Add record provider in table
        providers    
        :param name: name good
        :type name: String
        """

        count_provider = self.session.query(Provider).filter(
                                        Provider.name == name).\
                                        count()
        if count_provider == 0:
            
            provider = Provider(
                name=name
            )

            self.session.add(provider)
            self.session.commit()
    
    def add_record_good(self, name, amount, price, 
                        id_provider, id_shelf):
        """
        Add record good in table
        goods    
        :param name: name good
        :type name: String
        :param amount: amount good
        :type amount: Integer
        :param price: price good
        :type price: Integer
        :param id_provider: id provider in table
        :type id_provider: integer
        :param id_date: id date in table
        :type id_date: Date
        :param id_shelf: id shelf in table
        :type id_shelf: Integer
        """
        
        good = Good(
            name=name,
            amount=amount,
            price=price,
            id_provider=id_provider,
            id_shelf=id_shelf
        )

        self.session.add(good)
        self.session.commit()

    def get_id_provider_by_name(self, name):
        """
        Function return id by name
        :return: id provider
        :return: Integer
        """

        providers = self.session.query(Provider).filter(
                                                Provider.name == name
        )
        
        id = None

        for provider in providers:
            id = provider.id
            break
            
        return id
    
    def get_id_delivery_by_date(self, date_delivery):
        """
        Function return id by date
        :return: id date_delivery
        :return: Integer
        """

        dates = self.session.query(Delivery).filter(
                                        Delivery.date_delivery == date_delivery
        )

        id = None

        for date in dates:
            id = date.id
            break
        
        return id
    
    def get_id_shelf(self, shelf_life):
        """
        Function return id by shelf_life
        :return: id shelf_life
        :return: Integer
        """

        shelfs = self.session.query(Shelf).filter(
                                    Shelf.shelf_life == shelf_life
        )

        id = None

        for shelf in shelfs:
            id = shelf.id
            break

        return id

    @staticmethod
    def __check_shell_life_good(good_date, shelf_life):
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
        good_date =  parse(good_date)
        ending_shelf_life = good_date + shelf_life
        today = datetime.today()

        if today < ending_shelf_life:
            return True
        else:
            return False
    
    @staticmethod
    def __check_product_data(name, price, amount, date_import, shelf_life):
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
            amount >= 0 and DB_Worker.__check_date(date_import)):
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

    def get_max_price(self):
        """
        Return max price goods
        """

        max_price = self.session.query(func.max(Good.price)).scalar()

        return max_price

    def get_min_price(self):
        """
        Return max price goods
        """

        min_price = self.session.query(func.max(Good.price)).scalar()

        return min_price

    def update_good(self, name, amount):
        """
        Update good in database
        :param name: name good
        :param amount: amount good
        """

        self.session.query(Good).\
                        filter(Good.name == name).\
                        update({"amount": (Good.amount - amount)})
        self.session.commit()

    def get_list_by_date_and_shelf(self):
        """
        Return list by date and shelf
        """

        list_data = self.session.query(Good, Shelf, Delivery)\
                                 .filter(and_(
                                    Good.id_shelf == Shelf.id,
                                    Delivery.id == Shelf.id_delivery
                                ))
        
        return list_data
    
    def get_list_by_name(self, name):
        """
        Return list by name
        """

        goods_find_list = self.session.query(Good).\
                                            filter(name == Good.name)

        return goods_find_list
    
    def get_count_good_by_name(self, name):
        """
        Get good count by name
        """

        goods_find_list_count = self.session.query(Good).\
                                            filter(name == Good.name).\
                                            count()

        return goods_find_list_count
    
    def get_count_goods(self):
        """
        Return count good
        """

        count = self.session.query(func.count(Good.id)).scalar()

        return count    
    
    def get_average_goods(self):
        """
        Get average goods
        """

        average = self.session.query(func.avg(Good.price)).scalar()

        return average
    
    def get_sort_goods_by_name(self):
        """
        Return sort goods by name
        """

        goods_order_by_name = self.session.query(Good).\
                                        order_by(Good.name)

        return goods_order_by_name
    
    def get_sort_goods_by_amount(self):
        """
        Return sort goods by amount
        """

        goods_order_by_amount = self.session.query(Good).\
                                    order_by(Good.amount)
        
        return goods_order_by_amount
    
    def get_sort_goods_by_price(self):
        """
        Return sort goods by price
        """

        goods_price_by_price = self.session.query(Good).\
                                            order_by(Good.price)

        return goods_price_by_price                       
    
    def get_good_with_max_price(self):
        """
        Return max price from goods
        """
        
        max_price = self.session.query(func.max(Good.price)).scalar()

        return max_price
    
    def get_goods_by_price(self, price):
        """
        Return goods by price
        :param price: price good
        :type price: Integer
        :return: good filter by price
        """

        price_goods = self.session.query(Good).filter(
                                                Good.price == price)

        return price_goods

    def remove_goods_with_max_price(self):
        """
        Return goods with max price
        """

        max_price = self.get_good_with_max_price()
        
        goods = self.session.query(Good).filter(
                                        Good.price == max_price).\
                                delete(synchronize_session='evaluate')
        self.session.commit()

        return goods

    def remove_last(self):
        """
        Remove last in database
        """
        count_goods = self.get_count_goods()
        
        self.session.query(Good).filter(Good.id == count_goods).\
                    delete(synchronize_session='evaluate')            
        self.session.commit()
    
    def get_goods_ending(self):
        """
        Return goods ending
        :return goods: goods query with 
        ending goods
        :type goods: Query
        """

        goods = self.session.query(Good).filter(Good.amount < 5)

        return goods

    def remove_by_name(self, name):
        """
        Remove good by name
        """
        
        self.session.query(Good).filter(Good.name == name).\
                delete(synchronize_session='evaluate')
        self.session.commit()