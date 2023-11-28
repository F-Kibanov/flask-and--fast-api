"""Задание:

Необходимо создать API для управления списком пользователей. Создайте класс User с полями id, name, email и password.

API должен содержать следующие конечные точки:
— GET /users — возвращает список пользователей.
— GET /users/{id} — возвращает пользователя с указанным идентификатором.
— POST /users — добавляет нового пользователя.
— PUT /users/{id} — обновляет пользователя с указанным идентификатором.
— DELETE /users/{id} — удаляет пользователя с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
Для этого использовать библиотеку Pydantic.
"""

import logging

import pydantic
import uvicorn
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class User(BaseModel):
    user_id: int
    name: str
    email: pydantic.EmailStr = None
    password: str = None
    is_active: Optional[bool] = True


users = []


@app.get('/user/', response_model=list[User])
async def get_all_users():
    return [user for user in users if user.is_active]


@app.get('/user/{user_id}', response_model=User)
async def get_user_by_id(user_id: int):
    user = [user for user in users if user.user_id == user_id][0]
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@app.post('/user/', response_model=User)
async def create_user(user: User):
    if [u for u in users if u.user_id == user.user_id]:
        raise HTTPException(status_code=409, detail='User id already exist')
    users.append(user)
    return user


@app.put('/user/', response_model=User)
async def update_user(user_id: int, user: User):
    for i in range(len(users)):
        if users[i].user_id == user_id:
            users[i] = user
            return user
    raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/', response_model=User)
async def delete_user(user_id: int):
    for i in range(len(users)):
        if users[i].user_id == user_id:
            user = users[i]
            del users[i]
            return user
    raise HTTPException(status_code=404, detail='User not found')


if __name__ == '__main__':
    uvicorn.run('dz_5:app', host='localhost', port=8000, reload=True)
