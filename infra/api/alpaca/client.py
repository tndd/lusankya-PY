from dataclasses import dataclass
from enum import Enum

import requests


class Endpoint(str, Enum):
    ASSET = 'https://broker-api.sandbox.alpaca.markets/v1/assets'
    BAR = "https://data.alpaca.markets/v2/stocks/bars"


@dataclass
class ApiSnapshot:
    endpoint: str
    query: dict
    header: dict
    r_status: int
    r_header: dict
    r_body: str


@dataclass
class AlpacaApiClient:
    key: str
    secret: str

    @property
    def header(self):
        return {
            "APCA-API-KEY-ID": self.key,
            "APCA-API-SECRET-KEY": self.secret
        }

    def get(self, url: str, query: dict) -> ApiSnapshot:
        r = requests.get(url, params=query, headers=self.header)
        return ApiSnapshot(
            url,
            query,
            self.header,
            r.status_code,
            dict(r.headers),
            r.text
        )
