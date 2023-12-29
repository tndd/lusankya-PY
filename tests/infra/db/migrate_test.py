from dotenv import load_dotenv

from infra.db.client import PsqlClient
from infra.db.migrate import (migrate, queries_extension, queries_schema,
                              queries_table, queries_view)
from tests.conftest import psql_client

load_dotenv()


def test_queries_extension():
    result = queries_extension()
    assert isinstance(result, list)


def test_queries_schema():
    result = queries_schema()
    assert isinstance(result, list)


def test_queries_table():
    result = queries_table()
    assert isinstance(result, list)


def test_queries_view():
    result = queries_view()
    assert isinstance(result, list)


def test_migrate(psql_client: PsqlClient):
    migrate(psql_client)
