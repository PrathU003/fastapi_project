from typing import Optional
from unicodedata import category
from pydantic import BaseModel , Field , constr

'''
class Category(BaseModel):
    name: constr(min_length=2, max_length=50)


class ListCategory(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True
'''

class Services(BaseModel):
    name: str
    description: Optional[str]
    category :str
    price : int


class CreateUser(BaseModel):
    username : str
    email : Optional[str]
    first_name : str
    last_name :str
    password : str
    mobile : int

'''
class Product(Services):
    category_id: int
    class Config:
        orm_mode = True

class ProductListing(Services):
    category: ListCategory
    class Config:
        orm_mode = True
'''