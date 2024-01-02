from os import getenv

import pytest

from infra.db.client import PsqlClient


@pytest.fixture
def psql_client() -> PsqlClient:
    return PsqlClient(url=getenv('PSQL_URL_TEST', 'NOT_EXIST_ENV'))
