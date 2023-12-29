from dataclasses import dataclass

from domain.dataflow.api.repository.alpaca import AlpacaApiflowRepository
from domain.dataset.repository import AssetRepository
from domain.dataset.value import Adjustment, TimeFrame


@dataclass
class BarRepository:
    rp_asset: AssetRepository

    def fetch_latest_timestamp_of_symbol(
            self,
            symbol: str,
            timeframe: TimeFrame,
            adjustment: Adjustment,
        ) -> str:
        """
        特定Symbolの最新のBarデータのタイムスタンプを取得する
        出力はRFC-3339 or YYYY-MM-DD形式で返される
        """
        # TODO: 仮実装。DBに値が無ければ2000-01-01を返す
        return "2000-01-01"