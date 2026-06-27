import logging
from logging.handlers import RotatingFileHandler


def get_logger():

    logger = logging.getLogger("backend")

    logger.setLevel(logging.INFO)


    handler = RotatingFileHandler(
        "app.log",
        maxBytes=5000000,
        backupCount=3
    )


    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )


    handler.setFormatter(formatter)


    if not logger.handlers:
        logger.addHandler(handler)


    return logger


logger = get_logger()