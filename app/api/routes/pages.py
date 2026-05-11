from fastapi import APIRouter, HTTPException, Query, status

from app.api.deps import DbSession
from app.schemas import PageCreate, PageRead, PageUpdate
from app.services import page as page_service

router = APIRouter(prefix="/pages", tags=["pages"])


@router.post("", response_model=PageRead, status_code=status.HTTP_201_CREATED)
async def create_page(payload: PageCreate, db: DbSession) -> PageRead:
    page = await page_service.create_page(db, payload)
    return PageRead.model_validate(page)


@router.get("", response_model=list[PageRead])
async def list_pages(
    db: DbSession,
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
) -> list[PageRead]:
    pages = await page_service.list_pages(db, limit=limit, offset=offset)
    return [PageRead.model_validate(p) for p in pages]


@router.get("/{page_id}", response_model=PageRead)
async def get_page(page_id: int, db: DbSession) -> PageRead:
    page = await page_service.get_page(db, page_id)
    if page is None:
        raise HTTPException(status_code=404, detail=f"page {page_id} not found")
    return PageRead.model_validate(page)


@router.patch("/{page_id}", response_model=PageRead)
async def update_page(
    page_id: int, payload: PageUpdate, db: DbSession
) -> PageRead:
    page = await page_service.get_page(db, page_id)
    if page is None:
        raise HTTPException(status_code=404, detail=f"page {page_id} not found")
    updated = await page_service.update_page(db, page, payload)
    return PageRead.model_validate(updated)


@router.delete("/{page_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_page(page_id: int, db: DbSession) -> None:
    page = await page_service.get_page(db, page_id)
    if page is None:
        raise HTTPException(status_code=404, detail=f"page {page_id} not found")
    await page_service.delete_page(db, page)
