from models import Adverts
from .schemas import AdvertCreate

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result


class AdvertQuerySet:
    @classmethod
    async def create_advert(cls, session: AsyncSession, advert_in: AdvertCreate) -> Adverts:
        db_ad = Adverts(**advert_in.model_dump())
        session.add(db_ad)
        await session.commit()
        return db_ad

    @classmethod
    async def get_adverts(cls, session: AsyncSession) -> list[Adverts] | None:
        stmt = select(Adverts).order_by(Adverts.position)
        result: Result = await session.execute(stmt)
        db_ad = result.scalars().all()
        return list(db_ad)

    @classmethod
    async def get_advert(cls, session: AsyncSession, advert_id: int) -> Adverts | None:
        return await session.get(Adverts, advert_id)


advert_query_set = AdvertQuerySet()
