from fastapi import APIRouter, status

from ..schemas import Vote


router = APIRouter(prefix="/vote", tags=["Vote"])

@router.post('/', status_code=status.HTTP_201_CREATED)
async def vote(vote_obj: Vote):
    print(vote_obj.)
