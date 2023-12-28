from dataclasses import dataclass

from infra.api.client import ApiClient, ApiSnapshot, ApiQuery


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

    def get_as_alpaca(self, endpoint: str, query: ApiQuery) -> ApiSnapshot:
        return self.get(endpoint, query, self.header_alpaca)