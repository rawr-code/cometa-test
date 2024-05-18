from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.order import OrderEntity


class OrderRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[OrderEntity]:
        raise NotImplemented
