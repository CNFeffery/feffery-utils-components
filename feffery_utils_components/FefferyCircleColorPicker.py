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


class FefferyCircleColorPicker(Component):
    """A FefferyCircleColorPicker component.
Circle风格色彩选择器

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- width (string; default '252px'):
    整体宽度  默认值：`'252px'`.

- circleSize (number; default 28):
    圆圈像素大小  默认值：`28`.

- circleSpacing (number; default 14):
    圆圈之间的像素间隔大小  默认值：`14`.

- color (string; optional):
    监听或设置当前选中色彩对应16进制颜色值.

- colors (list of strings; default ["#f44336", "#e91e63", "#9c27b0", "#673ab7", "#3f51b5", "#2196f3", "#03a9f4", "#00bcd4", "#009688", "#4caf50", "#8bc34a", "#cddc39", "#ffeb3b", "#ffc107", "#ff9800", "#ff5722", "#795548", "#607d8b"]):
    设置可选色彩对应16进制颜色值数组  默认值：`[\"#f44336\", \"#e91e63\", \"#9c27b0\",
    \"#673ab7\", \"#3f51b5\", \"#2196f3\", \"#03a9f4\", \"#00bcd4\",
    \"#009688\", \"#4caf50\", \"#8bc34a\", \"#cddc39\", \"#ffeb3b\",
    \"#ffc107\", \"#ff9800\", \"#ff5722\", \"#795548\", \"#607d8b\"]`."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCircleColorPicker'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        width: typing.Optional[str] = None,
        circleSize: typing.Optional[NumberType] = None,
        circleSpacing: typing.Optional[NumberType] = None,
        color: typing.Optional[str] = None,
        colors: typing.Optional[typing.Sequence[str]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'width', 'circleSize', 'circleSpacing', 'color', 'colors']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'width', 'circleSize', 'circleSpacing', 'color', 'colors']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyCircleColorPicker, self).__init__(**args)

setattr(FefferyCircleColorPicker, "__init__", _explicitize_args(FefferyCircleColorPicker.__init__))
