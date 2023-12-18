from dotenv import load_dotenv

from infra.db.psql.client import PsqlClient
from infra.db.psql.migrate import migrate
from tests.conftest import psql_client

load_dotenv()


def test_migrate(psql_client: PsqlClient):
    migrate(psql_client)
