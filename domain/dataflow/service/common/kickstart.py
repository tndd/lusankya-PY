from domain.dataflow.repository.apiflow import ApiFlowRepository


def kickstart_apiflow(rp_apiflow: ApiFlowRepository):
    """
    全エンドポイントの未実行あるいは失敗したAPIを無差別に実行する
    """
    api_requests = rp_apiflow.fetch_requests_not_executed_or_failed()
    pass