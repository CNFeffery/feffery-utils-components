# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class FefferyExtraSpinner(Component):
    """A FefferyExtraSpinner component.
额外加载动画组件FefferyExtraSpinner

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- type (a value equal to: "ball", "swap", "bars", "grid", "wave", "push", "firework", "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse", "swish", "sequence", "impulse", "cube", "magic", "flag", "fill", "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop", "flapper", "jellyfish", "trace", "classic", "whisper", "metro"; default 'ball'):
    可用的动画类型，可选项有`'ball'`、`'swap'`、`'bars'`、`'grid'`、`'wave'`、`'push'`、`'firework'`、
    `'stage'`、`'ring'`、`'heart'`、`'guard'`、`'rotate'`、`'spiral'`、`'pulse'`、`'swish'`、
    `'sequence'`、`'impulse'`、`'cube'`、`'magic'`、`'flag'`、`'fill'`、`'sphere'`、`'domino'`、
    `'goo'`、`'comb'`、`'pong'`、`'rainbow'`、`'hoop'`、`'flapper'`、`'jellyfish'`、`'trace'`、
    `'classic'`、`'whisper'`、`'metro'`.

- size (number; optional):
    图标尺寸值.

- sizeUnit (string; default 'px'):
    图标尺寸值单位  默认值：`'px'`.

- color (string; default '#1890ff'):
    图标颜色.

- frontColor (string; default '#def6ff'):
    图标前景色.

- backColor (string; default '#1890ff'):
    图标背景色."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyExtraSpinner'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        type: typing.Optional[Literal["ball", "swap", "bars", "grid", "wave", "push", "firework", "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse", "swish", "sequence", "impulse", "cube", "magic", "flag", "fill", "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop", "flapper", "jellyfish", "trace", "classic", "whisper", "metro"]] = None,
        size: typing.Optional[NumberType] = None,
        sizeUnit: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        frontColor: typing.Optional[str] = None,
        backColor: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'type', 'size', 'sizeUnit', 'color', 'frontColor', 'backColor']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'type', 'size', 'sizeUnit', 'color', 'frontColor', 'backColor']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyExtraSpinner, self).__init__(**args)

setattr(FefferyExtraSpinner, "__init__", _explicitize_args(FefferyExtraSpinner.__init__))
