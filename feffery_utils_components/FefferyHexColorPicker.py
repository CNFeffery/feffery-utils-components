# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyHexColorPicker(Component):
    """A FefferyHexColorPicker component.
16进制色彩选择器FefferyHexColorPicker

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- color (string; default '#44cef6'):
    监听或设置当前选中色彩对应16进制颜色值  默认值：`'#36a0f8'`.

- showAlpha (boolean; default False):
    是否显示透明度选择控件  默认值：`False`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyHexColorPicker'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        showAlpha: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'color', 'showAlpha']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'color', 'showAlpha']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyHexColorPicker, self).__init__(**args)
