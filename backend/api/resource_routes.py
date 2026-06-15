from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.dependencies import get_db

from models.resource import Resource

from schemas.resource_schema import ResourceResponse

router = APIRouter(
    prefix="/resources",
    tags=["Resources"]
)


@router.get(
    "/",
    response_model=list[ResourceResponse]
)
def get_resources(
    db: Session = Depends(get_db)
):
    return db.query(Resource).all()

@router.get("/search")
def search_resources(
    category: str,
    db: Session = Depends(get_db)
):
    resources = (
        db.query(Resource)
        .filter(Resource.category.ilike(f"%{category}%"))
        .all()
    )

    return resources

@router.get(
    "/{resource_id}",
    response_model=ResourceResponse
)
def get_resource(
    resource_id: int,
    db: Session = Depends(get_db)
):
    resource = (
        db.query(Resource)
        .filter(Resource.id == resource_id)
        .first()
    )

    if not resource:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    return resource
