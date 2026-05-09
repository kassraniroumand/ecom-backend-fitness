from fastapi import APIRouter, HTTPException

from app.data.categories import HERO_IMAGES, all_categories, get_category
from app.schemas import CategoriesResponse, Category

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("", response_model=CategoriesResponse)
def categories() -> CategoriesResponse:
    return CategoriesResponse(
        categories=all_categories(),
        heroImages=HERO_IMAGES,
    )


@router.get("/{slug}", response_model=Category)
def category(slug: str) -> Category:
    found = get_category(slug)
    if found is None:
        raise HTTPException(status_code=404, detail=f"category '{slug}' not found")
    return found
