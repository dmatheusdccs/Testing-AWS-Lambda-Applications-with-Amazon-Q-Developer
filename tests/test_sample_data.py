# tests/test_sample_data.py
from datetime import datetime
from src.models import JobPosting, Salary, EmploymentType

def test_create_job_posting():
    job_posting = JobPosting(
        id="123e4567-e89b-12d3-a456-426655440000",
        title="Software Engineer",
        description="Build web applications using Python and Django",
        salary=Salary(amount=100000, currency="USD"),
        location="Remote",
        company="Acme Corp",
        employment_type=EmploymentType.FULL_TIME,
        application_deadline=datetime(2023, 1, 15)
    )

    assert job_posting.title == "Software Engineer"
    assert job_posting.salary.amount == 100000
    assert job_posting.employment_type == EmploymentType.FULL_TIME
