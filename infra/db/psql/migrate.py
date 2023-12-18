from typing import List

from infra.db.psql.client import PsqlClient
from infra.db.psql.query.helper import Command, Schema, load_query


def migrate(cli: PsqlClient):
    q = queries_schema() + queries_table() + queries_view()
    cli.transact_execute(q)


def queries_schema() -> List[str]:
    q_schema_alpaca = load_query(Schema.DATAFLOW, Command.CREATE, 'schema_dataflow')
    q_schema_dataflow = load_query(Schema.ALPACA, Command.CREATE, 'schema_alpaca')
    return [
        q_schema_dataflow,
        q_schema_alpaca
    ]

def queries_table() -> List[str]:
    # dataflow
    q_table_api_schedule = load_query(Schema.DATAFLOW, Command.CREATE, 'table_api_schedule')
    q_table_api_snapshot = load_query(Schema.DATAFLOW, Command.CREATE, 'table_api_snapshot')
    q_table_api_query_schedule = load_query(Schema.DATAFLOW, Command.CREATE, 'table_api_query_schedule')
    return [
        q_table_api_schedule,
        q_table_api_snapshot,
        q_table_api_query_schedule
    ]

def queries_view() -> List[str]:
    q_view_latest_api_snapshot = load_query(Schema.DATAFLOW, Command.CREATE, 'view_latest_api_snapshot')
    return [
        q_view_latest_api_snapshot,
    ]
