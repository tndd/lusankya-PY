import os

import pytest

from infra.db.psql.client import PsqlClient


@pytest.fixture
def psql_client() -> PsqlClient:
    return PsqlClient(url=os.getenv('PSQL_URL_TEST'))
