# tests/test_save_to_dynamodb.py
from datetime import datetime
import boto3
from moto import mock_aws

from src.models import JobPosting, Salary, EmploymentType
from src.save_to_dynamodb import save_to_dynamodb_table


# --- sample data (igual que en Paso 2) ---
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


@mock_aws
def test_save_to_dynamodb_table(mock_table_name):
    """
    1) Usa la fixture mock_table_name para setear TABLE_NAME = 'mock-table'.
    2) Crea una tabla DynamoDB mock con el mismo nombre.
    3) Llama a save_to_dynamodb_table(job_posting).
    4) Recupera el item de la tabla y valida los campos.
    """
    # 1) recurso DynamoDB mock
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

    # 2) crear la tabla mock
    table = dynamodb.create_table(
        TableName="mock-table",
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )
    table.meta.client.get_waiter("table_exists").wait(TableName="mock-table")

    # 3) invocar la función que guarda el job_posting
    save_to_dynamodb_table(job_posting)

    # 4) leer el item guardado
    response = table.get_item(Key={"id": job_posting.id})
    item = response.get("Item")
    assert item is not None

    # Validaciones clave (ajusta si serialización difiere)
    assert item["id"] == "123e4567-e89b-12d3-a456-426655440000"
    assert item["title"] == "Software Engineer"
    assert item["description"] == "Build web applications using Python and Django."
    assert item["salary"] == {"amount": 100000, "currency": "USD"}
    assert item["location"] == "Remote"
    assert item["company"] == "Acme Corp"

    # Dependiendo de cómo se realize EmploymentType:
    # puede ser "Full Time" o EmploymentType.FULL_TIME.value
    assert item["employment_type"] in ["Full Time", EmploymentType.FULL_TIME.value]
