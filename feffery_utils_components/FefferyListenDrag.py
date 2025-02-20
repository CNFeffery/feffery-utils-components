# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyListenDrag(Component):
    """A FefferyListenDrag component.
拖拽事件监听组件FefferyListenDrag

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- targetSelector (string; optional):
    拖拽事件监听目标选择器规则字符串.

- data (boolean | number | string | dict | list; optional):
    当前监听目标所携带的数据，配合**FefferyListenDrop**使用.

- isDragging (boolean; optional):
    监听目标是否处于拖拽中状态."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyListenDrag'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        targetSelector: typing.Optional[str] = None,
        data: typing.Optional[typing.Any] = None,
        isDragging: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'targetSelector', 'data', 'isDragging']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'targetSelector', 'data', 'isDragging']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyListenDrag, self).__init__(**args)
