import { FC } from 'react';
import { Round } from '../../modules/orders/domain/Order';

// Utils
import { cn } from '../../utils';

// Testing
import createTestIDs from '../../testing/createTestIDs';
const ownTestIDs = createTestIDs('Bill', ['root']);

type TBillDetail = {
	title: string;
	label: string;
};

interface IBillProps {
	details: TBillDetail[];
	rounds: Round[];

	className?: string;
	classes?: {
		root?: string;
	};
	testIDs?: { [k in keyof typeof ownTestIDs]?: string | undefined };
}

const Bill: FC<IBillProps> = ({
	details,
	rounds,
	className = '',
	classes = {},
	testIDs = {},
}) => {
	return (
		<div
			className={cn(
				'w-80 rounded bg-gray-50 px-6 pt-8 border',
				className,
				classes.root,
			)}
			data-testid={testIDs.root || ownTestIDs.root}
		>
			<p className="text-6xl text-center my-2">🍺</p>
			<div className="flex flex-col justify-center items-center gap-2">
				<h4 className="font-semibold">Business Bar</h4>
			</div>
			<div className="flex flex-col gap-3 border-b py-6 text-xs">
				{details.map((detail, index) => (
					<p className="flex justify-between" key={index}>
						<span className="text-gray-400">{detail.title}</span>
						<span>{detail.label}</span>
					</p>
				))}
			</div>
			<div className="flex flex-col gap-3 pb-6 pt-2 text-xs">
				{rounds.map((round, index) => (
					<table className="w-full text-left" key={index}>
						<thead>
							<tr className="flex">
								<th className="w-full py-2">
									{new Date(round.created).toLocaleTimeString('en-US', {
										hour: '2-digit',
										minute: '2-digit',
									})}
								</th>
								<th className="min-w-[44px] py-2">Quantity</th>
							</tr>
						</thead>
						<tbody>
							{round.items.map((item, index) => (
								<tr className="flex" key={index}>
									<td className="flex-1 py-1">{item.name}</td>
									<td className="min-w-[44px] text-right">{item.quantity}</td>
								</tr>
							))}
						</tbody>
					</table>
				))}
			</div>
		</div>
	);
};

export default Bill;
export { ownTestIDs as testIDs };
