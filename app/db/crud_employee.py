from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import null

from . import models
from ..schemas import schemas


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employees(db: Session):
    return db.query(models.Employee).all()


def get_emplyees_by_job_status(db: Session, job_status: bool):
    try:
        lst = []
        if job_status:
            lst.extend(db.query(models.Employee).filter(models.Employee.job != None).all())
            return lst

        lst.extend(db.query(models.Employee).filter(models.Employee.job == None).all())
        return lst
    except:
        return {"error": "Employees not wound"}


def create_employee(db: Session, employeeIn: schemas.EmployeeCreate):
    e = models.Employee(name=employeeIn.name)
    db.add(e)
    db.commit()
    db.refresh(e)
    return e


def add_job_for_employee(db: Session, job_id: int, employee_id: int):
    j = db.query(models.Job).filter(models.Job.id == job_id).first()
    e = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    j.employee_id = e.id

    db.add(j)
    db.commit()
    db.refresh(j)
    return j