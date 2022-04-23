import sys
from django.db import router
sys.path.append("..")

from fastapi import FastAPI , Depends , HTTPException ,APIRouter
from database import SessionLocal  ,get_db
import models
from database import engine 
from sqlalchemy.orm import Session
from allschemas import Services
from exception import http_exception , successful_response

router = APIRouter()

models.Base.metadata.create_all(bind = engine)

router = APIRouter(
    tags=['service'],
)


@router.post('/')
async def create_service(service: Services, db: Session = Depends(get_db)):
    service_model = models.Service()
    service_model.name = service.name
    service_model.description = service.description
    service_model.category = service.category
    service_model.price= service.price
    
    #service_model.category_id = category.get('id')

    db.add(service_model)
    db.commit()

    return{
        'status' : 201 , 'transaction' : 'Successful'
    }

@router.get('/')
async def read_all(db : Session = Depends(get_db)):
    return db.query(models.Service).all()



@router.get('/services/{service_id}')
async def read_service(service_id: int, db: Session = Depends(get_db)):
    service_model = db.query(models.Service).filter(models.Service.id == service_id).first()  
    if service_model is not None:  
        return service_model
    raise http_exception()



@router.put('/{sevice_id}')
async def update_service(service_id : int, service: Services, db: Session = Depends(get_db)):
    service_model = db.query(models.Service).filter(models.Service.id == service_id).first()
        
    if service_model is None:
        raise http_exception()
    service_model.name = service.name
    service_model.description = service.description
    service_model.price= service.price
    service_model.category = service.category

    db.add(service_model)
    db.commit()

    return successful_response(200) 


@router.delete('/{service_id}')
async def delete_service(service_id : int, db: Session = Depends(get_db)):
    service_model = db.query(models.Service).filter(models.Service.id == service_id).first()
    if service_id is None:
        raise http_exception()
    db.query(models.Service).filter(models.Service.id == service_id).delete()
    db.commit()
    return successful_response(200)


'''
@app.get('/category/')
async def read_all(db : Session = Depends(get_db)):
    return db.query(models.Category).all()

@app.post('/category/')
async def create_category(category: Category, db: Session = Depends(get_db)):
    new_category = models.Category()
    new_category.name = category.name
    
    db.add(new_category)
    db.commit()

    return{
        'status' : 201 , 'transaction' : 'Successful'
    }
'''