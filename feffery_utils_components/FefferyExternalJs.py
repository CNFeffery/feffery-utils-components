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


class FefferyExternalJs(Component):
    """A FefferyExternalJs component.
外部js资源动态注入组件FefferyExternalJs

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- jsUrl (string; default ''):
    设置对应绑定的js静态文件资源`url`  默认值：`''`.

- recentlyStatus (a value equal to: 'unset', 'loading', 'ready', 'error'; optional):
    监听最近一次资源变更操作后对应的状态."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyExternalJs'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        jsUrl: typing.Optional[str] = None,
        recentlyStatus: typing.Optional[Literal["unset", "loading", "ready", "error"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'jsUrl', 'recentlyStatus']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'jsUrl', 'recentlyStatus']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyExternalJs, self).__init__(**args)

setattr(FefferyExternalJs, "__init__", _explicitize_args(FefferyExternalJs.__init__))
