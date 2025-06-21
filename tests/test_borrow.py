# test_borrow.py

import pytest
from httpx import ASGITransport, AsyncClient
from src.main import app


# tests/test_borrow.py
import pytest
from httpx import ASGITransport, AsyncClient
from src.main import app
from src.exceptions import BookUnavailableException, BorrowLimitExceededException

@pytest.mark.asyncio
async def test_borrow_4th_book_rejected(override_get_current_user, mock_borrow_book):
    mock_borrow_book.side_effect = BorrowLimitExceededException

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/borrows/take", params={"reader_id": 1, "book_id": 4})

    assert response.status_code == 400
    assert response.json() == {"detail": "Вы не можете взять более 3-х книг одновременно"}
    mock_borrow_book.assert_awaited_once_with(book_id=4, reader_id=1)

@pytest.mark.asyncio
async def test_borrow_unavailable_book(override_get_current_user, mock_borrow_book):
    mock_borrow_book.side_effect = BookUnavailableException

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/borrows/take", params={"reader_id": 1, "book_id": 999})

    assert response.status_code == 400
    assert response.json() == {"detail": "Сейчас эта книга не доступна"}
    mock_borrow_book.assert_awaited_once_with(book_id=999, reader_id=1)



