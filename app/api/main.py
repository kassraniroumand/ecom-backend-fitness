from fastapi import APIRouter

from app.api.routes import categories, health, homepage, items, pages, products

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(homepage.router)
api_router.include_router(categories.router)
api_router.include_router(products.router)
api_router.include_router(items.router)
api_router.include_router(pages.router)
