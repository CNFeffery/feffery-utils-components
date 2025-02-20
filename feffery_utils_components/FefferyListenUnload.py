# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyListenUnload(Component):
    """A FefferyListenUnload component.
页面关闭监听组件FefferyListenUnload

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- unloaded (boolean; optional):
    监听页面重载或关闭事件，每次页面关闭时会触发更新为`True`.

- confirmBeforeUnload (boolean; default False):
    是否在用户重载或关闭当前页面时，添加二次确认  默认值：`False`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyListenUnload'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        unloaded: typing.Optional[bool] = None,
        confirmBeforeUnload: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'unloaded', 'confirmBeforeUnload']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'unloaded', 'confirmBeforeUnload']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyListenUnload, self).__init__(**args)
