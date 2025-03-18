# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyDraggable(Component):
    """A FefferyDraggable component.
可拖拽组件FefferyDraggable

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- className (string; optional):
    当前组件css类名.

- draggable (boolean; default True):
    是否开启可拖拽  默认值：`True`.

- initialX (number; required):
    必填，设置初始状态下当前可拖拽组件左上角距离页面顶端的像素距离.

- initialY (number; required):
    必填，设置初始状态下当前可拖拽组件左上角距离页面左侧的像素距离.

- showDragLine (boolean; default False):
    设置是否在拖拽时显示相关辅助线  默认值：`False`.

- dragLineColors (list of strings; default ['#d9d9d9', '#8c8c8c']):
    设置拖拽辅助线颜色  默认值：`['#d9d9d9', '#8c8c8c']`.

- focusWithinStyle (dict; default {    boxShadow: 'rgba(0, 0, 0, 0.08) 0px 6px 16px -8px, rgba(0, 0, 0, 0.05) 0px 9px 28px, rgba(0, 0, 0, 0.03) 0px 12px 48px 16px'}):
    设置聚焦状态下的额外`css`样式.

- boundsSelector (string; optional):
    设置可拖拽范围边界容器对应的`css`选择器，设置后拖拽将基于*相对-绝对布局*被限制在边界容器内部.

- x (number; optional):
    只读，用于监听当前可拖拽组件左上角距离页面顶端的像素距离.

- y (number; optional):
    只读，用于监听当前可拖拽组件左上角距离页面左侧的像素距离.

- isFocusWithin (boolean; optional):
    只读，用于监听当前可拖拽组件是否处于聚焦状态."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDraggable'

    @_explicitize_args
    def __init__(
        self,
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        draggable: typing.Optional[bool] = None,
        initialX: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        initialY: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        showDragLine: typing.Optional[bool] = None,
        dragLineColors: typing.Optional[typing.Sequence[str]] = None,
        focusWithinStyle: typing.Optional[dict] = None,
        boundsSelector: typing.Optional[str] = None,
        x: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        y: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        isFocusWithin: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'draggable', 'initialX', 'initialY', 'showDragLine', 'dragLineColors', 'focusWithinStyle', 'boundsSelector', 'x', 'y', 'isFocusWithin']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'draggable', 'initialX', 'initialY', 'showDragLine', 'dragLineColors', 'focusWithinStyle', 'boundsSelector', 'x', 'y', 'isFocusWithin']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['initialX', 'initialY']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyDraggable, self).__init__(children=children, **args)
