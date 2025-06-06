from fastapi import APIRouter, HTTPException, Response, status

from .schemas import SourceCreate, SourceOut, SourceUpdate
from .services import (
    create_source,
    get_source_by_id,
    list_sources,
    update_source,
    delete_source,
)

sources_router = APIRouter(prefix="/sources", tags=["Sources"])


# TODO: add session: SessionDep
@sources_router.post("/", response_model=SourceOut)
async def source_create(new_source: SourceCreate):
    source = await create_source(new_source)
    return source


# TODO: use http_exception_handler or custom exception handler
@sources_router.get("/{source_id}", response_model=SourceOut)
async def source_get(source_id: int):
    source = await get_source_by_id(source_id)

    if not source:
        raise HTTPException(status_code=404, detail="Source not found")

    return source


# TODO: add support for pagination, filtering by domain
@sources_router.get("/", response_model=list[SourceOut])
async def source_list():
    source = await list_sources()
    return source


@sources_router.patch("/{source_id}", response_model=SourceOut)
async def source_update(source_id: int, updated_source: SourceUpdate):
    source = await update_source(source_id, updated_source)

    if not source:
        raise HTTPException(status_code=404, detail="Source not found")

    return source


@sources_router.delete("/{source_id}", response_model=SourceOut)
async def source_delete(source_id: int):
    succeed = await delete_source(source_id)

    if not succeed:
        raise HTTPException(status_code=404, detail="Source not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
