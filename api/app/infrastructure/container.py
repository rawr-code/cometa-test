from dependency_injector import containers, providers
from app.domain.entities.order import OrderEntityFactory
from app.infrastructure.events.order import OrderCreatedQueueEvent, OrderUpdatedQueueEvent
from app.infrastructure.handlers import Handlers
from app.infrastructure.repositories.order import OrderInMemoryRepository
from app.application.services.order import OrderService


class Container(containers.DeclarativeContainer):

    # loads all handlers where @injects are set
    wiring_config = containers.WiringConfiguration(modules=Handlers.modules())

    # Factories
    order_factory = providers.Factory(OrderEntityFactory)

    # Repositories
    order_repository = providers.Singleton(OrderInMemoryRepository)

    # Events
    order_created_event = providers.Factory(OrderCreatedQueueEvent)
    order_updated_event = providers.Factory(OrderUpdatedQueueEvent)

    # Services
    order_services = providers.Factory(
        OrderService, order_repository, order_created_event, order_updated_event)
