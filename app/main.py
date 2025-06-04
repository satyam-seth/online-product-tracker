from fastapi import FastAPI, HTTPException, Response, status

from app.sources.schemas import SourceUpdate

from .schemas import HealthCheck
from .sources import SourceCreate, SourceOut
from .sources import (
    create_source,
    get_source_by_id,
    list_sources,
    update_source,
    delete_source,
)

app = FastAPI()


@app.get("/health-check", response_model=HealthCheck, tags=["Health"])
def health_check():
    return HealthCheck()


# TODO: add session: SessionDep
@app.post("/sources", response_model=SourceOut, tags=["Sources"])
async def source_create(new_source: SourceCreate):
    source = await create_source(new_source)
    return source


# TODO: use http_exception_handler or custom exception handler
@app.get("/sources/{source_id}", response_model=SourceOut, tags=["Sources"])
async def source_get(source_id: int):
    source = await get_source_by_id(source_id)

    if not source:
        raise HTTPException(status_code=404, detail="Source not found")

    return source


# TODO: add support for pagination, filtering by domain
@app.get("/sources", response_model=list[SourceOut], tags=["Sources"])
async def source_list():
    source = await list_sources()
    return source


@app.patch("/sources/{source_id}", response_model=SourceOut, tags=["Sources"])
async def source_update(source_id: int, updated_source: SourceUpdate):
    source = await update_source(source_id, updated_source)

    if not source:
        raise HTTPException(status_code=404, detail="Source not found")

    return source


@app.delete("/sources/{source_id}", response_model=SourceOut, tags=["Sources"])
async def source_delete(source_id: int):
    succeed = await delete_source(source_id)

    if not succeed:
        raise HTTPException(status_code=404, detail="Source not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
