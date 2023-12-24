from infra.api.alpaca.bar import AlpacaBarClient, QueryBar
from infra.api.client import ApiSnapshot


def chain_requests_bar(cli: AlpacaBarClient, query: QueryBar):
    while True:
        snapshot: ApiSnapshot = cli.get_bar(query)
        # snapshotの結果をScheduleとResponseの両方に保存
        # TODO: 保存処理
        if not 'next_page_token' in snapshot.r_body:
            break # 次のページがない場合は終了
        # query_barのnext_page_tokenを更新して再実行
        query.page_token = snapshot.r_body['next_page_token']
