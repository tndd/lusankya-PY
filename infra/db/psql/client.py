from concurrent.futures import ProcessPoolExecutor
from typing import List

from psycopg2 import connect, sql
from os import getenv


def transact(f):
    """
    概要:
        データベースへの接続およびトランザクション処理をラップするデコレータ。

    Note:
        このデコレータを適用した関数には、自動的に第一引数にcursorオブジェクトが渡される。
        そのためデコレータ適用先の関数呼び出しの際、引数にはcursorオブジェクトを渡す必要はない。
        適用先関数だけ見れば、どこから_curが発生したのか分からなくなるので注意。
    """
    def _wrapper(*args, **kwargs):
        conn = connect(getenv('PSQL_URL'))
        cur = conn.cursor()
        try:
            result = f(cur, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            conn.close()
    return _wrapper


@transact
def execute_queries(_cur, queries: List[str]):
    for query in queries:
        _cur.execute(sql.SQL(query))


@transact
def execute_many(_cur, query: str, data: List[tuple]):
    _cur.executemany(query, data)


def parallel_execute(queries: List[str], n_max_worker: int = 8):
    n_query = len(queries)
    n_process = min(n_query, n_max_worker)
    with ProcessPoolExecutor(max_workers=n_process) as executor:
        for i in range(n_process):
            chunk = queries[i::n_process]
            executor.submit(execute_queries, chunk)


def parallel_executemany(query: str, data: List(tuple), n_max_worker: int = 8):
    n_data = len(data)
    n_process = min(n_data, n_max_worker)
    with ProcessPoolExecutor(max_workers=n_process) as executor:
        for i in range(n_process):
            chunk = data[i::n_process]
            executor.submit(execute_many, chunk)