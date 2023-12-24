from dataclasses import dataclass, asdict

import requests


@dataclass
class ApiQuery:
    def to_params(self) -> dict:
        """
        Noneを除いた自身の要素を辞書化する
        """
        return {k: v for k, v in asdict(self).items() if v is not None}


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
