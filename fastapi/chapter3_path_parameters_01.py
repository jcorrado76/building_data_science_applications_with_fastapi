from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{type}/{user_id}")
async def get_user(type: str, user_id: int):
    return {"user_id": str(user_id), "type": type}
