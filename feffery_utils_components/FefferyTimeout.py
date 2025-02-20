# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyTimeout(Component):
    """A FefferyTimeout component.
定时执行组件FefferyTimeout

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- timeoutCount (number; default 0):
    监听超时事件完成次数  默认值：`0`.

- delay (number; optional):
    设置距离下一次超时事件触发的倒计时间隔，单位：毫秒，每次有效的`delay`对应超时事件结束后都会被重置为空值."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTimeout'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        timeoutCount: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        delay: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'timeoutCount', 'delay']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'timeoutCount', 'delay']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyTimeout, self).__init__(**args)
