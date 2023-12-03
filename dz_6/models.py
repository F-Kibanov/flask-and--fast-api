from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import Literal


class ProductIn(BaseModel):
    title: str = Field(max_length=128)
    desc: str = Field(max_length=512)
    price: float


class Product(ProductIn):
    id: int


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(max_length=80)
    email: EmailStr
    password: str


class User(UserIn):
    id: int


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    order_date: date
    status: Literal['cancelled', 'in progress', 'done']


class Order(BaseModel):
    id: int
    user: User
    product: Product
    order_date: date
    status: Literal['cancelled', 'in progress', 'done']
