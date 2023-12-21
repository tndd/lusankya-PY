from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from typing import List

from psycopg2 import connect, sql


@dataclass
class PsqlClient:
    url: str

    def transact_execute(self, queries: List[str]):
        conn = connect(self.url)
        cur = conn.cursor()
        try:
            for query in queries:
                cur.execute(sql.SQL(query))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            conn.close()

    def parallel_execute(self, queries: List[str], n_max_worker: int = 8):
        n_query = len(queries)
        n_process = min(n_query, n_max_worker)
        with ProcessPoolExecutor(max_workers=n_process) as executor:
            for i in range(n_process):
                chunk = queries[i::n_process]
                executor.submit(self.transact_execute, chunk)
