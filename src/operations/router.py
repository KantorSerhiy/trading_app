from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["operations"]
)


@router.get("/")
async def get_specific_operation(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.all


@router.post("/")
async def add_specific_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    statement = insert(operation).values(**new_operation.dict())
    await session.execute(statement)
    await session.commit()
    return {"status": "success"}

@router.get('/ad')
async def test():
    pass
