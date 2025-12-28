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


class FefferyCloudsBackground(Component):
    """A FefferyCloudsBackground component.
3D-Clouds背景组件FefferyCloudsBackground

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，设置内嵌元素内容.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- mouseControls (boolean; default True):
    设置是否开启鼠标控制  默认为`True`.

- touchControls (boolean; default True):
    设置是否开启触摸控制  默认为`True`.

- gyroControls (boolean; default False):
    设置是否开启陀螺仪控制  默认为`False`.

- minHeight (number; default 200.00):
    设置最小高度  默认为`200.00`.

- minWidth (number; default 200.00):
    设置最小宽度  默认为`200.00`.

- backgroundColor (string; default '#ffffff'):
    设置背景颜色  默认为`'#ffffff'`.

- skyColor (string; default '#68b8d7'):
    设置天空颜色  默认为`'#68b8d7'`.

- cloudColor (string; default '#adc1de'):
    设置云颜色  默认为`'#adc1de'`.

- cloudShadowColor (string; default '#183550'):
    设置云阴影颜色  默认为`'#183550'`.

- sunColor (string; default '#ff9919'):
    设置太阳颜色  默认为`'#ff9919'`.

- sunGlareColor (string; default '#ff6633'):
    设置太阳炫光颜色  默认为`'#ff6633'`.

- sunlightColor (string; default '#ff9933'):
    设置太阳光线颜色  默认为`'#ff9933'`.

- speed (number; default 1):
    设置动画速度，范围`0`到`3`  默认为`1`."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCloudsBackground'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        mouseControls: typing.Optional[bool] = None,
        touchControls: typing.Optional[bool] = None,
        gyroControls: typing.Optional[bool] = None,
        minHeight: typing.Optional[NumberType] = None,
        minWidth: typing.Optional[NumberType] = None,
        backgroundColor: typing.Optional[str] = None,
        skyColor: typing.Optional[str] = None,
        cloudColor: typing.Optional[str] = None,
        cloudShadowColor: typing.Optional[str] = None,
        sunColor: typing.Optional[str] = None,
        sunGlareColor: typing.Optional[str] = None,
        sunlightColor: typing.Optional[str] = None,
        speed: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'backgroundColor', 'skyColor', 'cloudColor', 'cloudShadowColor', 'sunColor', 'sunGlareColor', 'sunlightColor', 'speed']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'backgroundColor', 'skyColor', 'cloudColor', 'cloudShadowColor', 'sunColor', 'sunGlareColor', 'sunlightColor', 'speed']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyCloudsBackground, self).__init__(children=children, **args)

setattr(FefferyCloudsBackground, "__init__", _explicitize_args(FefferyCloudsBackground.__init__))
