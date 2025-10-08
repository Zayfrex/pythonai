#trying out pydantic
# pydantic is a data validation and settings management library for Python, based on Python type annotations.
# It allows you to define data models with type hints, and it automatically validates and parses the data according to the specified types.



#!!!!! learn json integration with pydantic to make the app communicate with other services
from pydantic import BaseModel, EmailStr ,field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")#custom validator to ensure account_id is positive
    def valid_account_id(cls, v):
        if v <= 0:
            raise ValueError(f"account_id must be positive: {v}")
        return v

user = User(name="Jack",email="jack@gmail.com",account_id=123)  #note strings that are valid int can be trasnformed automatically

print(user)