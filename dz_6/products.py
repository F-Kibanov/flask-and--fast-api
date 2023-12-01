from fastapi import APIRouter, Path

from db import products, database
from models import Product, ProductIn

router = APIRouter()


@router.get('/products/', response_model=list[Product])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)


@router.get('/products/{product_id}', response_model=Product)
async def get_product(product_id: int = Path(..., gt=0, title='ID', desc='Product ID')):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@router.post('/products/', response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(title=product.title, desc=product.desc, price=product.price)
    last_record_id = await database.execute(query)
    return Product(id=last_record_id, **product.model_dump())


@router.put('/products/{product_id}/', response_model=Product)
async def update_product(new_product: ProductIn, product_id: int = Path(..., ge=0, title='ID', desc='Product ID')):
    query = products.update().where(products.c.id == product_id).values(title=new_product.title, desc=new_product.desc,
                                                                        price=new_product.price)
    await database.execute(query)
    return Product(id=product_id, **new_product.model_dump())


@router.delete('/products/{product_id}/', response_model=dict)
async def delete_product(product_id: int = Path(..., ge=0, title='ID', desc='Product ID')):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': "Product deleted"}
