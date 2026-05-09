from fastapi import APIRouter, HTTPException

from app.data.categories import find_product, related_products
from app.schemas import ProductDetail

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/{product_id}", response_model=ProductDetail)
def product(product_id: str) -> ProductDetail:
    found = find_product(product_id)
    if found is None:
        raise HTTPException(status_code=404, detail=f"product '{product_id}' not found")
    matched, parent = found
    return ProductDetail(
        product=matched,
        category=parent,
        related=related_products(parent, exclude_id=product_id, limit=3),
    )
