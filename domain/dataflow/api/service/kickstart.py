from domain.dataflow.api.repository.alpaca import AlpacaApiflowRepository


def kickstart_alpaca_apiflow(rp_alpaca_apiflow: AlpacaApiflowRepository):
    """
    未実行あるいは失敗したAPIを実行する
    """
    api_requests = rp_alpaca_apiflow.fetch_bar_requests_not_executed_or_failed()
    pass