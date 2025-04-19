from fastapi import FastAPI
from models import User

app = FastAPI()

users = []

@app.get('/users/')
def get_users():
    return users

@app.post('/user/update/')
def update_user(user: User):
    new_user = {
        "email": user.email,
        "password": user.password
    }
    users.append(new_user)
    return new_user
