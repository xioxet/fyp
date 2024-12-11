import {json} from '@sveltejs/kit';
import { PROXY_URL } from "$env/static/private";


//export async function handle({event, resolve}) {
//    
//    const response = await resolve(event);
//
//    if (event.url.pathname.startsWith('/chat')) {
//
//        response.headers.set('Access-Control-Allow-Origin', `http://kita.fyp.com`);
//        response.headers.set('Access-Control-Allow-Methods','GET, POST');
//        response.headers.set('Access-Control-Allow-Headers','Content-Type, Authorization');
//        response.headers.set('Access-Control-Allow-Credentials','true');
//
//        console.log(`attempted to set headers for ${response.headers}`)
//
//
//    }
//
//    if (event.request.method === 'OPTIONS') {
//        console.log('OPTIONS request sent');
//    }
//
//    if (event.request.method === 'POST') {
//        console.log('POST request sent');
//    }
//
//    return response;
//}

