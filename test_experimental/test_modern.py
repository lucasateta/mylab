from datetime import datetime
from pydantic import BaseModel
from typing import Union
from fastapi import FastAPI, BackgroundTasks, Depends
from typing import Optional, Annotated

app = FastAPI()

def main(user_id: str):
    return user_id

class User(BaseModel):
    id: int
    name: str
    joined: Optional[datetime]


def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)

def get_query(background_tasks: BackgroundTasks, q: Optional[str] = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q

def write_notification(email: str, message = ""):
    with open("log.txt", mode="a") as email_file:
        content = f"notification for {email}: {message}\n"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_task: BackgroundTasks, q: Annotated[str, Depends(get_query)]):
    message = f"message to {email}\n"

    background_task.add_task(write_log, message)
    return {"message": "notification sent in the background."}

@app.get("/")
async def read_root():
    return {"Hello": "World1"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q.title()}

@app.put("/items/{item_id}")
def save_item(item_id: int, item: User):
    return {"item_id": item_id, "item_name": item.name, "date": item.joined}
