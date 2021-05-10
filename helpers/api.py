import aiohttp


async def get_request(loop, url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            # print("Status:", response.status)
            # print("Content-type:", response.headers['content-type'])

            json = await response.json()
            # print("Body:", html)
            return json
