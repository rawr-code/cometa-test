from app.domain.entities.order import OrderEntity
from app.domain.events.order import OrderCreatedEvent, OrderUpdatedEvent


class OrderCreatedQueueEvent(OrderCreatedEvent):

    def send(self, order: OrderEntity):
        return True


class OrderUpdatedQueueEvent(OrderUpdatedEvent):

    def send(self, order: OrderEntity):
        return True
