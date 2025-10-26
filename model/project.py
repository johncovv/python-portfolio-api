from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, JSON, func
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from core.database import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4
    )

    name: Mapped[str] = mapped_column(String(128), nullable=False)
    alias: Mapped[str] = mapped_column(String(64), unique=True, nullable=True)
    description: Mapped[str] = mapped_column(String(1024), nullable=True)
    project_url: Mapped[str] = mapped_column(String(256), nullable=True)

    # Icon fields
    icon_alt: Mapped[str] = mapped_column(String(256), nullable=True)
    icon_url: Mapped[str] = mapped_column(String(256), nullable=True)

    # UI Design fields
    ui_design_type: Mapped[str] = mapped_column(String(64), nullable=True)
    ui_design_url: Mapped[str] = mapped_column(String(256), nullable=True)

    # Repository fields
    repository_type: Mapped[str] = mapped_column(String(64), nullable=True)
    repository_url: Mapped[str] = mapped_column(String(256), nullable=True)

    # Alert fields
    alert_type: Mapped[str] = mapped_column(String(64), nullable=True)
    alert_message: Mapped[str] = mapped_column(String(512), nullable=True)

    images: Mapped[JSON] = mapped_column(JSON, nullable=True, default=list)
    technologies: Mapped[JSON] = mapped_column(JSON, nullable=True, default=list)
    partners: Mapped[JSON] = mapped_column(JSON, nullable=True, default=list)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
    )
