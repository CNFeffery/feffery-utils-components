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


class FefferyEyeDropper(Component):
    """A FefferyEyeDropper component.
色彩拾取组件FefferyEyeDropper

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- enable (boolean; default False):
    控制激活新一次的色彩拾取，每次完成色彩拾取后都会自动被重置为`False`  默认值：`False`.

- color (string; optional):
    监听最近一次色彩拾取操作对应16进制颜色值."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyEyeDropper'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        enable: typing.Optional[bool] = None,
        color: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'enable', 'color']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'enable', 'color']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyEyeDropper, self).__init__(**args)

setattr(FefferyEyeDropper, "__init__", _explicitize_args(FefferyEyeDropper.__init__))
