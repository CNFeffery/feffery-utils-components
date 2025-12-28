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


class FefferyTwitterColorPicker(Component):
    """A FefferyTwitterColorPicker component.
Twitter风格色彩选择器FefferyGithubColorPicker

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- width (string; default '276px'):
    整体宽度  默认值：`'276px'`.

- color (string; optional):
    监听或设置当前选中色彩对应16进制颜色值.

- colors (list of strings; default ['#FF6900', '#FCB900', '#7BDCB5', '#00D084', '#8ED1FC', '#0693E3', '#ABB8C3', '#EB144C', '#F78DA7', '#9900EF']):
    设置可选色彩对应16进制颜色值数组  默认值：`['#FF6900', '#FCB900', '#7BDCB5',
    '#00D084', '#8ED1FC', '#0693E3', '#ABB8C3', '#EB144C', '#F78DA7',
    '#9900EF']`.

- triangle (a value equal to: 'hide', 'top-left', 'top-right'; default 'top-left'):
    顶部箭头方位，可选项有`'hide'`、`'top-left'`、`'top-right'`  默认值：`'top-left'`."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTwitterColorPicker'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        width: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        colors: typing.Optional[typing.Sequence[str]] = None,
        triangle: typing.Optional[Literal["hide", "top-left", "top-right"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'width', 'color', 'colors', 'triangle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'width', 'color', 'colors', 'triangle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyTwitterColorPicker, self).__init__(**args)

setattr(FefferyTwitterColorPicker, "__init__", _explicitize_args(FefferyTwitterColorPicker.__init__))
