from dataclasses import dataclass

from infra.api.interface import ApiQuery, ApiSnapshot

from .cli import AlpacaApiClient


@dataclass
class QueryBar(ApiQuery):
    symbol: str
    timeframe: str
    start: str
    end: str
    limit: int = 10000
    adjustment: str = 'raw'
    asof: str = None
    feed: str = 'iex'
    currency: str = None
    page_token: str = None
    sort: str = 'asc'


@dataclass
class AlpacaBarClient(AlpacaApiClient):
    BAR = 'https://data.alpaca.markets/v2/stocks/bars'

    def get_bar(self, query: QueryBar) -> ApiSnapshot:
        return self.get_as_alpaca(self.BAR, query.to_params())
