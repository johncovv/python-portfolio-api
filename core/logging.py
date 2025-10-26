import logging
from .settings import settings


def setup_logging():
    class ColoredFormatter(logging.Formatter):
        def format(self, record):
            if record.levelno == logging.INFO:
                record.msg = f"\033[92m{record.msg}\033[0m"
            elif record.levelno == logging.WARNING:
                record.msg = f"\033[93m{record.msg}\033[0m"
            elif record.levelno == logging.ERROR:
                record.msg = f"\033[91m{record.msg}\033[0m"
            return super().format(record)

    handler = logging.StreamHandler()
    handler.setFormatter(ColoredFormatter("%(message)s"))

    if settings.is_development:
        conversion_logger = logging.getLogger("conversion")
        conversion_logger.setLevel(logging.CRITICAL)

        return conversion_logger

    logging.basicConfig(
        level=logging.CRITICAL, handlers=[handler], encoding="utf-8", force=True
    )

    logging.getLogger().disabled = True

    startup_logger = logging.getLogger("startup")
    startup_logger.setLevel(logging.INFO)
    startup_logger.disabled = False

    conversion_logger = logging.getLogger("conversion")
    conversion_logger.disabled = True

    return startup_logger


logger = setup_logging()
