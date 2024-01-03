from domain.dataflow.model import ApiRequest
from infra.adapter.dataflow.api_request import (api_request_from_row,
                                                api_request_from_snapshot,
                                                api_request_to_params)
from infra.api.model import ApiSnapshot


def test_api_api_request_from_row():
    pass


def test_api_request_to_params():
    ENDPOINT = 'https://api.alpaca.markets/v2/assets'
    PARAMS = {
        'query_01': 'query_01_value',
        'query_02': 'query_02_value'
    }
    HEADER = {
        'header_01': 'header_01_value',
        'header_02': 'header_02_value'
    }
    api_request = ApiRequest(
        endpoint=ENDPOINT,
        params=PARAMS,
        header=HEADER
    )
    params: dict = api_request_to_params(api_request)
    assert params['endpoint'] == ENDPOINT
    assert params['params'] == PARAMS
    assert params['req_header'] == HEADER


def test_api_request_from_snapshot():
    ENDPOINT = 'https://api.alpaca.markets/v2/assets'
    PARAMS = {
        'query_01': 'query_01_value',
        'query_02': 'query_02_value'
    }
    HEADER = {
        'header_01': 'header_01_value',
        'header_02': 'header_02_value'
    }
    snapshot = ApiSnapshot(
        endpoint=ENDPOINT,
        query=PARAMS,
        header=HEADER,
        r_status=200,
        r_header={},
        r_body='body'
    )
    api_request: ApiRequest = api_request_from_snapshot(snapshot)
    assert api_request.endpoint == ENDPOINT
    assert api_request.params == PARAMS
    assert api_request.header == HEADER