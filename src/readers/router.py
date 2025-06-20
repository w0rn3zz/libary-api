from fastapi import APIRouter, Depends

from src.readers.schemas import (
    ReaderAddSchema,
    ReaderResponseSchema,
    ReaderUpdateSchema,
)
from src.exceptions import (
    ReaderNotFoundException,
    ReaderDeleteFailedException,
    ReaderAddFailedException,
    ReaderUpdateFailedException,
)
from src.readers.dao import ReaderDAO
from src.users.dependencies import get_current_user
from src.users.models import User


router = APIRouter(prefix="/readers", tags=["readers"])


@router.get("/{reader_id}")
async def get__by_id(
    reader_id: int, current_user: User = Depends(get_current_user)
) -> ReaderResponseSchema:
    reader = await ReaderDAO.find_by_id(reader_id)
    if not reader:
        raise ReaderNotFoundException
    return reader


@router.post("/add")
async def add_reader(
    data: ReaderAddSchema, current_user: User = Depends(get_current_user)
):
    try:
        await ReaderDAO.add(**data.model_dump())
        return {"status": "ok", "message": "success"}
    except Exception:
        raise ReaderAddFailedException


@router.delete("/delete/{reader_id}")
async def delete_reader_by_id(
    reader_id: int, current_user: User = Depends(get_current_user)
):
    try:
        await ReaderDAO.delete_by_id(reader_id)
        return {"status": "ok", "message": "success"}
    except ValueError:
        raise ReaderDeleteFailedException


@router.patch("/update/{reader_id}")
async def update_reader_by_id(
    reader_id: int,
    data: ReaderUpdateSchema,
    current_user: User = Depends(get_current_user),
) -> ReaderResponseSchema:
    try:
        return await ReaderDAO.update_by_id(reader_id, **data.model_dump())
    except ValueError:
        raise ReaderUpdateFailedException
