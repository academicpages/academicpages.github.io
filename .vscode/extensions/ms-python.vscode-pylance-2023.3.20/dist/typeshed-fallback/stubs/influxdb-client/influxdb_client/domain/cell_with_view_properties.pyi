from _typeshed import Incomplete

from influxdb_client.domain.cell import Cell

class CellWithViewProperties(Cell):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        properties: Incomplete | None = ...,
        id: Incomplete | None = ...,
        links: Incomplete | None = ...,
        x: Incomplete | None = ...,
        y: Incomplete | None = ...,
        w: Incomplete | None = ...,
        h: Incomplete | None = ...,
        view_id: Incomplete | None = ...,
    ) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def properties(self): ...
    @properties.setter
    def properties(self, properties) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
