from dataclasses import dataclass

from domain.dataflow.api.repository.alpaca import AlpacaApiflowRepository
from domain.dataset.repository.asset import AssetRepository
from domain.dataset.value.asset_tag import AssetTag
from infra.api.alpaca.bar import AlpacaApiClient


@dataclass
class BarRepository:
    api_cli_bar: AlpacaApiClient
    repo_asset: AssetRepository
    repo_alpaca_apiflow: AlpacaApiflowRepository

    def update_dataset(self):
        """
        自身のDBに保存されているBarデータを最新のものに更新する
        """
        pass

    def update_dataset_of_asset_tag(self, tag: AssetTag):
        """
        特定AssetTagのBarデータのみを最新のものに更新する
        """
        pass

    def update_dataset_of_symbol(self, symbol: str, time_to: str = '2023-12-29'):
        """
        特定SymbolのBarデータのみを最新のものに更新する
        """
        pass