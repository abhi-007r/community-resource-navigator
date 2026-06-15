from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    situation: str


class ResourceResponse(BaseModel):
    id: int
    name: str
    category: str
    description: str | None = None
    city: str | None = None
    state: str | None = None
    phone: str | None = None
    website: str | None = None

    class Config:
        from_attributes = True


class RecommendationResponse(BaseModel):
    recommended_categories: list[str]
    resources: list[ResourceResponse]