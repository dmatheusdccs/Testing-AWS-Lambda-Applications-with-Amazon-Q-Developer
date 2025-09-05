import os
import pytest
from moto import mock_aws
import boto3

# ----------------------------
# Fixture 1: Mock DynamoDB
# ----------------------------
@pytest.fixture(scope="function")
def dynamodb_table():
    """
    Fixture that sets up a mocked DynamoDB table before each test
    and tears it down after.
    """
    with mock_aws(config={"dynamodb": {"use_docker": False}}):
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
        table = dynamodb.create_table(
            TableName="Users",
            KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        # Esperar a que la tabla esté activa
        table.meta.client.get_waiter("table_exists").wait(TableName="Users")
        yield table

# ----------------------------
# Fixture 2: TABLE_NAME (para Lambda)
# ----------------------------
@pytest.fixture(scope="function")
def table_name_env():
    """
    Fixture to temporarily set TABLE_NAME environment variable to 'Users'
    """
    original_value = os.environ.get("TABLE_NAME")
    os.environ["TABLE_NAME"] = "Users"
    yield "Users"
    if original_value is not None:
        os.environ["TABLE_NAME"] = original_value
    else:
        del os.environ["TABLE_NAME"]

# ----------------------------
# Fixture 3: mock_table_name (ejemplo rápido)
# ----------------------------
@pytest.fixture
def mock_table_name():
    """
    Fixture to temporarily set TABLE_NAME to 'mock-table' for testing.
    """
    original_value = os.environ.get("TABLE_NAME")
    os.environ["TABLE_NAME"] = "mock-table"
    yield "mock-table"
    if original_value is not None:
        os.environ["TABLE_NAME"] = original_value
    else:
        del os.environ["TABLE_NAME"]
