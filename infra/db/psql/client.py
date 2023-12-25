from concurrent.futures import ProcessPoolExecutor
from typing import List, Tuple

from psycopg2 import connect, sql
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

    def execute(self, queries: List[str]):
        def _f(_cur, queries):
            for query in queries:
                _cur.execute(sql.SQL(query))
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
                executor.submit(self.execute, chunk)

    def parallel_executemany(self, query: str, data: list):
        n_process = self.calc_optimum_process_num(data)
        with ProcessPoolExecutor(max_workers=n_process) as executor:
            for i in range(n_process):
                chunk = data[i::n_process]
                executor.submit(self.executemany, query, chunk)