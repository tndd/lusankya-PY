from domain.dataflow.repository.apiflow import ApiFlowRepository


def kickstart_apiflow(rp_apiflow: ApiFlowRepository):
    """
    未実行あるいは失敗したAPIを実行する
    """
    api_requests = rp_apiflow.fetch_requests_not_executed_or_failed()
    pass