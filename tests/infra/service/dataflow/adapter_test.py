from infra.service.dataflow.adapter import snapshot_to_schedule, snapshot_to_response
from infra.service.dataflow.model import ApiSchedule, ApiResponse
from infra.api.alpaca.cli import ApiSnapshot

def test_snapshot_to_schedule():
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
    api_schedule: ApiSchedule = snapshot_to_schedule(snapshot)
    assert api_schedule.endpoint == ENDPOINT
    assert api_schedule.params == PARAMS
    assert api_schedule.header == HEADER


def test_snapshot_to_response():
    ENDPOINT = 'https://api.alpaca.markets/v2/assets'
    R_STATUS = 200
    R_HEADER = {
        'r_header_01': 'r_header_01_value',
        'r_header_02': 'r_header_02_value'
    }
    BODY = 'BODY'
    snapshot = ApiSnapshot(
        endpoint=ENDPOINT,
        query={},
        header={},
        r_status=R_STATUS,
        r_header=R_HEADER,
        r_body=BODY
    )
    SHCEDULE_ID = '8ad823f6-0a9a-685a-0099-4495034aeb37'
    api_response: ApiResponse = snapshot_to_response(snapshot, SHCEDULE_ID)
    assert api_response.api_schedule_id == SHCEDULE_ID
    assert api_response.status == R_STATUS
    assert api_response.header == R_HEADER
    assert api_response.body == BODY

