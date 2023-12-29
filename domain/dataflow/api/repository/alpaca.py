from domain.dataflow.api.repository import ApiFlowRepository
from infra.api.alpaca.bar import AlpacaBarClient, QueryBar
from infra.api.client import ApiSnapshot


class AlpacaDataflowRepository:
    api_cli_bar: AlpacaBarClient
    api_flow_repo: ApiFlowRepository

    def store_chain_requests_bar(self, query: QueryBar):
        """
        AlpacaのBarデータをトークンを辿って取得し、結果の保存を行う
        """
        while True:
            # データ取得
            snapshot: ApiSnapshot = self.api_cli_bar.get_bar(query)
            # snapshotの結果をScheduleとResponseの両方に保存
            self.api_flow_repo.store_api_snapshot(snapshot)
            if not 'next_page_token' in snapshot.r_body:
                break # 次のページがない場合は終了
            # query_barのnext_page_tokenを更新して再実行
            query.page_token = snapshot.r_body['next_page_token']

    def kickstart(self):
        """
        未実行あるいは失敗したAPIを実行する
        """
        pass
