# AWS Lambda Testing with DynamoDB and Amazon Q Developer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-5A5A5A?style=for-the-badge&logo=pytest&logoColor=white)
![Amazon Q Developer](https://img.shields.io/badge/Amazon%20Q-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![DynamoDB](https://img.shields.io/badge/DynamoDB-4053D6?style=for-the-badge&logo=amazondynamodb&logoColor=white)
![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-FF9900?style=for-the-badge&logo=aws-lambda&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

---

## Project Overview

This project demonstrates a professional approach to testing AWS Lambda functions with Python, DynamoDB, and Amazon Q Developer.


## Automated testing is crucial to ensure:

    - **Reliability:** Applications work as intended.  
    - **Maintainability:** Changes do not break existing functionality.  
    - **Documentation:** Tests serve as live documentation.  


In this project, we:

1. Implemented "save_to_dynamodb_table" to store "JobPosting" objects to DynamoDB.  
2. Created **sample data** and **fixtures** for testing.  
3. Used **Moto** to mock DynamoDB (no real AWS resources are affected).  
4. Refactored tests to be **descriptive, independent, and maintainable**.  
5. Leveraged **Amazon Q Developer** to identify test scenarios, generate tests, and improve code quality.

Reference: [AWS DevOps & Developer Productivity Blog — “Testing your applications with Amazon Q Developer,” July 29, 2024”](https://aws.amazon.com/blogs/devops/testing-your-applications-with-amazon-q-developer/)

---

## Project Structure

project/
├─ src/
│ 	├─ models.py
│ 	├─ save_to_dynamodb.py
├─ tests/
│ 	├─ conftest.py
│ 	├─ test_save_to_dynamodb.py
├─ README.md




- **src/models.py** – Defines `JobPosting`, `Salary`, `EmploymentType`.  
- **src/save_to_dynamodb.py** – Function to save job postings to DynamoDB.  
- **tests/conftest.py** – Fixtures for environment variables and mock data.  
- **tests/test_save_to_dynamodb.py** – Unit tests using `pytest` and `Moto`.  

---


## Installation

1. Clone the repository:

   git clone <your-repo-url>
   cd <project-folder>

2. Install dependencies:

   pip install -r requirements.txt


3. Running Tests

   Run all tests:

	pytest -q

4. Run a specific test file:

   pytest -q tests/test_save_to_dynamodb.py

5. Generate coverage report:

   pytest --cov=src tests/



## Sample Fixture and Data

```python
import os
import pytest
from datetime import datetime
from src.models import JobPosting, Salary, EmploymentType

@pytest.fixture
def mock_table_name():
    os.environ["TABLE_NAME"] = "mock-table"
    yield
    del os.environ["TABLE_NAME"]

job_posting = JobPosting(
    id="123e4567-e89b-12d3-a456-426655440000",
    title="Software Engineer",
    description="Build web applications using Python and Django.",
    salary=Salary(amount=100000, currency="USD"),
    location="Remote",
    company="Acme Corp",
    employment_type=EmploymentType.FULL_TIME,
    application_deadline=datetime(2023, 1, 15)
)


## Using Moto to Mock DynamoDB

```python
from moto import mock_dynamodb2
import boto3
from src.save_to_dynamodb import save_to_dynamodb_table

@mock_dynamodb2
def test_save_to_dynamodb_table(mock_table_name):
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.create_table(
        TableName="mock-table",
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )
    
    save_to_dynamodb_table(job_posting)
    
    item = table.get_item(Key={"id": job_posting.id})["Item"]
    assert item["title"] == job_posting.title

> **Note:** All tests run against a mocked DynamoDB. No real AWS resources are affected.


## Benefits of Amazon Q Developer

   - Learning & Guidance: Explains testing concepts interactively.
   - Scenario Identification: Suggests unit test scenarios, including edge cases.
   - Test Generation & Refactoring: Generates and refactors unit tests for clarity.
   - Dependency Mocking: Provides guidance on mocking external services.
   - Improved Code Quality: Reduces human error and accelerates development.


## Try It Yourself


   1. Ensure Python 3.11+ is installed.
   2. Install dependencies: pip install -r requirements.txt
   3. Run tests: pytest -q
   4. Modify or add new JobPosting test cases.
   5. Observe results in the terminal or generate coverage report.



## Best Practices Implemented

   - Independent tests: No reliance on global state.
   - Fixtures for setup/teardown: Environment variables and sample data.
   - Descriptive test names: Clearly indicate purpose.
   - Complete assertions: All relevant properties verified.
   - Mocking external dependencies: DynamoDB is mocked with Moto.


## Conclusion

   This project demonstrates a professional workflow for testing serverless Python applications:

   - Mocked DynamoDB tables with Moto.
   - Fixtures for reliable setup and teardown.
   - Descriptive, maintainable, and independent tests.
   - Full integration with Amazon Q Developer to accelerate and improve test writing.

It is ready to be extended with additional features or serve as an educational example for testing AWS Lambda functions.
