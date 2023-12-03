from fastapi import FastAPI
import uvicorn


from db import database
import users
import products
import orders

app = FastAPI()
app.include_router(users.router, tags=['users'])
app.include_router(products.router, tags=['products'])
app.include_router(orders.router, tags=['orders'])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host="localhost",
        port=8000,
        reload=True
    )
