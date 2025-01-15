import { fail } from '@sveltejs/kit';
import { BACKEND_URL } from "$env/static/private";


export const actions = {
    default: async ({ fetch, params, request }) => {
        const formData = await request.formData();
        const fileData = formData.get('file');
        const response = await fetch(`http://${BACKEND_URL}:5000/classify/`, 
            {
                method: 'POST',
                body: formData
            }
        );
    }
}