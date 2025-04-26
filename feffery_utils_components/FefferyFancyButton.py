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


class FefferyFancyButton(Component):
    """A FefferyFancyButton component.
美观按钮组件FefferyFancyButton

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- className (string | dict; optional):
    当前组件css类名.

- nClicks (number; default 0):
    按钮累计点击次数，用于监听按钮点击行为  默认值：`0`.

- debounceWait (number; default 0):
    按钮点击事件监听防抖延时，单位：毫秒  默认值：`0`.

- type (a value equal to: 'primary', 'secondary', 'danger'; optional):
    按钮类型，可选项有`'primary'`、`'secondary'`、`'danger'`  默认值：`'primary'`.

- disabled (boolean; optional):
    是否禁用当前组件  默认值：`False`.

- href (string; optional):
    按钮点击跳转链接地址.

- target (string; default '_blank'):
    按钮点击跳转链接方式  默认值：`'_blank'`.

- before (a list of or a singular dash component, string or number; optional):
    组件型，按钮前缀元素.

- after (a list of or a singular dash component, string or number; optional):
    组件型，按钮后缀元素.

- ripple (boolean; optional):
    是否开启点击涟漪效果  默认值：`False`."""
    _children_props = ['before', 'after']
    _base_nodes = ['before', 'after', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFancyButton'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        nClicks: typing.Optional[NumberType] = None,
        debounceWait: typing.Optional[NumberType] = None,
        type: typing.Optional[Literal["primary", "secondary", "danger"]] = None,
        disabled: typing.Optional[bool] = None,
        href: typing.Optional[str] = None,
        target: typing.Optional[str] = None,
        before: typing.Optional[ComponentType] = None,
        after: typing.Optional[ComponentType] = None,
        ripple: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'nClicks', 'debounceWait', 'type', 'disabled', 'href', 'target', 'before', 'after', 'ripple']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'nClicks', 'debounceWait', 'type', 'disabled', 'href', 'target', 'before', 'after', 'ripple']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyFancyButton, self).__init__(children=children, **args)

setattr(FefferyFancyButton, "__init__", _explicitize_args(FefferyFancyButton.__init__))
