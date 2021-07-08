from typing import Optional

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def events():
    try:
        
        # jobs


        return {
            "status": "SUCCESS",
            "message": "Aciklama",
            "data": {}
        }
    except Exception as e:
        return {
            "status": "SUCCESS",
            "message": "Errors: " + str(e),
            "data": {}
        }

