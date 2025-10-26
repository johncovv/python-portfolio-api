# Portfolio API

A minimal FastAPI service for my portfolio website.

The main purpose of this project is to help me learn Python.

## Features

- Environment-based config via `pydantic-settings` and `.env`

## Quickstart

1. Create and activate a virtual environment (optional, but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  

# Windows: .venv\\Scripts\\activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Configure environment

- Copy `.env.example` to `.env` and adjust as needed.

```bash
cp .env.example .env
```

Available variables:

- `ENVIRONMENT` — e.g., `development` or `production`
- `PORT` — server port, default `8000`
- `HOST` — server host, default `0.0.0.0` in code (example shows `localhost`)

4. Run the API (development)

```bash
python main.py
```

Or with uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Once running, open:

- Docs (Swagger UI): http://localhost:8000/docs
- Docs (Redoc): http://localhost:8000/redoc
- Health: http://localhost:8000/health

## Configuration

- Settings source: `core/settings.py`
- Loads `.env` automatically at startup.
- Key computed property:
  - `Settings.is_development` toggles dev behaviors like uvicorn `reload`.

## License

This project is provided as-is for educational purposes. Add your preferred license if publishing.

