from typing_extensions import Literal, TypeAlias

_Key: TypeAlias = bytes | str | memoryview

ADD_CMD: Literal["TS.ADD"]
ALTER_CMD: Literal["TS.ALTER"]
CREATERULE_CMD: Literal["TS.CREATERULE"]
CREATE_CMD: Literal["TS.CREATE"]
DECRBY_CMD: Literal["TS.DECRBY"]
DELETERULE_CMD: Literal["TS.DELETERULE"]
DEL_CMD: Literal["TS.DEL"]
GET_CMD: Literal["TS.GET"]
INCRBY_CMD: Literal["TS.INCRBY"]
INFO_CMD: Literal["TS.INFO"]
MADD_CMD: Literal["TS.MADD"]
MGET_CMD: Literal["TS.MGET"]
MRANGE_CMD: Literal["TS.MRANGE"]
MREVRANGE_CMD: Literal["TS.MREVRANGE"]
QUERYINDEX_CMD: Literal["TS.QUERYINDEX"]
RANGE_CMD: Literal["TS.RANGE"]
REVRANGE_CMD: Literal["TS.REVRANGE"]

class TimeSeriesCommands:
    def create(
        self,
        key: _Key,
        retention_msecs: int | None = ...,
        uncompressed: bool | None = ...,
        labels: dict[str, str] | None = ...,
        chunk_size: int | None = ...,
        duplicate_policy: str | None = ...,
    ): ...
    def alter(
        self,
        key: _Key,
        retention_msecs: int | None = ...,
        labels: dict[str, str] | None = ...,
        chunk_size: int | None = ...,
        duplicate_policy: str | None = ...,
    ): ...
    def add(
        self,
        key: _Key,
        timestamp: int | str,
        value: float,
        retention_msecs: int | None = ...,
        uncompressed: bool | None = ...,
        labels: dict[str, str] | None = ...,
        chunk_size: int | None = ...,
        duplicate_policy: str | None = ...,
    ): ...
    def madd(self, ktv_tuples): ...
    def incrby(
        self,
        key: _Key,
        value: float,
        timestamp: int | str | None = ...,
        retention_msecs: int | None = ...,
        uncompressed: bool | None = ...,
        labels: dict[str, str] | None = ...,
        chunk_size: int | None = ...,
    ): ...
    def decrby(
        self,
        key: _Key,
        value: float,
        timestamp: int | str | None = ...,
        retention_msecs: int | None = ...,
        uncompressed: bool | None = ...,
        labels: dict[str, str] | None = ...,
        chunk_size: int | None = ...,
    ): ...
    def delete(self, key, from_time, to_time): ...
    def createrule(
        self, source_key: _Key, dest_key: _Key, aggregation_type: str, bucket_size_msec: int, align_timestamp: int | None = ...
    ): ...
    def deleterule(self, source_key, dest_key): ...
    def range(
        self,
        key: _Key,
        from_time: int | str,
        to_time: int | str,
        count: int | None = ...,
        aggregation_type: str | None = ...,
        bucket_size_msec: int | None = ...,
        filter_by_ts: list[int] | None = ...,
        filter_by_min_value: int | None = ...,
        filter_by_max_value: int | None = ...,
        align: int | str | None = ...,
        latest: bool | None = ...,
        bucket_timestamp: str | None = ...,
        empty: bool | None = ...,
    ): ...
    def revrange(
        self,
        key: _Key,
        from_time: int | str,
        to_time: int | str,
        count: int | None = ...,
        aggregation_type: str | None = ...,
        bucket_size_msec: int | None = ...,
        filter_by_ts: list[int] | None = ...,
        filter_by_min_value: int | None = ...,
        filter_by_max_value: int | None = ...,
        align: int | str | None = ...,
        latest: bool | None = ...,
        bucket_timestamp: str | None = ...,
        empty: bool | None = ...,
    ): ...
    def mrange(
        self,
        from_time: int | str,
        to_time: int | str,
        filters: list[str],
        count: int | None = ...,
        aggregation_type: str | None = ...,
        bucket_size_msec: int | None = ...,
        with_labels: bool | None = ...,
        filter_by_ts: list[int] | None = ...,
        filter_by_min_value: int | None = ...,
        filter_by_max_value: int | None = ...,
        groupby: str | None = ...,
        reduce: str | None = ...,
        select_labels: list[str] | None = ...,
        align: int | str | None = ...,
        latest: bool | None = ...,
        bucket_timestamp: str | None = ...,
        empty: bool | None = ...,
    ): ...
    def mrevrange(
        self,
        from_time: int | str,
        to_time: int | str,
        filters: list[str],
        count: int | None = ...,
        aggregation_type: str | None = ...,
        bucket_size_msec: int | None = ...,
        with_labels: bool | None = ...,
        filter_by_ts: list[int] | None = ...,
        filter_by_min_value: int | None = ...,
        filter_by_max_value: int | None = ...,
        groupby: str | None = ...,
        reduce: str | None = ...,
        select_labels: list[str] | None = ...,
        align: int | str | None = ...,
        latest: bool | None = ...,
        bucket_timestamp: str | None = ...,
        empty: bool | None = ...,
    ): ...
    def get(self, key: _Key, latest: bool | None = ...): ...
    def mget(
        self, filters: list[str], with_labels: bool | None = ..., select_labels: list[str] | None = ..., latest: bool | None = ...
    ): ...
    def info(self, key): ...
    def queryindex(self, filters): ...
