from domain.dataflow.api.adapter.api_result import \
    snapshot_to_request_and_response
from domain.dataflow.api.model import ApiRequest, ApiResponse
from domain.dataflow.api.repository import ApiFlowRepository
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
        rq, rp = snapshot_to_request_and_response(snapshot)
        rp_api_flow.store_api_request(rq)
        rp_api_flow.store_api_response(rp)
        # 次のページがない場合は終了
        if not 'next_page_token' in snapshot.r_body:
            break
        # query_barのnext_page_tokenを更新して再実行
        query.page_token = snapshot.r_body['next_page_token']