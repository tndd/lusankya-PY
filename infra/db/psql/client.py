from concurrent.futures import ProcessPoolExecutor
from typing import List

from psycopg2 import connect, sql
from os import getenv


def transact(f):
    def _wrapper(*args, **kwargs):
        conn = connect(getenv('PSQL_URL'))
        cur = conn.cursor()
        try:
            return f(cur, *args, **kwargs)
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            conn.close()
    return _wrapper


@transact
def execute_queries(_cur, queries: List[str]):
    """
    _curはtransactデコレータ内で作成されたものが渡されるため、
    この関数の実行時に_curを渡す必要はなく、queriesのみ渡せば良い。
    """
    for query in queries:
        _cur.execute(sql.SQL(query))


def parallel_execute(queries: List[str], n_max_worker: int = 8):
    n_query = len(queries)
    n_process = min(n_query, n_max_worker)
    with ProcessPoolExecutor(max_workers=n_process) as executor:
        for i in range(n_process):
            chunk = queries[i::n_process]
            executor.submit(execute_queries, chunk)
