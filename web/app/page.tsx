import { createApiOrderRepository } from '@/src/modules/orders/infra/ApiOrderRepository';

// Components
import Bill from '@/src/components/Bill/Bill';

export default async function Home() {
	const orders = await createApiOrderRepository().getAll();

	const mainOrder = orders[0];

	return (
		<main className="w-full h-full flex items-center justify-center">
			<Bill
				details={[
					{
						title: 'Receipt No.',
						label: '1997',
					},
					{
						title: 'Order Type',
						label: 'FullStack Developer',
					},
					{
						title: 'Host',
						label: 'Emmanuel Villegas',
					},
					{
						title: 'Customer',
						label: 'Amaury Prieto',
					},
				]}
				rounds={mainOrder.rounds}
			/>
		</main>
	);
}
