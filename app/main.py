from fastapi import FastAPI
from app.config.database import engine, Base
from app.routers.product import router as product_router

app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

app.include_router(product_router, prefix="/api", tags=["products"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Product Management System!"}
