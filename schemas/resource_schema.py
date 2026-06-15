from pydantic import BaseModel


class ResourceResponse(BaseModel):
    id: int
    name: str
    category: str
    description: str
    city: str | None = None
    state: str | None = None
    phone: str | None = None
    website: str | None = None

    class Config:
        from_attributes = True