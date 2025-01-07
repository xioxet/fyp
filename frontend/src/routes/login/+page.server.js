import { browser } from "$app/environment";
import { BACKEND_URL } from "$env/static/private";
import { redirect } from '@sveltejs/kit';

export const actions = {
	default: async ({fetch, params, request, cookies}) => {
		const formData = await request.formData();
    	const username = formData.get('username');
        const password = formData.get('password');

		const response = await fetch(`http://${BACKEND_URL}:5000/login/`, {
			headers: {
				'Content-Type': 'application/json'
			},
			method: "POST",
			body: JSON.stringify({
				"username":username,
				"password":password,
			})
		})
		const result = await response.json();
        if (result.error) {
            console.log(result.message);
        } else {
            const jwt = result.message;
            cookies.set(
                'accessToken', jwt, {
                    secure: true,
                    httpOnly: true,
                    path: '/'
                }
            )
            redirect(302, '/chat')
        }
		console.log(messages);
	}
}