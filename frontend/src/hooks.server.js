import postgres from 'postgres';

export const handle = async ({event, resolve}) => {
    const sql = postgres('postgres://fyp-postgres:postgres@postgres:5432/main');

    event.locals = {
        sql: sql
    };

    const response = await resolve(event);
    return response;
}