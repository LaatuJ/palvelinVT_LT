from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean

from .database import Base


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    job = relationship('Job')


class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    job_done = Column(Boolean, default=False, nullable=False)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=True)

    employee = relationship('Employee', back_populates='job')



