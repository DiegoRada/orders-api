from pydantic import BaseModel, Field
from typing import Optional


class Customer(BaseModel):
    customerid: Optional[int] = None
    customername: str = Field(min_length=3, max_length=30)
    contactname: str = Field(min_length=3, max_length=30)
    address: str = Field(min_length=5, max_length=30)
    city: str = Field(min_length=5, max_length=30)
    postalcode: str = Field(min_length=5, max_length=30)
    country: str = Field(min_length=5, max_length=30)

    class Config:
        schema_extra = {
            "example": {
                "customerid": 1,
                "customername": "John Doe",
                "contactname": "John Doe",
                "address": "123 Main St",
                "city": "New York",
                "postalcode": "10001",
                "country": "USA"
            }
        }
