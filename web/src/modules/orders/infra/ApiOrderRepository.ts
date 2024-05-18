import { Order } from '../domain/Order';
import { OrderRepository } from '../domain/OrderRepository';

export function createApiOrderRepository(): OrderRepository {
	return {
		getAll,
	};
}

async function getAll(): Promise<Order[]> {
	const response = await fetch(process.env.NEXT_API_URL + '/orders');
	const comments = await response.json();

	return comments;
}
