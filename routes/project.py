from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db_session
from services.project import ProjectCreate, ProjectService

router = APIRouter(prefix="/projects", tags=["Project"])


@router.get("/")
async def get_all_projects(
    session: AsyncSession = Depends(get_db_session),
):
    service = ProjectService(session)
    return await service.get_all_projects()


@router.post("/")
async def create_project(
    project: ProjectCreate,
    session: AsyncSession = Depends(get_db_session),
):
    service = ProjectService(session)
    return await service.create_project(project)
