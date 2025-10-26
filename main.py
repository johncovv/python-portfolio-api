from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from starlette.requests import Request as StarletteRequest
from starlette.responses import JSONResponse
from dotenv import load_dotenv

from core import settings, logger

load_dotenv(dotenv_path=settings.Config.env_file)

app = FastAPI(
    title=settings.project_name,
    description=settings.description,
    version=settings.version,
)


@app.exception_handler(Exception)
async def global_exception_handler(request: StarletteRequest, exc: Exception):
    logger.error(f"Erro interno: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500, content={"detail": "Erro interno do servidor."}
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: StarletteRequest, exc: HTTPException):
    if exc.status_code == 500:
        logger.error(f"HTTP 500: {str(exc.detail)}", exc_info=True)
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


@app.get("/health")
async def health_check():
    return {
        "project_name": settings.project_name,
        "environment": settings.environment,
        "status": "ok",
    }


if __name__ == "__main__":
    import uvicorn

    print(f"Starting {settings.project_name} in {settings.environment} mode.")

    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.is_development,
        log_level="info",
        workers=1,
    )
