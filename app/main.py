from fastapi import FastAPI
from api.resource_routes import router as resource_router
from api.auth_routes import router as auth_router
from api.recommendation_routes import (
    router as recommendation_router
    
)

app = FastAPI(
    title="Community Resource Navigator",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(resource_router)
app.include_router(recommendation_router)

@app.get("/")
def root():
    return {
        "message": "Community Resource Navigator API Running"
    }