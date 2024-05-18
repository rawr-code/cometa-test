from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.order import OrderEntity
from app.domain.events.order import OrderCreatedEvent, OrderUpdatedEvent
from app.domain.repositories.order import OrderRepository


class OrderUseCases(ABC):

    @abstractmethod
    def __init__(self, order_repository: OrderRepository,
                 order_created_event: OrderCreatedEvent,
                 order_updated_event: OrderUpdatedEvent
                 ):
        self.order_repository = order_repository
        self.order_created_event = order_created_event
        self.order_updated_event = order_updated_event

    @abstractmethod
    def orders_catalog(self) -> List[OrderEntity]:
        raise NotImplemented
