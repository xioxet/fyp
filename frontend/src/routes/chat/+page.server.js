import { browser } from "$app/environment";
import { BACKEND_URL } from "$env/static/private";
import { redirect } from '@sveltejs/kit';

export async function load({ fetch, params, cookies }) {
	const accessToken = cookies.get('accessToken');
	if (accessToken) {
		const response = await fetch(`http://${BACKEND_URL}:5000/get_messages/${accessToken}/`);
		var messages = await response.json();
		return { messages };
	} else {
		redirect(302, '/login')
	}
}

export const actions = {
	default: async ({fetch, params, request, cookies}) => {
		const accessToken = cookies.get('accessToken');
		const formData = await request.formData();
    	const messagecontent = formData.get('message');
		const response = await fetch(`http://${BACKEND_URL}:5000/add_message/`, {
			headers: {
				'Content-Type': 'application/json'
			},
			method: "POST",
			body: JSON.stringify({
				"jwt":accessToken,
				"messagecontent":messagecontent,
				"fromuser":true
			})
		})
		const messages = await response.json();
		return { messages };
	}
}