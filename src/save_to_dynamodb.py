# src/save_to_dynamodb.py
import boto3
import os
from datetime import datetime
from enum import Enum

def to_dict(obj):
    """
    Convierte un objeto en un dict válido para DynamoDB:
    - Si es un objeto con __dict__, convierte sus atributos recursivamente.
    - Si es Enum, devuelve su valor (string).
    - Si es datetime, lo convierte a ISO 8601 string.
    - Si es lista o dict, procesa sus elementos recursivamente.
    - Caso contrario, lo devuelve tal cual.
    """
    if isinstance(obj, Enum):
        return obj.value
    elif isinstance(obj, datetime):
        return obj.isoformat()
    elif hasattr(obj, "__dict__"):
        return {k: to_dict(v) for k, v in obj.__dict__.items()}
    elif isinstance(obj, list):
        return [to_dict(v) for v in obj]
    elif isinstance(obj, dict):
        return {k: to_dict(v) for k, v in obj.items()}
    else:
        return obj

def save_to_dynamodb_table(item, table_name=None):
    """
    Guarda un item en DynamoDB. Si no se pasa table_name,
    se usa la variable de entorno TABLE_NAME.
    Convierte objetos complejos en dict válido.
    """
    if table_name is None:
        table_name = os.environ.get("TABLE_NAME", "JobPostings")

    # Convertimos cualquier objeto en dict antes de guardar
    item_dict = to_dict(item)

    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table(table_name)
    table.put_item(Item=item_dict)
