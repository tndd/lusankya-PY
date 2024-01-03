import json

from domain.dataflow.adapter.api_result import api_result_from_snapshot
from domain.dataflow.repository.apiflow import ApiFlowRepository
from infra.api.alpaca.bar import AlpacaBarClient, QueryBar
from infra.api.interface import ApiSnapshot


def store_chain_requests_bar(
    api_cli_bar: AlpacaBarClient,
    rp_api_flow: ApiFlowRepository,
    query: QueryBar
):
    """
    AlpacaのBarデータをトークンを辿って取得し、結果の保存を行う
    """
    while True:
        # データ取得
        snapshot: ApiSnapshot = api_cli_bar.get_bar(query)
        # snapshotの結果を変換し保存
        api_result = api_result_from_snapshot(snapshot)
        rp_api_flow.store_api_result(api_result)
        # 次のページがない場合は終了
        if not 'next_page_token' in snapshot.r_body:
            break
        # query_barのnext_page_tokenを更新して再実行
        body = json.loads(snapshot.r_body) # [Note]: r_bodyは文字列型なのでjson.loadsで辞書型に変換する
        query.page_token = body['next_page_token']
