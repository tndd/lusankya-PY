from dataclasses import dataclass

import requests


@dataclass
class ApiSnapshot:
    endpoint: str
    query: dict
    header: dict
    r_status: int
    r_header: dict
    r_body: str


class ApiClient:
    def get(self, endpoint: str, query: dict, header: dict) -> ApiSnapshot:
        r = requests.get(url=endpoint, params=query, headers=header)
        return ApiSnapshot(
            endpoint,
            query,
            header,
            r.status_code,
            dict(r.headers),
            r.text
        )
