from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)



class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    total_price = Column(Float)
    status = Column(String, default="Pending")  # Статус заказа

    client = relationship("Client", back_populates="orders")
    products = relationship("OrderProduct", back_populates="order")


class OrderProduct(Base):
    __tablename__ = 'order_products'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String)
    product_name = Column(String)
    quantity = Column(Integer)
    customer_name = Column(String )

    order = relationship("Order", back_populates="products")
    product = relationship("Product")
