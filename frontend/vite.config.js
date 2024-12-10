import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		cors: {
			"origin":"http://navi.fyp.com",
			"methods":"GET,HEAD,PUT,PATCH,POST,DELETE",
			"preflightContinue": false,
			"optionsSuccessStatus": 204
		}
	}
});
