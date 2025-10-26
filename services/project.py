from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel

from model.project import Project


class ProjectCreate(BaseModel):
    name: str
    alias: str | None = None
    description: str | None = None
    project_url: str | None = None
    icon_alt: str | None = None
    icon_url: str | None = None
    ui_design_type: str | None = None
    ui_design_url: str | None = None
    repository_type: str | None = None
    repository_url: str | None = None
    alert_type: str | None = None
    alert_message: str | None = None
    images: list | None = []
    technologies: list | None = []
    partners: list | None = []


class ProjectService:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def create_project(self, project: ProjectCreate):
        project = Project(**project.model_dump())

        self.session.add(project)
        await self.session.commit()
        await self.session.refresh(project)
        return project

    async def get_all_projects(self):
        result = await self.session.execute(select(Project))
        return result.scalars().all()
