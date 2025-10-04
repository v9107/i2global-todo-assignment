from fastapi import APIRouter

router = APIRouter(tags=["Base"], prefix="/base")


@router.get("/health")
async def health_check():
    return {"msg": "server healthy"}
