from abc import ABC, abstractmethod
from app.domain.entities.order import OrderEntity


class OrderCreatedEvent(ABC):

    @abstractmethod
    def send(self, order: OrderEntity) -> bool:
        raise NotImplemented


class OrderUpdatedEvent(ABC):

    @abstractmethod
    def send(self, order: OrderEntity) -> bool:
        raise NotImplemented
