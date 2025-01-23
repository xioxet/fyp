import { fail } from '@sveltejs/kit';
import { BACKEND_URL } from "$env/static/private";

export const actions = {
    default: async ({ fetch, params, request }) => {
        const formData = await request.formData();
        const fileData = formData.get('file');
        const response = await fetch(`http://${BACKEND_URL}:5000/upload/`, 
            {
                method: 'POST',
                body: formData
            }
        );
        const result = await response.json();
        console.log(result)
        if (result.error) {
            console.log('error triggered');
            return fail(400, {
                error: result.message
            })
        } else {
            console.log('returning...');
            return {
                success: true,
                message: "Upload succeeded!"
            }
        }
    }
}