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


class FefferyDebounceProp(Component):
    """A FefferyDebounceProp component.
防抖属性组件FefferyDebounceProp

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- sourceProp (boolean | number | string | dict | list; optional):
    用于同步目标属性，请通过回调函数更新.

- debounceProp (boolean | number | string | dict | list; optional):
    对应`sourceProp`的防抖控制状态.

- debounceWait (number; default 200):
    设置防抖延时时长，单位：毫秒  默认值：`200`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDebounceProp'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        sourceProp: typing.Optional[typing.Any] = None,
        debounceProp: typing.Optional[typing.Any] = None,
        debounceWait: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'sourceProp', 'debounceProp', 'debounceWait']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'sourceProp', 'debounceProp', 'debounceWait']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDebounceProp, self).__init__(**args)

setattr(FefferyDebounceProp, "__init__", _explicitize_args(FefferyDebounceProp.__init__))
