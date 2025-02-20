# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyLongPress(Component):
    """A FefferyLongPress component.
长按事件监听组件FefferyLongPress

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- targetId (string; optional):
    设置当前长按监听组件的监听目标元素`id`.

- pressCounts (number; default 0):
    监听目标组件累计被长按次数  默认值：`0`.

- isLongPressing (boolean; optional):
    监听目标组件是否正处于长按状态.

- delay (number; default 300):
    设置符合长按行为的持续时长，单位：毫秒  默认值：`300`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyLongPress'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        targetId: typing.Optional[str] = None,
        pressCounts: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        isLongPressing: typing.Optional[bool] = None,
        delay: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'targetId', 'pressCounts', 'isLongPressing', 'delay']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'targetId', 'pressCounts', 'isLongPressing', 'delay']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyLongPress, self).__init__(**args)
