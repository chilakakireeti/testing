import time

from fastapi import Request

from config.logger import logger



async def request_logger(
    request: Request,
    call_next
):

    start = time.time()


    response = await call_next(request)


    duration = time.time() - start


    logger.info(

        f"{request.method} "
        f"{request.url.path} "
        f"completed in {duration:.2f}s"

    )


    return response