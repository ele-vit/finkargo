from typing import List
from pydantic import BaseModel, validator


class FinancialSchema(BaseModel):
    months: List[str]
    sales: List[float]
    bills: List[float]

    @validator('months', 'sales', 'bills')
    def field_must_be_populated(cls, value):
        if not value:
            raise ValueError('This field must be complete')
        return value
