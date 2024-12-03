export const actions = {
	default: async (event) => {
		// add new message to Messages
	}
};

export async function load({ fetch, params }) {
	const response = await fetch('/messages');
    var messages = await response.json();
	return { messages };
}