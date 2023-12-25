import os

from dotenv import load_dotenv

from infra.db.psql.client import PsqlClient

load_dotenv()


def test_generate_psql_client():
    assert PsqlClient(url=os.getenv('PSQL_URL_TEST'))


def test_execute():
    psql_cli = PsqlClient(url=os.getenv('PSQL_URL_TEST'))
    queries = ['SELECT 1' for _ in range(4)]
    assert psql_cli.execute(queries) == None


def test_parallel_execute():
    psql_cli = PsqlClient(url=os.getenv('PSQL_URL_TEST'))
    queries = ['SELECT 1' for _ in range(10)]
    assert psql_cli.parallel_execute(queries) == None

def test_parallel_execute_change_worker_num():
    psql_cli = PsqlClient(
        url=os.getenv('PSQL_URL_TEST'),
        n_max_worker=16
    )
    queries = ['SELECT 1' for _ in range(32)]
    assert psql_cli.parallel_execute(queries) == None
