from typing import List
from app.domain.entities.order import OrderEntityFactory, OrderEntity
from app.domain.repositories.order import OrderRepository


class OrderInMemoryRepository(OrderRepository):

    orders: List[dict] = [
        {
            "created": "2024-09-10 12:00:00",
            "paid": False,
            "subtotal": 0,
            "taxes": 0,
            "discounts": 0,
            "items": [],
            "rounds": [
                {
                    "created": "2024-09-10 12:00:30",
                    "items": [
                        {
                            "name": "Corona",
                            "quantity": 2
                        },
                        {
                            "name": "Club Colombia",
                            "quantity": 1
                        }
                    ]
                },
                {
                    "created": "2024-09-10 12:20:31",
                    "items": [
                        {
                            "name": "Club Colombia",
                            "quantity": 1
                        },
                        {
                            "name": "Quilmes",
                            "quantity": 2
                        }
                    ]
                },
                {
                    "created": "2024-09-10 12:43:21",
                    "items": [
                        {
                            "name": "Quilmes",
                            "quantity": 3
                        }
                    ]
                }
            ]
        },
    ]

    def get_all(self) -> List[OrderEntity]:
        return [OrderEntityFactory.create(**order) for order in self.orders]
