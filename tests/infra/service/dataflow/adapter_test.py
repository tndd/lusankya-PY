from infra.service.dataflow.adapter import snapshot_to_schedule, snapshot_to_response
from infra.service.dataflow.model import ApiSchedule, ApiResponse
from infra.api.alpaca.cli import ApiSnapshot

def test_snapshot_to_schedule_and_response():
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
    api_schedule = snapshot_to_schedule(snapshot)
    assert api_schedule.endpoint == ENDPOINT
    assert api_schedule.params == PARAMS
    assert api_schedule.header == HEADER
