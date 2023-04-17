from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2019-05-02 12:22",
    "friends": [1, 2, "3"],
}

user = User(**external_data)
print(user.id)
print(user.friends)
print(user.dict())

try:
    User(signup_ts='broken', friends=[1, 2, 'Not a number'])
except ValidationError as e:
    print(e)