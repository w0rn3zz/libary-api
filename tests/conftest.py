import pytest
from unittest.mock import AsyncMock
from fastapi import Depends

from src.main import app
from src.users.dependencies import get_current_user
from src.users.models import User
from src.borrows.dao import BorrowDAO


@pytest.fixture
def override_get_current_user():
    async def fake_user():
        return User(id=1, username="testuser", email="test@test.com", hashed_password='test')
    app.dependency_overrides[get_current_user] = fake_user
    yield
    app.dependency_overrides.clear()


@pytest.fixture
def mock_borrow_book(monkeypatch):
    mock = AsyncMock()
    monkeypatch.setattr(BorrowDAO, "borrow_book", mock)
    return mock
