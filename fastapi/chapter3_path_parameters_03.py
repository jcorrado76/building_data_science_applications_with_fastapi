from enum import Enum
from fastapi import FastAPI


class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"


app = FastAPI()


@app.get("/users/{type}/{user_id}")
async def get_user(type: UserType, user_id: int):
    return {"user_id": str(user_id), "type": type}
