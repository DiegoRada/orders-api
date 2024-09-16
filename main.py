
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import List
from schemas.customer import Customer
from config.database import Session
from services.customer import CustomerService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()
app.title = "Orders API"
app.version = "0.0.1"


@app.get('/', tags=['home'])
def home():
    return HTMLResponse(f'<h1>Orders API </h1>')


@app.get('/customers', tags=['customers'], response_model=List[Customer])
def get_customers():
    db = Session()
    result = CustomerService(db).get_customers()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@app.get('/customer/{id}', tags=['customers'], response_model=Customer)
def get_customer(id: int):
    db = Session()
    result = CustomerService(db).get_customer(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


def run():
    uvicorn.run("main:app", reload=True)


if __name__ == "__main__":
    run()
