# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyThrottleProp(Component):
    """A FefferyThrottleProp component.
节流属性组件FefferyThrottleProp

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- sourceProp (boolean | number | string | dict | list; optional):
    用于同步目标属性，请通过回调函数更新.

- throttleProp (boolean | number | string | dict | list; optional):
    对应`sourceProp`的节流控制状态.

- throttleWait (number; default 200):
    设置节流延时时长，单位：毫秒  默认值：`200`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyThrottleProp'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        sourceProp: typing.Optional[typing.Any] = None,
        throttleProp: typing.Optional[typing.Any] = None,
        throttleWait: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'sourceProp', 'throttleProp', 'throttleWait']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'sourceProp', 'throttleProp', 'throttleWait']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyThrottleProp, self).__init__(**args)
