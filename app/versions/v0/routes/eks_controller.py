from fastapi import APIRouter

from . import log_controller
from . import event_controller

router = APIRouter()

router.include_router(
    log_controller.router,
    prefix="/logs",
    tags=["Logs"]
    #responses={418: {"description": "I'm a teapot"}},
)

router.include_router(
    event_controller.router,
    prefix="/events",
    tags=["Events"]
    #responses={418: {"description": "I'm a teapot"}},
)

@router.get("")
async def devops_root():
    return {
        "status": "SUCCES",
        "message": "EKS Root"
    }



