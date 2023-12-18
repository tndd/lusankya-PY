from dataclasses import dataclass
from enum import Enum

from infra.api.client import ApiClient, ApiSnapshot


class AlpacaEndpoint(str, Enum):
    ASSET = 'https://broker-api.sandbox.alpaca.markets/v1/assets'
    BAR = 'https://data.alpaca.markets/v2/stocks/bars'


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
        return self.get(endpoint.value, query, self.header_alpaca)