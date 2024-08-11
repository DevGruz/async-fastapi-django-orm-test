from asgiref.sync import sync_to_async

from models import EndpointStates, ClientInfo
from schemas import FilterSchema, ResultSchema
from utils import datetime_to_unix_microseconds


@sync_to_async
def get_filtered_data(filter_schema: FilterSchema) -> ResultSchema:
    state_start_unix_microseconds = datetime_to_unix_microseconds(filter_schema.input_start)

    endpoints = EndpointStates.objects.filter(
        state_start__gte=state_start_unix_microseconds,
        endpoint_id=139
    ).order_by('-state_start')

    endpoints = [endpoint for endpoint in endpoints if endpoint.id % 3 == 0]

    if len(endpoints) < 3:
        return ResultSchema(
            filtered_count=len(endpoints),
            client_info=None,
            state_id=None,
        )

    third_endpoint = endpoints[2]
    client_info = ClientInfo.objects.get(pk=third_endpoint.client.client_info.id).info

    return ResultSchema(
        filtered_count=len(endpoints),
        client_info=client_info,
        state_id=third_endpoint.state_id,
    )
