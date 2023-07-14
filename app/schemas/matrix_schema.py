from typing import List
from pydantic import BaseModel, validator


class MatrixSchema(BaseModel):
    unclassified: List[int]

    @validator('unclassified')
    def field_must_be_populated(cls, value):
        if not value:
            raise ValueError('This field must be complete')
        return value
