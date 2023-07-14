from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, validator
from app.schemas.auth import SignUpSchema


class GetUserSchema(BaseModel):
    id: int

    @validator('id')
    def field_must_be_populated(cls, value):
        if not value:
            raise ValueError('This field must be complete')
        return value


class UpdateUserSchema(SignUpSchema):
    id: int

    @validator('id')
    def field_must_be_populated(cls, value):
        if not value:
            raise ValueError('This field must be complete')
        return value
