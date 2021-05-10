import asyncio
import pytest

import helpers.api
import helpers.db


@pytest.mark.asyncio
async def test_api(event_loop):
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    json_response = await helpers.api.get_request(event_loop, url)
    print(json_response)
    assert json_response['id'] == 1


@pytest.mark.asyncio
async def test_database_one(event_loop):
    query = 'SELECT * FROM cart_log WHERE id = 8;'
    db_record = await helpers.db.poll_db(event_loop, query)
    assert db_record is not None


@pytest.mark.asyncio
async def test_database_two(event_loop):
    query = 'SELECT * FROM cart_log WHERE id = 7;'
    db_record = await helpers.db.poll_db(event_loop, query)
    print(db_record)
    assert db_record is not None
    (_, merchant_id, logged) = db_record
    assert merchant_id == '123'


@pytest.fixture
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
