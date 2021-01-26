from sqlalchemy import create_engine, String,  \
    MetaData, Table, Column, Integer, ForeignKey, Date, insert
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship

Base = declarative_base()


class Good(Base):
    """
    Good represents table 
    goods in database
    """
    
    __tablename__ = 'goods'

    id = Column('id', Integer, primary_key=True)
    
    name = Column('name', String)
    
    amount = Column('amount', Integer)

    price = Column('price', Integer)

    id_provider = Column('id_provider', 
                         Integer, 
                         ForeignKey('providers.id',
                                     ondelete="CASCADE",
                                     onupdate="CASCADE"))
    
    id_shelf = Column('id_shelf', 
                        Integer, 
                        ForeignKey('shelfs_life.id',
                                    ondelete="CASCADE",
                                    onupdate="CASCADE"))

    provider = relationship("Provider", back_populates="good")
    shelf = relationship("Shelf", back_populates="good")

class Provider(Base):
    """
    Provider represents table 
    providers in database
    """

    __tablename__ = 'providers'
    
    id = Column('id', Integer, primary_key=True)

    name = Column('name', String)

    good = relationship("Good", back_populates="provider")


class Delivery(Base):
    """
    Delivery represents table 
    dates_delivery in database
    """

    __tablename__ = 'dates_delivery'

    id = Column('id', Integer, primary_key=True)

    date_delivery = Column('date_delivery', Date)

    shelf = relationship("Shelf", back_populates="delivery")
    

class Shelf(Base):
    """
    Shelf represents table 
    shelfs_life in database
    """

    __tablename__ = "shelfs_life"

    id = Column('id', Integer, primary_key=True)
    
    name = Column('name', String)

    shelf_life = Column('shelf_life', Integer)


    id_delivery = Column('id_delivery', 
                        Integer, 
                        ForeignKey('dates_delivery.id',
                                    ondelete="CASCADE",
                                    onupdate="CASCADE"))
    
    delivery = relationship("Delivery", back_populates="shelf")
    
    good = relationship("Good", back_populates="shelf")

    
