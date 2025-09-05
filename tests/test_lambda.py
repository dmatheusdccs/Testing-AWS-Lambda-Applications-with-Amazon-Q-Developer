# tests/test_lambda.py
import pytest
from src.lambda_function import lambda_handler

def test_lambda_handler_inserts_and_reads_item(dynamodb_table):
    event = {"id": "123", "name": "Alice"}
    response = lambda_handler(event, None)

    assert response == event
    # Verificar que el ítem fue insertado correctamente