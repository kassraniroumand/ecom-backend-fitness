from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class HeroSlide(BaseModel):
    img: str
    eyebrow: str
    title: str
    body: str
    cta: str
    accent: str


class FeatureItem(BaseModel):
    title: str
    subtitle: str
    img: str


class CategoryGridItem(BaseModel):
    index: str
    title: str
    subtitle: str
    tag: str
    count: str
    img: str


class ShopByCategoryItem(BaseModel):
    title: str
    count: int
    img: str


class LatestProduct(BaseModel):
    badge: str | None = None
    title: str
    tagline: str
    price: str
    img: str
    dark: bool = False
    category: str | None = None


class ElegantProduct(BaseModel):
    name: str
    price: str
    img: str
    category: Literal["all", "cardio", "strength", "wellness"]


class ElegantTab(BaseModel):
    id: Literal["all", "cardio", "strength", "wellness"]
    label: str
    icon: Literal["home", "zap", "flame", "dumbbell"]


class ElegantlyDesignedSection(BaseModel):
    products: list[ElegantProduct]
    tabs: list[ElegantTab]


class AwardItem(BaseModel):
    category: str
    name: str
    img: str


class AwardTab(BaseModel):
    id: str
    label: str


class AwardsSection(BaseModel):
    catalogue: dict[str, list[AwardItem]]
    tabs: list[AwardTab]
    default_tab: str = Field(..., alias="defaultTab")

    model_config = {"populate_by_name": True}


class Story(BaseModel):
    tag: str
    title: str
    img: str


class HomepageContent(BaseModel):
    hero_slides: list[HeroSlide] = Field(..., alias="heroSlides")
    features: list[FeatureItem]
    category_grid: list[CategoryGridItem] = Field(..., alias="categoryGrid")
    shop_by_category: list[ShopByCategoryItem] = Field(..., alias="shopByCategory")
    latest: list[LatestProduct]
    elegantly_designed: ElegantlyDesignedSection = Field(..., alias="elegantlyDesigned")
    awards: AwardsSection
    stories: list[Story]

    model_config = {"populate_by_name": True}


class CategoryProduct(BaseModel):
    id: str
    name: str
    badge: str | None = None
    price_label: str = Field(..., alias="priceLabel")
    price: str
    finance: str
    features: list[str]
    img: str
    dark: bool = False

    model_config = {"populate_by_name": True}


class Category(BaseModel):
    slug: str
    crumb: str
    eyebrow: str
    title: str
    description: str
    filters: list[str]
    products: list[CategoryProduct]
    bottom_eyebrow: str = Field(..., alias="bottomEyebrow")
    bottom_title_lead: str = Field(..., alias="bottomTitleLead")
    bottom_title_accent: str = Field(..., alias="bottomTitleAccent")
    bottom_title_tail: str = Field(..., alias="bottomTitleTail")

    model_config = {"populate_by_name": True}


class CategoriesResponse(BaseModel):
    categories: list[Category]
    hero_images: dict[str, str] = Field(..., alias="heroImages")

    model_config = {"populate_by_name": True}


class ProductDetail(BaseModel):
    product: CategoryProduct
    category: Category
    related: list[CategoryProduct]


class PageBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    content: dict[str, Any] = Field(default_factory=dict)
    seo: dict[str, Any] = Field(default_factory=dict)


class PageCreate(PageBase):
    pass


class PageUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    content: dict[str, Any] | None = None
    seo: dict[str, Any] | None = None


class PageRead(PageBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
