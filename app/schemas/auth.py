from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, validator


class SignUpSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator('username', 'email', 'password')
    def field_must_be_populated(cls, value):
        if not value:
            raise ValueError('This field must be complete')
        return value

    @validator('email')
    def email_must_be_valid(cls, email):
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise ValueError('The email field is invalid')
        return email
    

class SignInSchema(BaseModel):
    email: EmailStr
    password: str

    @validator('email', 'password')
    def field_must_be_populated(cls, value):
        if not value:
            raise ValueError('This field must be complete')
        return value

    @validator('email')
    def email_must_be_valid(cls, email):
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise ValueError('The email field is invalid')
        return email
