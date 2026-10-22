from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: str
    role: str = "user"  # Default role is "user"
    
class UserLogin(BaseModel):
    username: str
    password: str