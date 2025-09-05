# src/lambda_function.py
import boto3

def lambda_handler(event, context=None):
    """
    Lambda handler that stores and retrieves an item in DynamoDB.
    Expects event = {"id": "123", "name": "Alice"}
    """
    # Crear el recurso DynamoDB (en AWS real o con Moto en tests)
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table("Users")

    # Insertar el ítem en la tabla
    table.put_item(Item=event)

    # Recuperar el ítem usando la clave primaria "id"
    response = table.get_item(Key={"id": event["id"]})

    return response.get("Item")
