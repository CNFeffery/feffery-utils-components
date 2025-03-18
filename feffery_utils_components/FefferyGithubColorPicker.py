# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyGithubColorPicker(Component):
    """A FefferyGithubColorPicker component.
Github风格色彩选择器FefferyGithubColorPicker

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- color (string; optional):
    监听或设置当前选中色彩对应16进制颜色值.

- colors (list of strings; default ['#B80000', '#DB3E00', '#FCCB00', '#008B02', '#006B76', '#1273DE', '#004DCF', '#5300EB', '#EB9694', '#FAD0C3', '#FEF3BD', '#C1E1C5', '#BEDADC', '#C4DEF6', '#BED3F3', '#D4C4FB']):
    设置可选色彩对应16进制颜色值数组  默认值：`['#B80000', '#DB3E00', '#FCCB00',
    '#008B02', '#006B76', '#1273DE', '#004DCF', '#5300EB', '#EB9694',
    '#FAD0C3', '#FEF3BD', '#C1E1C5', '#BEDADC', '#C4DEF6', '#BED3F3',
    '#D4C4FB']`.

- triangle (a value equal to: 'hide', 'top-left', 'top-right'; default 'top-left'):
    顶部箭头方位，可选项有`'hide'`、`'top-left'`、`'top-right'`  默认值：`'top-left'`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyGithubColorPicker'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        colors: typing.Optional[typing.Sequence[str]] = None,
        triangle: typing.Optional[Literal["hide", "top-left", "top-right"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'color', 'colors', 'triangle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'color', 'colors', 'triangle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyGithubColorPicker, self).__init__(**args)
