from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    name = 'Jane Doe'

user = User(id='123')
user_x = User(id=123.45, name='Jane Doe')

assert user.id == 123
assert user_x.id == 123
assert isinstance(user_x.id, int)
assert user.name == 'Jane Doe'
print(user_x.__fields_set__)
print(user_x.dict())
print(dict(user_x))
print(user_x.json())
print(user_x.copy())
print(user_x.schema())
print(user_x.schema_json())
print(User.schema())

class Foo(BaseModel):
    count: int
    size: Optional[float] = None

class Bar(BaseModel):
    apple = 'x'
    banana = 'y'

class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]

m = Spam(foo={'count': 4}, bars=[{'apple': 'x1', 'banana': 'y1'}])
print(m)

