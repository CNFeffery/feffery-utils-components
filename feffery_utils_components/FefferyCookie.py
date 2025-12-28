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


class FefferyCookie(Component):
    """A FefferyCookie component.
Cookie控制组件FefferyCookie

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- cookieKey (string; required):
    必填，设置要绑定的`cookie`键名.

- defaultValue (string; optional):
    为当前所绑定的`cookie`设定缺省时的默认值，当所绑定的`cookie`本身有值时，该值将不会影响原本的`cookie`值.

- value (string; optional):
    用于更新当前绑定的`cookie`值.

- expires (number; optional):
    设置当前`cookie`值的有效存储时间，单位：秒.

- pathname (string; default '/'):
    设置当前`cookie`值可用的`pathname`  默认值：`'/'`.

- secure (boolean; default False):
    设置当前`cookie`是否仅允许通过`https`安全传输  默认值：`False`."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCookie'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        cookieKey: typing.Optional[str] = None,
        defaultValue: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        expires: typing.Optional[NumberType] = None,
        pathname: typing.Optional[str] = None,
        secure: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'cookieKey', 'defaultValue', 'value', 'expires', 'pathname', 'secure']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'cookieKey', 'defaultValue', 'value', 'expires', 'pathname', 'secure']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['cookieKey']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyCookie, self).__init__(**args)

setattr(FefferyCookie, "__init__", _explicitize_args(FefferyCookie.__init__))
