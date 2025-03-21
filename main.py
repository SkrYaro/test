import schemas
from fastapi import FastAPI

app = FastAPI()

users_list = []


@app.get("/users")
def get_users():
    return users_list


@app.post("/create/user")
def create_user(user: schemas.User):
    users_list.append(user)
    return user


if __name__ == "__main__":
    import os

    os.system("uvicorn main:app --reload")
