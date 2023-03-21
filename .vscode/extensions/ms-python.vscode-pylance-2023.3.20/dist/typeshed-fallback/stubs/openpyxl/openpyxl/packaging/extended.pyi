from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

def get_version(): ...

class DigSigBlob(Serialisable):  # type: ignore[misc]
    __elements__: Incomplete
    __attrs__: Incomplete

class VectorLpstr(Serialisable):  # type: ignore[misc]
    __elements__: Incomplete
    __attrs__: Incomplete

class VectorVariant(Serialisable):  # type: ignore[misc]
    __elements__: Incomplete
    __attrs__: Incomplete

class ExtendedProperties(Serialisable):
    tagname: str
    Template: Incomplete
    Manager: Incomplete
    Company: Incomplete
    Pages: Incomplete
    Words: Incomplete
    Characters: Incomplete
    PresentationFormat: Incomplete
    Lines: Incomplete
    Paragraphs: Incomplete
    Slides: Incomplete
    Notes: Incomplete
    TotalTime: Incomplete
    HiddenSlides: Incomplete
    MMClips: Incomplete
    ScaleCrop: Incomplete
    HeadingPairs: Incomplete
    TitlesOfParts: Incomplete
    LinksUpToDate: Incomplete
    CharactersWithSpaces: Incomplete
    SharedDoc: Incomplete
    HyperlinkBase: Incomplete
    HLinks: Incomplete
    HyperlinksChanged: Incomplete
    DigSig: Incomplete
    Application: Incomplete
    AppVersion: Incomplete
    DocSecurity: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        Template: Incomplete | None = ...,
        Manager: Incomplete | None = ...,
        Company: Incomplete | None = ...,
        Pages: Incomplete | None = ...,
        Words: Incomplete | None = ...,
        Characters: Incomplete | None = ...,
        PresentationFormat: Incomplete | None = ...,
        Lines: Incomplete | None = ...,
        Paragraphs: Incomplete | None = ...,
        Slides: Incomplete | None = ...,
        Notes: Incomplete | None = ...,
        TotalTime: Incomplete | None = ...,
        HiddenSlides: Incomplete | None = ...,
        MMClips: Incomplete | None = ...,
        ScaleCrop: Incomplete | None = ...,
        HeadingPairs: Incomplete | None = ...,
        TitlesOfParts: Incomplete | None = ...,
        LinksUpToDate: Incomplete | None = ...,
        CharactersWithSpaces: Incomplete | None = ...,
        SharedDoc: Incomplete | None = ...,
        HyperlinkBase: Incomplete | None = ...,
        HLinks: Incomplete | None = ...,
        HyperlinksChanged: Incomplete | None = ...,
        DigSig: Incomplete | None = ...,
        Application: str = ...,
        AppVersion: Incomplete | None = ...,
        DocSecurity: Incomplete | None = ...,
    ) -> None: ...
    def to_tree(self): ...
