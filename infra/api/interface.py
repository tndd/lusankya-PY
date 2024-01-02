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


class ApiQuery:
    def to_params(self) -> dict:
        """
        Noneを除いた自身の要素を辞書化する
        """
        return {k: v for k, v in self.__dict__.items() if v is not None}


def rq_get(endpoint: str, params: dict, header: dict) -> ApiSnapshot:
    r = requests.get(url=endpoint, params=params, headers=header)
    return ApiSnapshot(
        endpoint,
        params,
        header,
        r.status_code,
        dict(r.headers),
        r.text
    )
