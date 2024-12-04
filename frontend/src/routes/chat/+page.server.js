import { browser } from "$app/environment";

export async function load({ fetch, params }) {
	const response = await fetch('/messages');
    var messages = await response.json();
	return { messages };
}

export const actions = {
	default: async ({fetch, params, request}) => {
		const formData = await request.formData();
    	const message = formData.get('message');
		const response = await fetch('/messages', {
			headers: {
				'Content-Type': 'application/json'
			},
			method: "POST",
			body: JSON.stringify({
				"messagecontent":message
			})
		})
		const messages = await response.json();
		return { messages };
	}
}