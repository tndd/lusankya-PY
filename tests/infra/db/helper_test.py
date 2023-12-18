from infra.db.sql.helper import Command, Schema, load_query


def test_load_query():
    query = load_query(Schema.DATAFLOW, Command.CREATE, 'schema_dataflow')
    assert query == 'CREATE SCHEMA dataflow AUTHORIZATION postgres;'