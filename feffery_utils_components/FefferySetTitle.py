# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferySetTitle(Component):
    """A FefferySetTitle component.
页面title设置组件FefferySetTitle

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- title (string; optional):
    用于设置要更新的`title`信息.

- originTitle (string; optional):
    当`title`参数为空，或当前组件从页面中卸载后应当还原的`title`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferySetTitle'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        originTitle: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'title', 'originTitle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'title', 'originTitle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferySetTitle, self).__init__(**args)
