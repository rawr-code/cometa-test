from typing import List
from datetime import datetime
from pydantic import BaseModel
from app.infrastructure.schemas.item import Item
from app.infrastructure.schemas.round import Round


class Order(BaseModel):
    created: datetime
    paid: bool
    subtotal: int
    taxes: int
    discounts: int
    items: List[Item]
    rounds: List[Round]
    
class OrderOutput(BaseModel):
    created: datetime
    paid: bool
    subtotal: int
    taxes: int
    discounts: int
    items: List[Item]
    rounds: List[Round]
