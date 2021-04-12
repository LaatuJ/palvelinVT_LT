from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Boolean

from . import models
from ..schemas import schemas


def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()


def get_jobs(db: Session):
    return db.query(models.Job).all()


def get_jobs_by_job_done(db: Session, job_done: Boolean):
    return db.query(models.Job).filter(models.Job.job_done == job_done).all()



def create_job(db: Session, jobIn: schemas.JobCreate):
    j = models.Job(name=jobIn.name)
    db.add(j)
    db.commit()
    db.refresh(j)
    return j


def update_job(db: Session, job: schemas.JobUpdate):
    j = db.query(models.Job).filter(models.Job.id == job.job_id).first()

    if job.employee_id != None:
        e = db.query(models.Employee).filter(models.Employee.id == job.employee_id).first()
        j.employee = e
        
    if job.job_done != None:
        j.job_done = job.job_done
        if (job.job_done == True):
            j.employee = None
    
    db.add(j)
    db.commit()
    db.refresh(j)
    return j