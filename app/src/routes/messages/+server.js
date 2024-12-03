export async function GET({ locals }) {
    const { sql } = locals;
    const healthcheck = await sql`SELECT * FROM pg_catalog.pg_tables`;
    const result = await sql`SELECT * FROM messages WHERE uuid='test';`
    console.log(result)
    return new Response(JSON.stringify(result), {
        headers: {
            'Content-Type': 'application/json'
        }
    })
}