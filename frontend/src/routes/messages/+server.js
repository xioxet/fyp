async function get_messages({ sql, uuid }) {
    const result = await sql`SELECT * FROM messages WHERE uuid='test';`
    return new Response(JSON.stringify(result), {
        headers: {
            'Content-Type': 'application/json'
        }
    })
}

export async function GET({ locals }) {
    const { sql } = locals;
    const uuid = "test";
    const healthcheck = await sql`SELECT * FROM pg_catalog.pg_tables`;
    return await get_messages({ sql, uuid })
}

export async function POST({ request, locals }) {
    const { sql } = locals;
    const body = await request.json();
    const messagecontent = body.messagecontent;
    console.log(`message = ${messagecontent}`)
    const uuid = "test";
    const fromuser = true;
    const query = await sql`INSERT INTO 
    MESSAGES (uuid, messagecontent, fromuser)VALUES (${uuid}, ${messagecontent}, ${fromuser})`;
    return await get_messages({sql, uuid});
}