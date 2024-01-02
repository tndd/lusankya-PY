from infra.api.interface import ApiSnapshot

from ..model import ApiRequest


def api_request_to_params(api_request: ApiRequest) -> dict:
    return {
        'id': api_request._id,
        'time_stamp': api_request.time_stamp,
        'endpoint': api_request.endpoint,
        'params': api_request.params,
        'req_header': api_request.header,
    }


def api_request_from_row(params: list) -> ApiRequest:
    return ApiRequest(
        _id=params[0],
        time_stamp=params[1],
        endpoint=params[2],
        params=params[3],
        header=params[4]
    )


def api_request_from_snapshot(snapshot: ApiSnapshot) -> ApiRequest:
    return ApiRequest(
        endpoint=snapshot.endpoint,
        params=snapshot.query,
        header=snapshot.header
    )