from fastapi import APIRouter

from .routes import eks_controller

router = APIRouter()

router.include_router(
    eks_controller.router,
    prefix="/eks",
    #responses={418: {"description": "I'm a teapot"}},
)

@router.get("")
async def v0_root():
    return {
        "status": "SUCCES",
        "message": "API V0 Root"
    }



