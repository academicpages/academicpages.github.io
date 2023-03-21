from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class EmbeddedWAVAudioFile(Serialisable):  # type: ignore[misc]
    name: Incomplete
    def __init__(self, name: Incomplete | None = ...) -> None: ...

class Hyperlink(Serialisable):
    tagname: str
    namespace: Incomplete
    invalidUrl: Incomplete
    action: Incomplete
    tgtFrame: Incomplete
    tooltip: Incomplete
    history: Incomplete
    highlightClick: Incomplete
    endSnd: Incomplete
    snd: Incomplete
    extLst: Incomplete
    id: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        invalidUrl: Incomplete | None = ...,
        action: Incomplete | None = ...,
        tgtFrame: Incomplete | None = ...,
        tooltip: Incomplete | None = ...,
        history: Incomplete | None = ...,
        highlightClick: Incomplete | None = ...,
        endSnd: Incomplete | None = ...,
        snd: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        id: Incomplete | None = ...,
    ) -> None: ...

class Font(Serialisable):
    tagname: str
    namespace: Incomplete
    typeface: Incomplete
    panose: Incomplete
    pitchFamily: Incomplete
    charset: Incomplete
    def __init__(
        self,
        typeface: Incomplete | None = ...,
        panose: Incomplete | None = ...,
        pitchFamily: Incomplete | None = ...,
        charset: Incomplete | None = ...,
    ) -> None: ...

class CharacterProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    kumimoji: Incomplete
    lang: Incomplete
    altLang: Incomplete
    sz: Incomplete
    b: Incomplete
    i: Incomplete
    u: Incomplete
    strike: Incomplete
    kern: Incomplete
    cap: Incomplete
    spc: Incomplete
    normalizeH: Incomplete
    baseline: Incomplete
    noProof: Incomplete
    dirty: Incomplete
    err: Incomplete
    smtClean: Incomplete
    smtId: Incomplete
    bmk: Incomplete
    ln: Incomplete
    highlight: Incomplete
    latin: Incomplete
    ea: Incomplete
    cs: Incomplete
    sym: Incomplete
    hlinkClick: Incomplete
    hlinkMouseOver: Incomplete
    rtl: Incomplete
    extLst: Incomplete
    noFill: Incomplete
    solidFill: Incomplete
    gradFill: Incomplete
    blipFill: Incomplete
    pattFill: Incomplete
    grpFill: Incomplete
    effectLst: Incomplete
    effectDag: Incomplete
    uLnTx: Incomplete
    uLn: Incomplete
    uFillTx: Incomplete
    uFill: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        kumimoji: Incomplete | None = ...,
        lang: Incomplete | None = ...,
        altLang: Incomplete | None = ...,
        sz: Incomplete | None = ...,
        b: Incomplete | None = ...,
        i: Incomplete | None = ...,
        u: Incomplete | None = ...,
        strike: Incomplete | None = ...,
        kern: Incomplete | None = ...,
        cap: Incomplete | None = ...,
        spc: Incomplete | None = ...,
        normalizeH: Incomplete | None = ...,
        baseline: Incomplete | None = ...,
        noProof: Incomplete | None = ...,
        dirty: Incomplete | None = ...,
        err: Incomplete | None = ...,
        smtClean: Incomplete | None = ...,
        smtId: Incomplete | None = ...,
        bmk: Incomplete | None = ...,
        ln: Incomplete | None = ...,
        highlight: Incomplete | None = ...,
        latin: Incomplete | None = ...,
        ea: Incomplete | None = ...,
        cs: Incomplete | None = ...,
        sym: Incomplete | None = ...,
        hlinkClick: Incomplete | None = ...,
        hlinkMouseOver: Incomplete | None = ...,
        rtl: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        noFill: Incomplete | None = ...,
        solidFill: Incomplete | None = ...,
        gradFill: Incomplete | None = ...,
        blipFill: Incomplete | None = ...,
        pattFill: Incomplete | None = ...,
        grpFill: Incomplete | None = ...,
        effectLst: Incomplete | None = ...,
        effectDag: Incomplete | None = ...,
        uLnTx: Incomplete | None = ...,
        uLn: Incomplete | None = ...,
        uFillTx: Incomplete | None = ...,
        uFill: Incomplete | None = ...,
    ) -> None: ...

class TabStop(Serialisable):  # type: ignore[misc]
    pos: Incomplete
    algn: Incomplete
    def __init__(self, pos: Incomplete | None = ..., algn: Incomplete | None = ...) -> None: ...

class TabStopList(Serialisable):  # type: ignore[misc]
    tab: Incomplete
    def __init__(self, tab: Incomplete | None = ...) -> None: ...

class Spacing(Serialisable):
    spcPct: Incomplete
    spcPts: Incomplete
    __elements__: Incomplete
    def __init__(self, spcPct: Incomplete | None = ..., spcPts: Incomplete | None = ...) -> None: ...

class AutonumberBullet(Serialisable):
    type: Incomplete
    startAt: Incomplete
    def __init__(self, type: Incomplete | None = ..., startAt: Incomplete | None = ...) -> None: ...

class ParagraphProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    marL: Incomplete
    marR: Incomplete
    lvl: Incomplete
    indent: Incomplete
    algn: Incomplete
    defTabSz: Incomplete
    rtl: Incomplete
    eaLnBrk: Incomplete
    fontAlgn: Incomplete
    latinLnBrk: Incomplete
    hangingPunct: Incomplete
    lnSpc: Incomplete
    spcBef: Incomplete
    spcAft: Incomplete
    tabLst: Incomplete
    defRPr: Incomplete
    extLst: Incomplete
    buClrTx: Incomplete
    buClr: Incomplete
    buSzTx: Incomplete
    buSzPct: Incomplete
    buSzPts: Incomplete
    buFontTx: Incomplete
    buFont: Incomplete
    buNone: Incomplete
    buAutoNum: Incomplete
    buChar: Incomplete
    buBlip: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        marL: Incomplete | None = ...,
        marR: Incomplete | None = ...,
        lvl: Incomplete | None = ...,
        indent: Incomplete | None = ...,
        algn: Incomplete | None = ...,
        defTabSz: Incomplete | None = ...,
        rtl: Incomplete | None = ...,
        eaLnBrk: Incomplete | None = ...,
        fontAlgn: Incomplete | None = ...,
        latinLnBrk: Incomplete | None = ...,
        hangingPunct: Incomplete | None = ...,
        lnSpc: Incomplete | None = ...,
        spcBef: Incomplete | None = ...,
        spcAft: Incomplete | None = ...,
        tabLst: Incomplete | None = ...,
        defRPr: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        buClrTx: Incomplete | None = ...,
        buClr: Incomplete | None = ...,
        buSzTx: Incomplete | None = ...,
        buSzPct: Incomplete | None = ...,
        buSzPts: Incomplete | None = ...,
        buFontTx: Incomplete | None = ...,
        buFont: Incomplete | None = ...,
        buNone: Incomplete | None = ...,
        buAutoNum: Incomplete | None = ...,
        buChar: Incomplete | None = ...,
        buBlip: Incomplete | None = ...,
    ) -> None: ...

class ListStyle(Serialisable):
    tagname: str
    namespace: Incomplete
    defPPr: Incomplete
    lvl1pPr: Incomplete
    lvl2pPr: Incomplete
    lvl3pPr: Incomplete
    lvl4pPr: Incomplete
    lvl5pPr: Incomplete
    lvl6pPr: Incomplete
    lvl7pPr: Incomplete
    lvl8pPr: Incomplete
    lvl9pPr: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        defPPr: Incomplete | None = ...,
        lvl1pPr: Incomplete | None = ...,
        lvl2pPr: Incomplete | None = ...,
        lvl3pPr: Incomplete | None = ...,
        lvl4pPr: Incomplete | None = ...,
        lvl5pPr: Incomplete | None = ...,
        lvl6pPr: Incomplete | None = ...,
        lvl7pPr: Incomplete | None = ...,
        lvl8pPr: Incomplete | None = ...,
        lvl9pPr: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
    ) -> None: ...

class RegularTextRun(Serialisable):
    tagname: str
    namespace: Incomplete
    rPr: Incomplete
    properties: Incomplete
    t: Incomplete
    value: Incomplete
    __elements__: Incomplete
    def __init__(self, rPr: Incomplete | None = ..., t: str = ...) -> None: ...

class LineBreak(Serialisable):
    tagname: str
    namespace: Incomplete
    rPr: Incomplete
    __elements__: Incomplete
    def __init__(self, rPr: Incomplete | None = ...) -> None: ...

class TextField(Serialisable):
    id: Incomplete
    type: Incomplete
    rPr: Incomplete
    pPr: Incomplete
    t: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        id: Incomplete | None = ...,
        type: Incomplete | None = ...,
        rPr: Incomplete | None = ...,
        pPr: Incomplete | None = ...,
        t: Incomplete | None = ...,
    ) -> None: ...

class Paragraph(Serialisable):
    tagname: str
    namespace: Incomplete
    pPr: Incomplete
    properties: Incomplete
    endParaRPr: Incomplete
    r: Incomplete
    text: Incomplete
    br: Incomplete
    fld: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        pPr: Incomplete | None = ...,
        endParaRPr: Incomplete | None = ...,
        r: Incomplete | None = ...,
        br: Incomplete | None = ...,
        fld: Incomplete | None = ...,
    ) -> None: ...

class GeomGuide(Serialisable):
    name: Incomplete
    fmla: Incomplete
    def __init__(self, name: Incomplete | None = ..., fmla: Incomplete | None = ...) -> None: ...

class GeomGuideList(Serialisable):
    gd: Incomplete
    def __init__(self, gd: Incomplete | None = ...) -> None: ...

class PresetTextShape(Serialisable):
    prst: Incomplete
    avLst: Incomplete
    def __init__(self, prst: Incomplete | None = ..., avLst: Incomplete | None = ...) -> None: ...

class TextNormalAutofit(Serialisable):
    fontScale: Incomplete
    lnSpcReduction: Incomplete
    def __init__(self, fontScale: Incomplete | None = ..., lnSpcReduction: Incomplete | None = ...) -> None: ...

class RichTextProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    rot: Incomplete
    spcFirstLastPara: Incomplete
    vertOverflow: Incomplete
    horzOverflow: Incomplete
    vert: Incomplete
    wrap: Incomplete
    lIns: Incomplete
    tIns: Incomplete
    rIns: Incomplete
    bIns: Incomplete
    numCol: Incomplete
    spcCol: Incomplete
    rtlCol: Incomplete
    fromWordArt: Incomplete
    anchor: Incomplete
    anchorCtr: Incomplete
    forceAA: Incomplete
    upright: Incomplete
    compatLnSpc: Incomplete
    prstTxWarp: Incomplete
    scene3d: Incomplete
    extLst: Incomplete
    noAutofit: Incomplete
    normAutofit: Incomplete
    spAutoFit: Incomplete
    flatTx: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        rot: Incomplete | None = ...,
        spcFirstLastPara: Incomplete | None = ...,
        vertOverflow: Incomplete | None = ...,
        horzOverflow: Incomplete | None = ...,
        vert: Incomplete | None = ...,
        wrap: Incomplete | None = ...,
        lIns: Incomplete | None = ...,
        tIns: Incomplete | None = ...,
        rIns: Incomplete | None = ...,
        bIns: Incomplete | None = ...,
        numCol: Incomplete | None = ...,
        spcCol: Incomplete | None = ...,
        rtlCol: Incomplete | None = ...,
        fromWordArt: Incomplete | None = ...,
        anchor: Incomplete | None = ...,
        anchorCtr: Incomplete | None = ...,
        forceAA: Incomplete | None = ...,
        upright: Incomplete | None = ...,
        compatLnSpc: Incomplete | None = ...,
        prstTxWarp: Incomplete | None = ...,
        scene3d: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        noAutofit: Incomplete | None = ...,
        normAutofit: Incomplete | None = ...,
        spAutoFit: Incomplete | None = ...,
        flatTx: Incomplete | None = ...,
    ) -> None: ...
