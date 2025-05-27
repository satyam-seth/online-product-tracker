from fastapi import FastAPI

from .schemas import HealthCheck
from .sources import SourceCreate, SourceOut
from .sources import create_source, get_source_by_id

app = FastAPI()


@app.get("/health-check", response_model=HealthCheck, tags=["Health"])
def health_check():
    return HealthCheck()


# TODO: add session: SessionDep
@app.post("/sources", response_model=SourceOut, tags=["Sources"])
async def source_create(new_source: SourceCreate):
    source = await create_source(new_source)
    return source


@app.get("/sources/{source_id}", response_model=SourceOut, tags=["Sources"])
async def source_get(source_id: int):
    source = await get_source_by_id(source_id)
    return source
