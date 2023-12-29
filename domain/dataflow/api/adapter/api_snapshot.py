from typing import Tuple

from infra.api.client import ApiSnapshot

from . import ApiRequest, ApiResponse


def snapshot_to_request_and_response(
        snapshot: ApiSnapshot
    ) -> Tuple[ApiRequest, ApiResponse]:
    api_request = ApiRequest(
        endpoint=snapshot.endpoint,
        params=snapshot.query,
        header=snapshot.header
    )
    api_response = ApiResponse(
        api_request_id=api_request._id,
        status=snapshot.r_status,
        header=snapshot.r_header,
        body=snapshot.r_body
    )
    return api_request, api_response
