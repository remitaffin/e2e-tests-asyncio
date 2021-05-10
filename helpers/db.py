import asyncio
import os
import aiomysql

HEARTBEAT = 1
MAX_ATTEMPTS = 30

async def poll_db(loop, query):
    pool = await aiomysql.create_pool(
        host=os.environ['DB_HOST'], port=3306,
        user=os.environ['DB_USERNAME'], password=os.environ['DB_PASSWORD'],
        db=os.environ['DB_NAME'], loop=loop, autocommit=True,
    )
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            for attempt in range(MAX_ATTEMPTS):
                await cur.execute(query)
                response = await cur.fetchone()
                if not response:
                    await asyncio.sleep(HEARTBEAT)
                    continue
                else:
                    return response
            return None
    pool.close()
    await pool.wait_closed()
