from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class Index(Serialisable):
    tagname: str
    v: Incomplete
    def __init__(self, v: int = ...) -> None: ...

class Tuple(Serialisable):  # type: ignore[misc]
    fld: Incomplete
    hier: Incomplete
    item: Incomplete
    def __init__(self, fld: Incomplete | None = ..., hier: Incomplete | None = ..., item: Incomplete | None = ...) -> None: ...

class TupleList(Serialisable):  # type: ignore[misc]
    c: Incomplete
    tpl: Incomplete
    __elements__: Incomplete
    def __init__(self, c: Incomplete | None = ..., tpl: Incomplete | None = ...) -> None: ...

class Missing(Serialisable):
    tagname: str
    tpls: Incomplete
    x: Incomplete
    u: Incomplete
    f: Incomplete
    c: Incomplete
    cp: Incomplete
    bc: Incomplete
    fc: Incomplete
    i: Incomplete
    un: Incomplete
    st: Incomplete
    b: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        tpls=...,
        x=...,
        u: Incomplete | None = ...,
        f: Incomplete | None = ...,
        c: Incomplete | None = ...,
        cp: Incomplete | None = ...,
        _in: Incomplete | None = ...,
        bc: Incomplete | None = ...,
        fc: Incomplete | None = ...,
        i: Incomplete | None = ...,
        un: Incomplete | None = ...,
        st: Incomplete | None = ...,
        b: Incomplete | None = ...,
    ) -> None: ...

class Number(Serialisable):
    tagname: str
    tpls: Incomplete
    x: Incomplete
    v: Incomplete
    u: Incomplete
    f: Incomplete
    c: Incomplete
    cp: Incomplete
    bc: Incomplete
    fc: Incomplete
    i: Incomplete
    un: Incomplete
    st: Incomplete
    b: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        tpls=...,
        x=...,
        v: Incomplete | None = ...,
        u: Incomplete | None = ...,
        f: Incomplete | None = ...,
        c: Incomplete | None = ...,
        cp: Incomplete | None = ...,
        _in: Incomplete | None = ...,
        bc: Incomplete | None = ...,
        fc: Incomplete | None = ...,
        i: Incomplete | None = ...,
        un: Incomplete | None = ...,
        st: Incomplete | None = ...,
        b: Incomplete | None = ...,
    ) -> None: ...

class Error(Serialisable):
    tagname: str
    tpls: Incomplete
    x: Incomplete
    v: Incomplete
    u: Incomplete
    f: Incomplete
    c: Incomplete
    cp: Incomplete
    bc: Incomplete
    fc: Incomplete
    i: Incomplete
    un: Incomplete
    st: Incomplete
    b: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        tpls: Incomplete | None = ...,
        x=...,
        v: Incomplete | None = ...,
        u: Incomplete | None = ...,
        f: Incomplete | None = ...,
        c: Incomplete | None = ...,
        cp: Incomplete | None = ...,
        _in: Incomplete | None = ...,
        bc: Incomplete | None = ...,
        fc: Incomplete | None = ...,
        i: Incomplete | None = ...,
        un: Incomplete | None = ...,
        st: Incomplete | None = ...,
        b: Incomplete | None = ...,
    ) -> None: ...

class Boolean(Serialisable):
    tagname: str
    x: Incomplete
    v: Incomplete
    u: Incomplete
    f: Incomplete
    c: Incomplete
    cp: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        x=...,
        v: Incomplete | None = ...,
        u: Incomplete | None = ...,
        f: Incomplete | None = ...,
        c: Incomplete | None = ...,
        cp: Incomplete | None = ...,
    ) -> None: ...

class Text(Serialisable):
    tagname: str
    tpls: Incomplete
    x: Incomplete
    v: Incomplete
    u: Incomplete
    f: Incomplete
    c: Incomplete
    cp: Incomplete
    bc: Incomplete
    fc: Incomplete
    i: Incomplete
    un: Incomplete
    st: Incomplete
    b: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        tpls=...,
        x=...,
        v: Incomplete | None = ...,
        u: Incomplete | None = ...,
        f: Incomplete | None = ...,
        c: Incomplete | None = ...,
        cp: Incomplete | None = ...,
        _in: Incomplete | None = ...,
        bc: Incomplete | None = ...,
        fc: Incomplete | None = ...,
        i: Incomplete | None = ...,
        un: Incomplete | None = ...,
        st: Incomplete | None = ...,
        b: Incomplete | None = ...,
    ) -> None: ...

class DateTimeField(Serialisable):
    tagname: str
    x: Incomplete
    v: Incomplete
    u: Incomplete
    f: Incomplete
    c: Incomplete
    cp: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        x=...,
        v: Incomplete | None = ...,
        u: Incomplete | None = ...,
        f: Incomplete | None = ...,
        c: Incomplete | None = ...,
        cp: Incomplete | None = ...,
    ) -> None: ...
