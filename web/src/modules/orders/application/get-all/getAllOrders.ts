import { Order } from '../../domain/Order';
import { OrderRepository } from '../../domain/OrderRepository';

export function getAllOrders(orderRepository: OrderRepository) {
	return async (): Promise<Order[]> => {
		return await orderRepository.getAll();
	};
}
