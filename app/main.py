from fastapi import FastAPI

from .schemas import HealthCheck
from .sources import sources_router
from .snapshots import snapshots_router

app = FastAPI()


@app.get("/health-check", response_model=HealthCheck, tags=["Health"])
def health_check():
    return HealthCheck()


app.include_router(sources_router)
app.include_router(snapshots_router)
