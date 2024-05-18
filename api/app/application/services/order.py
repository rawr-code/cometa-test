from typing import List
from app.domain.use_cases.order import OrderUseCases
from app.domain.entities.order import OrderEntity
from app.domain.events.order import OrderCreatedEvent, OrderUpdatedEvent
from app.domain.repositories.order import OrderRepository


class OrderService(OrderUseCases):

    def __init__(self, order_repository: OrderRepository,
                 order_created_event: OrderCreatedEvent,
                 order_updated_event: OrderUpdatedEvent
                 ):
        super().__init__(order_repository, order_created_event, order_updated_event)

    def orders_catalog(self) -> List[OrderEntity]:
        orders = self.order_repository.get_all()
        return orders
