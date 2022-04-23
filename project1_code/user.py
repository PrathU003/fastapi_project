import sys
from django.db import router
sys.path.append("..")

from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import get_db ,engine
from fastapi import Depends , FastAPI , APIRouter
import models
from allschemas import CreateUser
from exception import get_user_exception , http_exception , successful_response


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix='/user',
    tags=['user'],
)

'------------------------------------------------------------------------------------------------------------------------'
bcrypt_context = CryptContext(schemes = ['bcrypt'], deprecated = 'auto')

def get_password_hash(password):
    return bcrypt_context.hash(password)

def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)

'--------------------------------------------------------------------------------------------------------------------------'


@router.post('/create/user')
async def create_new_user(create_user: CreateUser , db : Session =Depends(get_db)):
    create_user_model = models.Users()
    create_user_model.email = create_user.email
    create_user_model.username = create_user.username
    create_user_model.first_name = create_user.first_name
    create_user_model.last_name = create_user.last_name
    create_user_model.mobile = create_user.mobile
    #hash password
    hash_password = get_password_hash(create_user.password)
    create_user_model.hashed_password = hash_password
    create_user_model.is_active = True
    db.add(create_user_model)
    db.commit()

@router.get('/')
async def read_all_users(db : Session = Depends(get_db)):
    return db.query(models.Users).all()

@router.get('/user/{user_id}')
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.id == user_id).first()  
    if user_model is not None:  
        return user_model
    raise http_exception()

@router.put('/{user_id}')
async def update_user(user_id : int, create_user: CreateUser, db: Session = Depends(get_db)):
    update_user_model = db.query(models.Users).filter(models.Users.id == user_id).first()  
        
    if update_user_model is None:
        raise http_exception()
    update_user_model.email = create_user.email
    update_user_model.username = create_user.username
    update_user_model.first_name = create_user.first_name
    update_user_model.last_name = create_user.last_name
    update_user_model.mobile = create_user.mobile
    hash_password = get_password_hash(create_user.password)
    update_user_model.hashed_password = hash_password
    update_user_model.is_active = True
    db.add(update_user_model)
    db.commit()

    return successful_response(200)

@router.delete('/{user_id}')
async def delete_user(user_id : int, db: Session = Depends(get_db)):
    service_model = db.query(models.Service).filter(models.Service.id == user_id).first()
    if user_id is None:
        raise http_exception()
    db.query(models.Users).filter(models.Users.id == user_id).delete()
    db.commit()
    return successful_response(200)


