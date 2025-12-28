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


class FefferySetFavicon(Component):
    """A FefferySetFavicon component.
favicon设置组件FefferySetFavicon

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- favicon (string; optional):
    用于设置要更新的`favicon`图片文件地址，支持`svg`、`png`、`ico`、`gif`格式."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferySetFavicon'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        favicon: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'favicon']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'favicon']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferySetFavicon, self).__init__(**args)

setattr(FefferySetFavicon, "__init__", _explicitize_args(FefferySetFavicon.__init__))
