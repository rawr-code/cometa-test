from datetime import datetime
from typing import List
from app.infrastructure.schemas.item import Item
from app.infrastructure.schemas.round import Round


class OrderEntity:

    def __init__(self,
                 created: datetime,
                 paid: bool,
                 subtotal: int,
                 taxes: int,
                 discounts: int,
                 items: List[Item],
                 rounds: List[Round]):

        self.created = created
        self.paid = paid
        self.subtotal = subtotal
        self.taxes = taxes
        self.discounts = discounts
        self.items = items
        self.rounds = rounds


class OrderEntityFactory:

    @staticmethod
    def create(created: datetime,
               paid: bool,
               subtotal: int,
               taxes: int,
               discounts: int,
               items: List[Item],
               rounds: List[Round]) -> OrderEntity:
        return OrderEntity(created, paid, int(subtotal), int(taxes), int(discounts), items, rounds)
