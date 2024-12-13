# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Customer(Base):
    """description: Table to store customer information"""
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    credit_limit = Column(DECIMAL, nullable=False)
    balance = Column(DECIMAL, nullable=False, default=0.0)


class Order(Base):
    """description: Table to store order information related to customers"""
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    date_shipped = Column(DateTime, nullable=True)
    amount_total = Column(DECIMAL, nullable=False, default=0.0)
    notes = Column(String(500))


class Item(Base):
    """description: Table to store item information related to orders"""
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL, nullable=False)
    amount = Column(DECIMAL, nullable=False, default=0.0)


class Product(Base):
    """description: Table to store product information"""
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    unit_price = Column(DECIMAL, nullable=False)


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    customer1 = Customer(name="Alice Johnson", credit_limit=Decimal('1000.00'), balance=Decimal('500.00'))
    customer2 = Customer(name="Bob Smith", credit_limit=Decimal('1500.00'), balance=Decimal('300.00'))
    customer3 = Customer(name="Charlie Brown", credit_limit=Decimal('2000.00'), balance=Decimal('1700.00'))
    customer4 = Customer(name="Diana Prince", credit_limit=Decimal('2500.00'), balance=Decimal('2300.00'))
    order1 = Order(customer_id=1, date_shipped=None, amount_total=Decimal('200.00'), notes="Delivery pending")
    order2 = Order(customer_id=1, date_shipped=None, amount_total=Decimal('300.00'), notes="Express delivery")
    order3 = Order(customer_id=2, date_shipped=datetime(2023, 1, 20), amount_total=Decimal('150.00'), notes="Delivered")
    order4 = Order(customer_id=3, date_shipped=None, amount_total=Decimal('500.00'), notes="Backordered")
    item1 = Item(order_id=1, product_id=1, quantity=2, unit_price=Decimal('50.00'), amount=Decimal('100.00'))
    item2 = Item(order_id=1, product_id=2, quantity=2, unit_price=Decimal('50.00'), amount=Decimal('100.00'))
    item3 = Item(order_id=2, product_id=3, quantity=3, unit_price=Decimal('20.00'), amount=Decimal('60.00'))
    item4 = Item(order_id=3, product_id=2, quantity=5, unit_price=Decimal('30.00'), amount=Decimal('150.00'))
    product1 = Product(name="Product A", unit_price=Decimal('50.00'))
    product2 = Product(name="Product B", unit_price=Decimal('30.00'))
    product3 = Product(name="Product C", unit_price=Decimal('20.00'))
    product4 = Product(name="Product D", unit_price=Decimal('60.00'))
    
    
    
    session.add_all([customer1, customer2, customer3, customer4, order1, order2, order3, order4, item1, item2, item3, item4, product1, product2, product3, product4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
