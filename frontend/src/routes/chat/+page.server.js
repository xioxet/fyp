import { browser } from "$app/environment";
import { BACKEND_URL } from "$env/static/private";

export async function load({ fetch, params }) {
	const response = await fetch(`http://${BACKEND_URL}:5000/get_messages/test`);
    var messages = await response.json();
	return { messages };
}

export const actions = {
	default: async ({fetch, params, request}) => {
		const formData = await request.formData();
    	const messagecontent = formData.get('message');
		const response = await fetch(`http://${BACKEND_URL}:5000/add_message/`, {
			headers: {
				'Content-Type': 'application/json'
			},
			method: "POST",
			body: JSON.stringify({
				"uuid":"test",
				"messagecontent":messagecontent,
				"fromuser":true
			})
		})
		const messages = await response.json();
		return { messages };
	}
}