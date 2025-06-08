import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) 

import models
from database import engine 

from fastapi import FastAPI

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
