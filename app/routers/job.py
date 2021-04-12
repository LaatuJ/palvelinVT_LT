from typing import List, Optional
from fastapi import APIRouter, Depends, status

from ..schemas import schemas

from ..db import crud_job
from ..utils.common import get_db

from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/job',
    tags=['job']
)


@router.post('/', response_model=schemas.Job, status_code=status.HTTP_201_CREATED)
def create_job(t: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud_job.create_job(db, t)

@router.put('/', response_model=schemas.JobFull, status_code=status.HTTP_201_CREATED)
def update_job(t: schemas.JobUpdate, db: Session = Depends(get_db)):
    return crud_job.update_job(db, t)


# /job?job_done=false
@router.get('/', response_model=List[schemas.Job])
def read_jobs(job_done: Optional[bool] = None, db: Session = Depends(get_db)):
    if job_done != None:
        return crud_job.get_jobs_by_job_done(db, job_done)
    return crud_job.get_jobs(db)


@router.get('/{job_id}', response_model=schemas.JobFull)
def read_job(job_id: int, db: Session = Depends(get_db)):
    return crud_job.get_job(db, job_id)
