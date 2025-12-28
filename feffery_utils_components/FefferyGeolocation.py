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


class FefferyGeolocation(Component):
    """A FefferyGeolocation component.
地理位置监听组件FefferyGeolocation

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- geoLocationInfo (dict; optional):
    监听当前用户地理位置相关信息."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyGeolocation'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        geoLocationInfo: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'geoLocationInfo']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'geoLocationInfo']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyGeolocation, self).__init__(**args)

setattr(FefferyGeolocation, "__init__", _explicitize_args(FefferyGeolocation.__init__))
