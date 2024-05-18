from typing import List
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from app.domain.entities.order import OrderEntity
from app.infrastructure.container import Container
from app.application.services.order import OrderService
from app.infrastructure.schemas.order import OrderOutput

router = APIRouter(
    prefix='/orders',
    tags=['orders']
)


@router.get('/', response_model=List[OrderOutput])
@inject
def get_catalog(order_services: OrderService = Depends(Provide[Container.order_services])) -> List[dict]:
    response: List[OrderEntity] = order_services.orders_catalog()
    return [order_entity.__dict__ for order_entity in response]
