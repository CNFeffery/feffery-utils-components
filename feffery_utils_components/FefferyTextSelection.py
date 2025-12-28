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


class FefferyTextSelection(Component):
    """A FefferyTextSelection component.
文字选中监听组件FefferyTextSelection

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- targetId (string; optional):
    设置目标监听容器`id`.

- targetSelector (string; optional):
    设置目标监听容器对应的`css`选择器.

- targetType (a value equal to: 'id', 'selector'; default 'id'):
    设置目标监听规则类型，可选项有`'id'`、`'selector'`  默认值：`'id'`.

- selectedTextInfo (dict; optional):
    监听最近一次目标容器内文本选中事件相关信息."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTextSelection'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        targetId: typing.Optional[str] = None,
        targetSelector: typing.Optional[str] = None,
        targetType: typing.Optional[Literal["id", "selector"]] = None,
        selectedTextInfo: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'targetId', 'targetSelector', 'targetType', 'selectedTextInfo']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'targetId', 'targetSelector', 'targetType', 'selectedTextInfo']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyTextSelection, self).__init__(**args)

setattr(FefferyTextSelection, "__init__", _explicitize_args(FefferyTextSelection.__init__))
