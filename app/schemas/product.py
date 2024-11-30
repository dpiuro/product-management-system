from datetime import datetime

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(..., max_length=50)
    description: str = Field(None, max_length=255)
    price: float = Field(..., gt=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    created_at: datetime

    class Config:
        orm_mode = True
