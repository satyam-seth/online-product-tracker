from fastapi import FastAPI

from .schemas import HealthCheck
from .sources import SourceCreate, SourceOut
from .sources import create_source

app = FastAPI()


@app.get("/health-check", response_model=HealthCheck, tags=["Health"])
def health_check():
    return HealthCheck()


# TODO: add session: SessionDep
@app.post("/sources", response_model=SourceOut, tags=["Sources"])
async def source_create(new_source: SourceCreate):
    source = await create_source(new_source)
    return source
