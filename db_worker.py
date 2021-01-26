import os
from sqlalchemy import create_engine, String,  \
    MetaData, Table, Column, Integer, ForeignKey, Date, update, insert
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from db_models import Good, Provider, Delivery, \
                      Shelf, Base
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import Session


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

    Methods:
    __init__()
    set_tables()
    __get_engine()
    get_session()

    """
    def __init__(self):
        """
        Initialize DB_NAME, HOST_NAME
        USER_NAME, PASS, metadata,
        engine, session
        """
        
        self.DB_NAME = 'learn_db_test'
        self.HOST_NAME = '127.0.0.1'
        self.USER_NAME = 'postgres'
        self.PASS = 'ohshitbegi2019'
        self.metadata = None
        self.engine = self.__get_engine()
        self.session = Session(bind=self.engine)

    def set_tables(self):
        """
        Create tables: goods, shelfs, delivery, 
        providers
        """   
        
        Base.metadata.create_all(self.engine)

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
    
    def get_session(self):
        """
        Return session for database
        :return: return session
        :rtype: Session
        """

        return self.session

   
    

