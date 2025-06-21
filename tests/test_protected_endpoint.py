import pytest
from httpx import ASGITransport, AsyncClient

from src.main import app


@pytest.mark.asyncio
async def test_authorized_access(override_get_current_user, mock_borrow_book):
    cookies = {"access_token": "faketoken"}  

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test", cookies=cookies) as ac:
        response = await ac.get("/books/1")

    assert response.status_code == 200

@pytest.mark.asyncio
async def test_unauthorized_access():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/books/1")

    assert response.status_code == 401
    assert response.json()["detail"] == 'Токен отсутствует'


