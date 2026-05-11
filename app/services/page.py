from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Page
from app.schemas import PageCreate, PageUpdate


async def create_page(db: AsyncSession, data: PageCreate) -> Page:
    page = Page(title=data.title, content=data.content, seo=data.seo)
    db.add(page)
    await db.commit()
    await db.refresh(page)
    return page


async def get_page(db: AsyncSession, page_id: int) -> Page | None:
    return await db.get(Page, page_id)


async def list_pages(
    db: AsyncSession, *, limit: int = 50, offset: int = 0
) -> Sequence[Page]:
    stmt = select(Page).order_by(Page.id).limit(limit).offset(offset)
    result = await db.execute(stmt)
    return result.scalars().all()


async def update_page(
    db: AsyncSession, page: Page, data: PageUpdate
) -> Page:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(page, field, value)
    await db.commit()
    await db.refresh(page)
    return page


async def delete_page(db: AsyncSession, page: Page) -> None:
    await db.delete(page)
    await db.commit()
