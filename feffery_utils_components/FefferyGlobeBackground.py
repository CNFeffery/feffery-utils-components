# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyGlobeBackground(Component):
    """A FefferyGlobeBackground component.
3D-Globe背景组件FefferyGlobeBackground

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，设置内嵌元素内容.

- style (dict; optional):
    当前组件css样式.

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

- backgroundColor (string; default '#23153c'):
    设置背景颜色  默认为`'#23153c'`.

- color (string; default '#ff3f81'):
    设置globe颜色  默认为`'#ff3f81'`.

- color2 (string; default '#ffffff'):
    设置globe颜色2  默认为`'#ffffff'`.

- size (number; default 1):
    设置globe大小，范围`0.5`到`2`  默认为`1`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyGlobeBackground'

    @_explicitize_args
    def __init__(
        self,
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        mouseControls: typing.Optional[bool] = None,
        touchControls: typing.Optional[bool] = None,
        gyroControls: typing.Optional[bool] = None,
        minHeight: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        minWidth: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        scale: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        scaleMobile: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        backgroundColor: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        color2: typing.Optional[str] = None,
        size: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'scale', 'scaleMobile', 'backgroundColor', 'color', 'color2', 'size']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'scale', 'scaleMobile', 'backgroundColor', 'color', 'color2', 'size']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyGlobeBackground, self).__init__(children=children, **args)
