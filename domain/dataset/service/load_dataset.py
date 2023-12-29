from domain.dataflow.api.repository.alpaca import AlpacaApiflowRepository
from domain.dataset.repository import BarRepository


def load_bar_dataset_from_apiflow(
    rp_bar: BarRepository,
    rp_alpaca_apiflow: AlpacaApiflowRepository,
):
    """
    ApiFlowの正常完了かつ未移動のAPIリクエスト結果すべてをBarテーブルに保存する
    """
    # TODO
    # 正常完了かつデータ未移動であるAPIリクエストの結果を全て取得
    # 各リクエストの結果のbodyをbarテーブル形式に変換し保存
    #   - リクエストごとに並列処理
    # 　- bodyの移行と移動元bodyの削除はトランザクション処理する
    pass