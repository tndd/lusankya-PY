from dataclasses import dataclass

from infra.api.model import ApiSnapshot
from infra.api.service import rq_get


@dataclass
class AlpacaApiClient():
    key: str
    secret: str

    @property
    def header_alpaca(self):
        return {
            "APCA-API-KEY-ID": self.key,
            "APCA-API-SECRET-KEY": self.secret
        }

    def get_as_alpaca(self, endpoint: str, params: dict) -> ApiSnapshot:
        return rq_get(endpoint, params, self.header_alpaca)