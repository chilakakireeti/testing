from fastapi import FastAPI

from middleware.error_handler import (
    global_exception_handler
)

from middleware.request_logger import (
    request_logger
)

from utils.custom_error import AppError

from routes.test_route import router



app = FastAPI()



# Request logging middleware

app.middleware("http")(
    request_logger
)



# Global error handling

app.add_exception_handler(
    Exception,
    global_exception_handler
)



app.include_router(router)



@app.get("/health")
def health():

    return {

        "status":"running"

    }
