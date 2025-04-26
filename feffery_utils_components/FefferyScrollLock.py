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


class FefferyScrollLock(Component):
    """A FefferyScrollLock component.
滚动锁定组件FefferyScrollLock

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- target (string; optional):
    设置滚动锁定目标元素`id`，默认将锁定整个页面.

- locked (boolean; default False):
    设置针对目标是否开启滚动锁定  默认值：`False`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyScrollLock'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        target: typing.Optional[str] = None,
        locked: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'target', 'locked']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'target', 'locked']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyScrollLock, self).__init__(**args)

setattr(FefferyScrollLock, "__init__", _explicitize_args(FefferyScrollLock.__init__))
