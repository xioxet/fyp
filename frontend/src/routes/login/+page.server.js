import { browser } from "$app/environment";
import { BACKEND_URL } from "$env/static/private";
import { redirect } from '@sveltejs/kit';
import { fail } from '@sveltejs/kit';

export const actions = {
	default: async ({ fetch, params, request, cookies }) => {
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
			return fail(400, {
				error: result.message
			})
        } else {
            const jwt = result.message;
            cookies.set(
                'accessToken', jwt, {
                    secure: false,
                    path: '/'
                }
            )
			cookies.set(
				'loggedIn', true, {
					secure: false,
					path: '/',
					httpOnly: false
				}
			)
			cookies.set(
				'username', result.username, {
					secure: false,
					path: '/',
					httpOnly: false
				}
			)
            redirect(302, '/chat')
        }
	}
}