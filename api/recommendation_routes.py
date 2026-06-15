from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from models.resource import Resource
from schemas.recommendation_schema import (
    RecommendationRequest,
    RecommendationResponse
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

    text = request.situation.lower()

    categories = []

    if any(
        word in text
        for word in [
            "food",
            "hungry",
            "groceries"
        ]
    ):
        categories.append("Food")

    if any(
        word in text
        for word in [
            "job",
            "employment",
            "work"
        ]
    ):
        categories.append(
            "Workforce Development"
        )

    if any(
        word in text
        for word in [
            "housing",
            "homeless",
            "rent"
        ]
    ):
        categories.append("Housing")

    if any(
        word in text
        for word in [
            "mental",
            "depression",
            "anxiety"
        ]
    ):
        categories.append(
            "Mental Health"
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