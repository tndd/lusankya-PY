from dataclasses import dataclass

from domain.dataflow.api.repository.alpaca import AlpacaApiflowRepository
from domain.dataset.repository import AssetRepository
from domain.dataset.value import Adjustment, AssetTag, TimeFrame
from infra.api.alpaca.bar import AlpacaApiClient, QueryBar


@dataclass
class BarRepository:
    rp_asset: AssetRepository
    rp_alpaca_apiflow: AlpacaApiflowRepository

    def load_from_apiflow(self):
        """
        ApiFlowの正常完了かつ未移動のAPIリクエスト結果すべてをBarテーブルに保存する

        サービスじみた挙動をしているが、
        単純な動作ではあることとBarテーブルへの情報の保存行為、
        何よりトランザクション処理の必要性によりリポジトリとして実装する妥協をしている。
        """
        # TODO
        # 正常完了かつデータ未移動であるAPIリクエストの結果を全て取得
        # 各リクエストの結果のbodyをbarテーブル形式に変換し保存
        #   - リクエストごとに並列処理
        # 　- bodyの移行と移動元bodyの削除はトランザクション処理する
        pass

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