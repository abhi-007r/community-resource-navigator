from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.dependencies import get_db

from models.resource import Resource

from schemas.recommendation_schema import (
    RecommendationRequest,
    RecommendationResponse
)

from services.recommendation_service import (
    extract_categories
)

router = APIRouter(
    prefix="/recommend",
    tags=["Recommendations"]
)


@router.post(
    "/",
    response_model=RecommendationResponse
)
def recommend_resources(
    request: RecommendationRequest,
    db: Session = Depends(get_db)
):

    categories = extract_categories(
        request.situation
    )

    resources = (
        db.query(Resource)
        .filter(
            Resource.category.in_(categories)
        )
        .all()
    )

    return {
        "recommended_categories": categories,
        "resources": resources
    }