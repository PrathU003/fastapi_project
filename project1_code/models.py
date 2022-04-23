from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.orm import relationship


from database import Base


class Service(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String)
    category=Column(String(20))
    price = Column(Integer)
    
    #category_id = Column(Integer, ForeignKey("category.id"))
    #category = relationship("Category", back_populates="service")

'''
class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    service = relationship("Service", back_populates="category")
'''


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, index = True)
    email = Column(String, unique = True, index = True)
    username = Column(String, unique = True, index = True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    mobile = Column(Integer)
