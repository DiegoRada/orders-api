from config.database import Base
from sqlalchemy import Column, Integer, String, Float


class Customer(Base):

    __tablename__ = "customers"

    customerid = Column(Integer, primary_key=True)
    customername = Column(String)
    contactname = Column(String)
    address = Column(String)
    city = Column(String)
    postalcode = Column(String)
    country = Column(String)
