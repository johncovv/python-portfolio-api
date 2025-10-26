from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = "Portfolio API"
    description: str = "API for managing portfolio information."
    version: str = "1.0.0"

    environment: str = "production"

    port: int = 8000
    host: str = "0.0.0.0"

    @property
    def is_development(self) -> bool:
        return self.environment == "development"

    class Config:
        env_file = ".env"


settings = Settings()
