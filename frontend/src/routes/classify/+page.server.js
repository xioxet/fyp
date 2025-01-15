import { fail } from '@sveltejs/kit';
import { BACKEND_URL } from "$env/static/private";

export const actions = {
    default: async ({ fetch, params, request }) => {
        const formData = await request.formData();
        
        const response = await fetch(`http://${BACKEND_URL}:5000/classify/`, 
            {
                method: 'POST',
                body: formData
            }
        );
        const result = await response.json();
        console.log(result);
        if (result.error) {
            console.log('error triggered');
            return fail(400, {
                error: result.message
            });
        } else {
            return {
                success: true,
                data: {
                    classification: result.classification,
                }
            };
        }
    }
};