from concurrent.futures import ProcessPoolExecutor
from typing import List, Any

from psycopg2 import connect
from dataclasses import dataclass

@dataclass
class PsqlClient:
    url: str
    n_max_worker: int = 8

    def transact(self, f, *args, **kwargs):
        conn = connect(self.url)
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

    def calc_optimum_process_num(self, tasks: list) -> int:
        return min(len(tasks), self.n_max_worker)
    
    def execute(self, query: str) -> Any:
        """
        単発のクエリを実行し、結果を取得する。
        結果を返さないタイプのクエリの場合はNoneを返す。
        """
        def _f(_cur, query):
            _cur.execute(query)
            if _cur.description is not None:
                # 結果を返すクエリの場合
                return _cur.fetchall()
            # 結果を返さないクエリの場合
            return None
        return self.transact(_f, query)

    def execute_queries(self, queries: List[str]):
        def _f(_cur, queries):
            for query in queries:
                _cur.execute(query)
        self.transact(_f, queries)

    def executemany(self, query: str, data: list):
        def _f(_cur, query, data):
            _cur.executemany(query, data)
        self.transact(_f, query, data)

    def parallel_execute(self, queries: List[str]):
        n_process = self.calc_optimum_process_num(queries)
        with ProcessPoolExecutor(max_workers=n_process) as executor:
            for i in range(n_process):
                chunk = queries[i::n_process]
                executor.submit(self.execute_queries, chunk)

    def parallel_executemany(self, query: str, data: list):
        n_process = self.calc_optimum_process_num(data)
        with ProcessPoolExecutor(max_workers=n_process) as executor:
            for i in range(n_process):
                chunk = data[i::n_process]
                executor.submit(self.executemany, query, chunk)