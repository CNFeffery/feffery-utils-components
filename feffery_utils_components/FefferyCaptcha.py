# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyCaptcha(Component):
    """A FefferyCaptcha component.
验证码组件FefferyCaptcha

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- captcha (string; optional):
    对应当前的验证码字符串.

- charNum (number; default 4):
    设置验证码字符数量.

- height (number; optional):
    设置验证码的像素高度  默认值：`40`.

- width (number; optional):
    设置验证码的像素宽度  默认值：`100`.

- bgColor (string; optional):
    设置验证码图片背景色  默认值：`'#DFF0D8'`.

- fontSize (number; optional):
    设置验证码字体像素大小  默认值：`25`.

- refresh (boolean; optional):
    用于手动刷新验证码，当传入`True`时会强制刷新验证码，再自动重置为`False`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCaptcha'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        captcha: typing.Optional[str] = None,
        charNum: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        height: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        width: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        bgColor: typing.Optional[str] = None,
        fontSize: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        refresh: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'captcha', 'charNum', 'height', 'width', 'bgColor', 'fontSize', 'refresh']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'captcha', 'charNum', 'height', 'width', 'bgColor', 'fontSize', 'refresh']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyCaptcha, self).__init__(**args)
