from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .crud import advert_query_set
from .schemas import Advert, AdvertCreate
from models import db_helper

router = APIRouter(tags=["Advertisements"])


@router.get("/{advert_id}/", response_model=Advert)
async def get_advert_by_id(
        advert_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    advert = await advert_query_set.get_advert(session=session, advert_id=advert_id)
    if advert is not None:
        return advert


@router.get("/", response_model=list(Advert))
async def get_all_adverts(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await advert_query_set.get_adverts(session=session)


@router.get("/", response_model=AdvertCreate)
async def create_advert(
        advert_in: AdvertCreate,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await advert_query_set.create_advert(session=session, advert_in=advert_in)
