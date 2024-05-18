from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class Round_Item(BaseModel):
    name: str
    quantity: Optional[int]


class Round(BaseModel):
    created: datetime
    items: List[Round_Item]
