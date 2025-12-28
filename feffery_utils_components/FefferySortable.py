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


class FefferySortable(Component):
    """A FefferySortable component.
排序列表组件FefferySortable

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- handleStyle (dict; optional):
    拖拽手柄css样式.

- handleClassName (string | dict; optional):
    拖拽手柄css类名.

- className (string | dict; optional):
    当前组件css类名.

- items (list of dicts; required):
    必填，定义子项源数组，数组顺序不会受拖拽排序结果影响.

    `items` is a list of dicts with keys:

    - key (number | string; required):
        对应当前子元素唯一标识.

    - content (a list of or a singular dash component, string or number; optional):
        当前子元素内容.

    - style (dict; optional):
        当前子元素容器`css`样式.

    - className (string | dict; optional):
        当前子元素容器`css`类名.

    - draggingStyle (dict; optional):
        当前子元素处于拖拽中状态下的`css`样式.

    - draggingClassName (string | dict; optional):
        当前子元素处于拖拽中状态下的`css`类名.

- direction (a value equal to: 'vertical', 'horizontal'; default 'vertical'):
    排序列表方向，可选项有`'vertical'`、`'horizontal'`  默认值：`'vertical'`.

- itemDraggingScale (number; default 1):
    设置子项处于拖拽中状态下的缩放比例  默认值：`1`.

- handlePosition (a value equal to: 'start', 'end'; default 'end'):
    设置拖拽手柄位置，可选项有`'start'`、`'end'`  默认值：`'end'`.

- handleType (a value equal to: 'holder', 'menu', 'drag'; default 'holder'):
    设置内置的推拽手柄图标类型，可选项有`'holder'`、`'menu'`、`'drag'`  默认值：`'holder'`.

- maxTranslateX (number; optional):
    限制横向拖拽最大像素偏移距离.

- maxTranslateY (number; optional):
    限制纵向拖拽最大像素偏移距离.

- currentOrder (list of number | strings; optional):
    监听或设置当前各子项呈现的顺序.

- value (number | string | list of number | strings; optional):
    设置或监听当前处于选中状态的子项`key`值.

- multiple (boolean; default False):
    是否允许多选  默认值：`False`.

- allowNoValue (boolean; default True):
    是否允许无选中项  默认值：`True`.

- selectedStyle (dict; optional):
    针对已选中项设置额外的`css`样式."""
    _children_props: typing.List[str] = ['items[].content']
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferySortable'
    Items = TypedDict(
        "Items",
            {
            "key": typing.Union[NumberType, str],
            "content": NotRequired[ComponentType],
            "style": NotRequired[dict],
            "className": NotRequired[typing.Union[str, dict]],
            "draggingStyle": NotRequired[dict],
            "draggingClassName": NotRequired[typing.Union[str, dict]]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        handleStyle: typing.Optional[dict] = None,
        handleClassName: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        items: typing.Optional[typing.Sequence["Items"]] = None,
        direction: typing.Optional[Literal["vertical", "horizontal"]] = None,
        itemDraggingScale: typing.Optional[NumberType] = None,
        handlePosition: typing.Optional[Literal["start", "end"]] = None,
        handleType: typing.Optional[Literal["holder", "menu", "drag"]] = None,
        maxTranslateX: typing.Optional[NumberType] = None,
        maxTranslateY: typing.Optional[NumberType] = None,
        currentOrder: typing.Optional[typing.Sequence[typing.Union[NumberType, str]]] = None,
        value: typing.Optional[typing.Union[typing.Union[NumberType, str], typing.Sequence[typing.Union[NumberType, str]]]] = None,
        multiple: typing.Optional[bool] = None,
        allowNoValue: typing.Optional[bool] = None,
        selectedStyle: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'handleStyle', 'handleClassName', 'className', 'items', 'direction', 'itemDraggingScale', 'handlePosition', 'handleType', 'maxTranslateX', 'maxTranslateY', 'currentOrder', 'value', 'multiple', 'allowNoValue', 'selectedStyle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'handleStyle', 'handleClassName', 'className', 'items', 'direction', 'itemDraggingScale', 'handlePosition', 'handleType', 'maxTranslateX', 'maxTranslateY', 'currentOrder', 'value', 'multiple', 'allowNoValue', 'selectedStyle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['items']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferySortable, self).__init__(**args)

setattr(FefferySortable, "__init__", _explicitize_args(FefferySortable.__init__))
