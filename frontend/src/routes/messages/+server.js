//async function get_messages({ sql, uuid }) {
//    const result = await sql`SELECT * FROM messages WHERE uuid='test';`
//    return new Response(JSON.stringify(result), {
//        headers: {
//            'Content-Type': 'application/json'
//        }
//    })
//}
//
//export async function GET({ locals }) {
//    const { sql } = locals;
//    const uuid = "test";
//    const healthcheck = await sql`SELECT * FROM pg_catalog.pg_tables`;
//    return await get_messages({ sql, uuid })
//}
//
//export async function POST({ request, locals }) {
//    const { sql } = locals;
//    const body = await request.json();
//    const messagecontent = body.messagecontent;
//    const uuid = "test";
//    const fromuser = true;
//    const user_query = await sql`INSERT INTO 
//    MESSAGES (uuid, messagecontent, fromuser)VALUES (${uuid}, ${messagecontent}, ${fromuser === true})`;
//    
//    // ask backend
//    console.log('sending to backend')
//    const backend_response = await fetch('http://fyp-backend:5000/process_message', {
//        headers: {
//            'Content-Type': 'application/json'
//        },
//        method: "POST",
//        body: JSON.stringify({
//            'message': messagecontent
//        })
//    })
//
//    const backend_message = await backend_response.json();
//
//    const backend_query = await sql`INSERT INTO 
//    MESSAGES (uuid, messagecontent, fromuser)VALUES (${uuid}, ${backend_message.message}, ${fromuser === false})`;
//
//    return await get_messages({sql, uuid});
//}