from domain.dataflow.api.model import ApiResponse
from infra.api.client import ApiSnapshot


def api_response_to_params(api_response: ApiResponse) -> dict:
    return {
        'id': api_response._id,
        'time_stamp': api_response.time_stamp,
        'api_request_id': api_response.api_request_id,
        'status': api_response.status,
        'resp_header': api_response.header,
        'body': api_response.body,
    }


def api_response_from_rows(params: list) -> ApiResponse:
    return ApiResponse(
        _id=params[0],
        time_stamp=params[1],
        api_request_id=params[2],
        status=params[3],
        header=params[4],
        body=params[5]
    )


def api_response_from_snapshot(snapshot: ApiSnapshot, api_request_id: str) -> ApiResponse:
    return ApiResponse(
        api_request_id=api_request_id,
        status=snapshot.r_status,
        header=snapshot.r_header,
        body=snapshot.r_body
    )