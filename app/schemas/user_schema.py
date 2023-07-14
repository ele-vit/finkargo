from pydantic import BaseModel, field_validator

from app.schemas.auth import SignUpSchema


class GetUserSchema(BaseModel):
    id: int

    @field_validator('id')
    def field_must_be_populated(cls, value):
        if not value:
            raise ValueError('This field must be complete')
        return value


class UpdateUserSchema(SignUpSchema):
    id: int

    @field_validator('id')
    def field_must_be_populated(cls, value):
        if not value:
            raise ValueError('This field must be complete')
        return value
