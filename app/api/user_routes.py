from fastapi import APIRouter, HTTPException, status
from ..schemas.user_schemas import UserIn, UserOut
# from ..dependencies import db_dependency
from ..context_managers import get_db
from ..repositories.repositories import UserRepository
from ..services.services import UserService
from ..worker.tasks.arithmetic import add, mul

router = APIRouter(prefix="/users", tags=["Users"])

# @router.post("/register/", response_model=UserOut)
# def register(user_in: UserIn, db: db_dependency):
#     try:
#         service = UserService(UserRepository(db))
#         add.apply_async((10, 16))
#         return service.register_user(user_in)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# @router.post("/get/", response_model=UserOut)
# def get_user(user_in: UserIn, db: db_dependency):
#     try:
#         service = UserService(UserRepository(db))
#         mul.delay(20, 16)
#         return service.get_user(user_in)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
@router.post("/register/", response_model=UserOut)
def register(user_in: UserIn):
    with get_db() as db:
        try:
            service = UserService(UserRepository(db))
            add.apply_async((10, 16))
            return service.register_user(user_in)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/get/", response_model=UserOut)
def get_user(user_in: UserIn):
    with get_db() as db:
        try:
            service = UserService(UserRepository(db))
            mul.delay(20, 16)
            return service.get_user(user_in)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))