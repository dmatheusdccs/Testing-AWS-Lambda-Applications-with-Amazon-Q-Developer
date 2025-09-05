# tests/test_env_fixture.py
import os

def test_mock_table_name(mock_table_name):
    # Revisar que la variable de entorno se haya seteado
    assert os.getenv("TABLE_NAME") == "mock-table"
