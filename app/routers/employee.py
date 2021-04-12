from typing import List, Optional
from fastapi import APIRouter, Depends, status

from ..schemas import schemas

from ..db import crud_employee
from ..utils.common import get_db

from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/employee',
    tags=['employee']
)


@router.post('/', response_model=schemas.Employee, status_code=status.HTTP_201_CREATED)
def create_Employee(e: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud_employee.create_employee(db, e)


# /job?job_status=false
@router.get('/', response_model=List[schemas.Employee] or List[schemas.EmployeeFull] or [])
def read_emplyees(job_status: Optional[bool] = None, db: Session = Depends(get_db)):
    if job_status != None:
        return crud_employee.get_emplyees_by_job_status(db, job_status)
    return crud_employee.get_employees(db)



@router.get('/{employee_id}', response_model=schemas.EmployeeFull)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    return crud_employee.get_employee(db, employee_id)
