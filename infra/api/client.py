from dataclasses import dataclass
from enum import Enum

import requests


class AlpacaEndpoint(str, Enum):
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


@dataclass
class AlpacaApiClient(ApiClient):
    key: str
    secret: str

    @property
    def header_alpaca(self):
        return {
            "APCA-API-KEY-ID": self.key,
            "APCA-API-SECRET-KEY": self.secret
        }

    def get_as_alpaca(self, endpoint: AlpacaEndpoint, query: dict) -> ApiSnapshot:
        return self.get(endpoint.value, query)
