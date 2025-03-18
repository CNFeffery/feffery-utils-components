# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyFormatNumber(Component):
    """A FefferyFormatNumber component.
数值格式化组件FefferyFormatNumber

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- value (number; default 0):
    待格式化的原始字节数值  默认值：`0`.

- type (a value equal to: 'decimal', 'percent'; default 'decimal'):
    格式化类型，可选项有`'decimal'`、`'percent'`  默认值：`'decimal'`.

- noGrouping (boolean; default False):
    是否关闭千分位符  默认值：`False`.

- minimumFractionDigits (number; optional):
    最小小数位数.

- maximumFractionDigits (number; optional):
    最大小数位数."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFormatNumber'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        value: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        type: typing.Optional[Literal["decimal", "percent"]] = None,
        noGrouping: typing.Optional[bool] = None,
        minimumFractionDigits: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        maximumFractionDigits: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'value', 'type', 'noGrouping', 'minimumFractionDigits', 'maximumFractionDigits']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'value', 'type', 'noGrouping', 'minimumFractionDigits', 'maximumFractionDigits']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyFormatNumber, self).__init__(**args)
