from typing import Callable, Iterable, Sequence
from ._typing import *
from .transforms import Transform
from .backend_bases import GraphicsContextBase, RendererBase

class AbstractPathEffect:
    def __init__(self, offset: Sequence[float] = ...) -> None: ...
    def draw_path(
        self,
        renderer: RendererBase,
        gc: GraphicsContextBase,
        tpath,
        affine,
        rgbFace=...,
    ): ...

class PathEffectRenderer(RendererBase):
    def __init__(
        self, path_effects: Iterable[AbstractPathEffect], renderer: RendererBase
    ) -> None: ...
    def copy_with_path_effect(self, path_effects): ...
    def draw_path(self, gc: GraphicsContextBase, tpath, affine, rgbFace=...): ...
    def draw_markers(
        self,
        gc: GraphicsContextBase,
        marker_path,
        marker_trans: Transform,
        path,
        *args,
        **kwargs
    ): ...
    def draw_path_collection(
        self, gc: GraphicsContextBase, master_transform, paths, *args, **kwargs
    ): ...
    def __getattribute__(
        self, name: str
    ) -> Callable | list[Stroke | Normal] | RendererBase: ...

class Normal(AbstractPathEffect): ...

class Stroke(AbstractPathEffect):
    def __init__(self, offset: Sequence[float] = ..., **kwargs) -> None: ...
    def draw_path(
        self,
        renderer: RendererBase,
        gc: GraphicsContextBase,
        tpath,
        affine,
        rgbFace: Color,
    ): ...

withStroke = ...

class SimplePatchShadow(AbstractPathEffect):
    def __init__(
        self,
        offset: Sequence[float] = ...,
        shadow_rgbFace: Color = ...,
        alpha: float = 0.3,
        rho: float = 0.3,
        **kwargs
    ) -> None: ...
    def draw_path(
        self,
        renderer: RendererBase,
        gc: GraphicsContextBase,
        tpath,
        affine,
        rgbFace: Color,
    ): ...

withSimplePatchShadow = ...

class SimpleLineShadow(AbstractPathEffect):
    def __init__(
        self,
        offset: Sequence[float] = ...,
        shadow_color: Color = "black",
        alpha: float = 0.3,
        rho: float = 0.3,
        **kwargs
    ) -> None: ...
    def draw_path(
        self,
        renderer: RendererBase,
        gc: GraphicsContextBase,
        tpath,
        affine,
        rgbFace: Color,
    ): ...

class PathPatchEffect(AbstractPathEffect):
    def __init__(self, offset: Sequence[float] = ..., **kwargs) -> None: ...
    def draw_path(
        self,
        renderer: RendererBase,
        gc: GraphicsContextBase,
        tpath,
        affine,
        rgbFace: Color,
    ): ...

class TickedStroke(AbstractPathEffect):
    def __init__(
        self,
        offset: Sequence[float] = ...,
        spacing: float = 10,
        angle: float = 45,
        length: float = 1.414,
        **kwargs
    ) -> None: ...
    def draw_path(
        self,
        renderer: RendererBase,
        gc: GraphicsContextBase,
        tpath,
        affine,
        rgbFace: Color,
    ): ...

withTickedStroke = ...
