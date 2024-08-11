from datetime import datetime


def datetime_to_unix_microseconds(dt: datetime) -> int:
    timestamp_seconds = dt.timestamp()
    timestamp_microseconds = int(timestamp_seconds * 1_000)
    return timestamp_microseconds
