from fastapi import APIRouter

from src.api.endpoints import hello, hi, teapot

api_router = APIRouter()
api_router.include_router(hello.router, tags=['hello'])
api_router.include_router(hi.router, tags=['hi'])
api_router.include_router(teapot.router, tags=['teapot'])
