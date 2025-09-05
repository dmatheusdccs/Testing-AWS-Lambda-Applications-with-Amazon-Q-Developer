# src/models.py
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class EmploymentType(Enum):
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    CONTRACT = "CONTRACT"
    INTERN = "INTERN"

@dataclass
class Salary:
    amount: float
    currency: str

@dataclass
class JobPosting:
    id: str
    title: str
    description: str
    salary: Salary
    location: str
    company: str
    employment_type: EmploymentType
    application_deadline: datetime
