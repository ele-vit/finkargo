from pydantic import BaseModel, EmailStr, field_validator


class SignUpSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator('username', 'email', 'password')
    def field_must_be_populated(cls, value):
        if not value:
            raise ValueError('This field must be complete')
        return value

    @field_validator('email')
    def email_must_be_valid(cls, email):
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise ValueError('The email field is invalid')
        return email


class SignInSchema(BaseModel):
    email: EmailStr
    password: str

    @field_validator('email', 'password')
    def field_must_be_populated(cls, value):
        if not value:
            raise ValueError('This field must be complete')
        return value

    @field_validator('email')
    def email_must_be_valid(cls, email):
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise ValueError('The email field is invalid')
        return email
