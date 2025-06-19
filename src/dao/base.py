from sqlalchemy import select, insert, update
from src.database import async_session
class BaseDAO:
    model = None
    
    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
    
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    @classmethod
    async def add(cls, **data):
        async with async_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
    @classmethod
    async def update_by_id(cls, model_id:int, **kwargs):
        async with async_session() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            item = result.scalar_one_or_none()
            
            if item is None:
                raise ValueError(f"Item with id {item} not found")
            
            update_query = (
                update(cls.model)
                .where(cls.model.id == model_id)
                .values(**kwargs)
                .returning(cls.model)
            )
            
            result = await session.execute(update_query)
            updated_item = result.scalar_one()
            await session.commit()

            return updated_item
    
    @classmethod
    async def delete_by_id(cls, model_id: int) -> bool:
        async with async_session() as session:
            query = select(cls.model).where(cls.model.id == model_id)
            result = await session.execute(query)
            entity = result.scalar_one_or_none()
            
            if not entity:
                return False
            
            await session.delete(entity)
            await session.commit()
            return True
    