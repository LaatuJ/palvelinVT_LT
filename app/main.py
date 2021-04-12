from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import models
from .db.database import engine
from .routers import job, employee

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(job.router)
app.include_router(employee.router)