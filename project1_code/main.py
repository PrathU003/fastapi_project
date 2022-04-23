from fastapi import FastAPI , Depends 
import models
from database import engine 
import user , service

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

app.include_router(user.router)
app.include_router(service.router)
