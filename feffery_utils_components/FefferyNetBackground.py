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


class FefferyNetBackground(Component):
    """A FefferyNetBackground component.
3D-Net背景组件FefferyNetBackground

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

- scale (number; default 1.00):
    设置比例  默认为`1.00`.

- scaleMobile (number; default 1.00):
    设置移动端比例  默认为`1.00`.

- color (string; default '#ff3f81'):
    设置`net`颜色  默认为`'#ff3f81'`.

- backgroundColor (string; default '#23153c'):
    设置背景颜色  默认为`'#23153c'`.

- points (number; default 10):
    设置`net`点的数量，范围`1`到`20`  默认为`10`.

- maxDistance (number; default 20):
    设置最大距离，范围`10`到`40`  默认为`20`.

- spacing (number; default 15):
    设置间距，范围`10`到`20`  默认为`15`.

- showDots (boolean; default True):
    设置是否展示点  默认为`True`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyNetBackground'


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
        scale: typing.Optional[NumberType] = None,
        scaleMobile: typing.Optional[NumberType] = None,
        color: typing.Optional[str] = None,
        backgroundColor: typing.Optional[str] = None,
        points: typing.Optional[NumberType] = None,
        maxDistance: typing.Optional[NumberType] = None,
        spacing: typing.Optional[NumberType] = None,
        showDots: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'scale', 'scaleMobile', 'color', 'backgroundColor', 'points', 'maxDistance', 'spacing', 'showDots']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'scale', 'scaleMobile', 'color', 'backgroundColor', 'points', 'maxDistance', 'spacing', 'showDots']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyNetBackground, self).__init__(children=children, **args)

setattr(FefferyNetBackground, "__init__", _explicitize_args(FefferyNetBackground.__init__))
