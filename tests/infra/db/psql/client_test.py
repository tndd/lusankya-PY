import os

from dotenv import load_dotenv

from infra.db.psql.client import PsqlClient

load_dotenv()


def test_generate_psql_client():
    assert PsqlClient(url=os.getenv('PSQL_URL_TEST'))


def test_execute():
    """
    以下２点の要素を確認する。
    1. 単発のクエリを実行出来ていること
    2. クエリの結果が取得できていること
    """
    psql_cli = PsqlClient(url=os.getenv('PSQL_URL_TEST'))
    assert psql_cli.execute('SELECT 1') == [(1,)]


def test_execute_queries():
    psql_cli = PsqlClient(url=os.getenv('PSQL_URL_TEST'))
    queries = ['SELECT 1' for _ in range(4)]
    assert psql_cli.execute_queries(queries) == None


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


def test_parallel_executemany():
    psql_cli = PsqlClient(url=os.getenv('PSQL_URL_TEST'))
    table_name = 'usksxcdw'
    try:
        # テスト用の一時的なテーブルを作成
        psql_cli.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (column1 varchar(255), column2 varchar(255))")
        # テスト用投入データを作成
        query = f"INSERT INTO {table_name} (column1, column2) VALUES (%s, %s)"
        data = [(f"value1_{i}", f"value2_{i}") for i in range(10)]
        # executemanyの動作確認
        assert psql_cli.executemany(query, data) == None
        # テーブルにデータが入っていることを確認
        rows = psql_cli.execute(f'select * from {table_name}')
        assert len(rows) == 10
    finally:
        # テスト用テーブルは必ず削除しておく
        psql_cli.execute(f"DROP TABLE IF EXISTS {table_name}")
