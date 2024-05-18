import runCommonTests from '../../testing/runCommonTests';

// Component
import Bill, { testIDs } from './Bill';

describe('Component | Bill', () => {
	runCommonTests(
		Bill,
		{ rootTestID: testIDs.root },
		{
			details: [
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
			],
			rounds: [],
		},
	);
});
