from fastapi import APIRouter

from app.data.content import build_homepage_content
from app.schemas import HomepageContent

router = APIRouter(tags=["homepage"])


@router.get("/homepage", response_model=HomepageContent)
def homepage() -> HomepageContent:
    return build_homepage_content()
