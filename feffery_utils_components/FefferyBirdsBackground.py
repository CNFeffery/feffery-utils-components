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


class FefferyBirdsBackground(Component):
    """A FefferyBirdsBackground component.
3D-Birds背景组件FefferyBirdsBackground

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
    设置是否开启鼠标控  默认为`True`.

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

- backgroundColor (string; default '#000000'):
    设置背景颜色  默认为`'#000000'`.

- backgroundAlpha (number; default 1):
    设置背景颜色透明度，范围`0`到`1`  默认为`1`.

- color1 (string; default '#ff0000'):
    设置birds颜色1  默认为`'#ff0000'`.

- color2 (string; default '#13becf'):
    设置birds颜色2  默认为`'#13becf'`.

- colorMode (a value equal to: 'lerp', 'variance', 'lerpGradient', 'varianceGradient'; default 'varianceGradient'):
    设置颜色模式，可选的有`'lerp'`、`'variance'`、`'lerpGradient'`、`'varianceGradient'`
    默认为`'varianceGradient'`.

- quantity (number; default 5):
    设置背景质量，范围`1`到`5`  默认为`5`.

- birdSize (number; default 1):
    设置birds大小，范围`1`到`4`  默认为`1`.

- wingSpan (number; default 30):
    设置birds翼展，范围`10`到`40`  默认为`30`.

- speedLimit (number; default 5):
    设置birds速度限制，范围`1`到`10`  默认为`5`.

- separation (number; default 20):
    设置birds分离大小，范围`1`到`100  默认为`20`.

- alignment (number; default 20):
    设置birds对齐大小，范围`1`到`100`  默认为`20`.

- cohesion (number; default 20):
    设置birds内聚大小，范围`1`到`100`  默认为`20`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyBirdsBackground'


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
        backgroundColor: typing.Optional[str] = None,
        backgroundAlpha: typing.Optional[NumberType] = None,
        color1: typing.Optional[str] = None,
        color2: typing.Optional[str] = None,
        colorMode: typing.Optional[Literal["lerp", "variance", "lerpGradient", "varianceGradient"]] = None,
        quantity: typing.Optional[NumberType] = None,
        birdSize: typing.Optional[NumberType] = None,
        wingSpan: typing.Optional[NumberType] = None,
        speedLimit: typing.Optional[NumberType] = None,
        separation: typing.Optional[NumberType] = None,
        alignment: typing.Optional[NumberType] = None,
        cohesion: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'scale', 'scaleMobile', 'backgroundColor', 'backgroundAlpha', 'color1', 'color2', 'colorMode', 'quantity', 'birdSize', 'wingSpan', 'speedLimit', 'separation', 'alignment', 'cohesion']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'scale', 'scaleMobile', 'backgroundColor', 'backgroundAlpha', 'color1', 'color2', 'colorMode', 'quantity', 'birdSize', 'wingSpan', 'speedLimit', 'separation', 'alignment', 'cohesion']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyBirdsBackground, self).__init__(children=children, **args)

setattr(FefferyBirdsBackground, "__init__", _explicitize_args(FefferyBirdsBackground.__init__))
