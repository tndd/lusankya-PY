from typing import List

from domain.dataflow.api.model.api_request import ApiRequest

from .apiflow import ApiFlowRepository


class AlpacaApiflowRepository(ApiFlowRepository):
    def fetch_bar_requests_not_executed_or_failed(self) -> List[ApiRequest]:
        """
        未実行あるいは失敗したbarのAPIリクエストのリストを取得する

        これにより取得されるリクエスト情報は、いずれも実行されるべきものである。
        """
        pass