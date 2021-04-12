from pydantic import BaseModel
from typing import List, Optional

from sqlalchemy.sql.expression import null

class FirstCommonBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CommonBase(FirstCommonBase):
    id: int


class Job(CommonBase):
    job_done: Optional[bool]

class Employee(CommonBase):
    pass

class JobFull(Job):
    employee_id: int
    employee: Employee


class EmployeeFull(Employee):
    job: Optional[Job] = None
    class Config:
        orm_mode = True


class JobCreate(FirstCommonBase):
    pass

class EmployeeCreate(FirstCommonBase):
    pass

class JobUpdate(BaseModel):
    job_id: int
    employee_id: Optional[int] = None
    job_done: Optional[bool] = None