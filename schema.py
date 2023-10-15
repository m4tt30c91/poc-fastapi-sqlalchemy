from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    surname: str
    
class UserRequest(UserBase):
    pass

class UserResponse(UserBase):
    id: int