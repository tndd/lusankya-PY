from domain.dataflow.api.repository.alpaca import AlpacaApiflowRepository
from domain.dataset.repository import AssetRepository, BarRepository
from domain.dataset.value import Adjustment, AssetTag, TimeFrame
from infra.api.alpaca.bar import QueryBar


def update_dataset():
    """
    自身のDBに保存されているBarデータを最新のものに更新する
    """
    pass


def update_dataset_of_asset_tag(tag: AssetTag):
    """
    特定AssetTagのBarデータのみを最新のものに更新する
    """
    pass


def update_dataset_of_symbol(
    rp_asset: AssetRepository,
    rp_alpaca_apiflow: AlpacaApiflowRepository,
    rp_bar: BarRepository,
    symbol: str,
    timeframe: TimeFrame,
    adjustment: Adjustment,
    time_to: str = '2023-12-29',
):
    """
    特定SymbolのBarデータのみを最新のものに更新する
    """
    # 指定symbolの最新タイムスタンプを取得
    time_from = rp_asset.fetch_latest_timestamp_of_symbol(
        symbol=symbol,
        timeframe=timeframe,
        adjustment=adjustment,
    )
    # クエリ作成
    query = QueryBar(
        symbol=symbol,
        timeframe=timeframe.value,
        start=time_from,
        end=time_to,
        adjustment=adjustment.value
    )
    # Barデータの取得し、Apiflowにキャッシュする
    rp_alpaca_apiflow.store_chain_requests_bar(query)
    # 自身のBarテーブルにキャッシュデータを保存する
    rp_bar.load_from_apiflow()