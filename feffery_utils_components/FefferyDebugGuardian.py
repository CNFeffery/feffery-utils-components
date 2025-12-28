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


class FefferyDebugGuardian(Component):
    """A FefferyDebugGuardian component.
调试守护组件FefferyDebugGuardian

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- detectInterval (number; default 1000):
    设置后台轮询检测的间隔时长，单位：毫秒  默认值：`1000`.

- strategy (a value equal to: 'infinite-debugger', 'debugger-then-auto-close', 'debugger-then-execute-js'; default 'infinite-debugger'):
    设置当检测到开发者工具被打开时的应对策略，可选的有`'infinite-debugger'`（无限debugger）、`'debugger-then-auto-close'`（激活debugger后自动关闭）、`'debugger-then-execute-js'`（激活debugger后执行js）
    默认值：`'infinite-debugger'`.

- jsString (string; optional):
    当`strategy`为`'debugger-then-execute-js'`时，设置要执行的js代码."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDebugGuardian'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        detectInterval: typing.Optional[NumberType] = None,
        strategy: typing.Optional[Literal["infinite-debugger", "debugger-then-auto-close", "debugger-then-execute-js"]] = None,
        jsString: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'detectInterval', 'strategy', 'jsString']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'detectInterval', 'strategy', 'jsString']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDebugGuardian, self).__init__(**args)

setattr(FefferyDebugGuardian, "__init__", _explicitize_args(FefferyDebugGuardian.__init__))
