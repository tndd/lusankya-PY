from enum import Enum
from os.path import abspath, dirname


class Schema(str, Enum):
    DATAFLOW = "dataflow"
    ALPACA = "alpaca"


class Command(str, Enum):
    SELECT = "select"
    INSERT = "insert"
    UPDATE = "update"
    DELETE = "delete"
    CREATE = "create"
    DROP = "drop"


def load_query(schema: Schema, command: Command, name: str) -> str:
    current_dir = dirname(abspath(__file__))

    with open(f'{current_dir}/{schema.value}/{command.value}/{name}.sql', 'r') as file:
        query = file.read()
    return query
