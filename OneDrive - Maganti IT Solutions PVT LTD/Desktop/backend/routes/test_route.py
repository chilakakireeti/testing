from fastapi import APIRouter

from utils.custom_error import AppError



router = APIRouter()



@router.get("/test-error")
async def test_error():


    raise AppError(
        "Database connection failed",
        503
    )