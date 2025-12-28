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


class FefferyResizable(Component):
    """A FefferyResizable component.
尺寸调整组件FefferyResizable

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，设置内部嵌套的子元素.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- defaultSize (dict; optional):
    设置尺寸调整组件初始化时的宽度和高度，可传入如`300`、`'300px'`、`'50%'`、`'50vh'`等形式.

    `defaultSize` is a dict with keys:

    - width (number | string; optional):
        设置宽度.

    - height (number | string; optional):
        设置高度.

- size (dict; optional):
    监听或设置尺寸调整组件的宽度和高度，可传入如`300`、`'300px'`、`'50%'`、`'50vh'`等形式.

    `size` is a dict with keys:

    - width (number | string; optional):
        设置宽度.

    - height (number | string; optional):
        设置高度.

- minWidth (number | string; default 10):
    设置尺寸调整组件的最小宽度  默认值：`10`.

- minHeight (number | string; default 10):
    设置尺寸调整组件的最小高度  默认值：`10`.

- maxWidth (number | string; optional):
    设置尺寸调整组件的最大宽度.

- maxHeight (number | string; optional):
    设置尺寸调整组件的最大高度.

- direction (list of a value equal to: 'top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft's; default ['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft']):
    设置允许进行尺寸调整的方向，多选，可选项有`'top'`、`'right'`、`'bottom'`、`'left'`、`'topRight'`、`'bottomRight'`、`'bottomLeft'`、`'topLeft'`
    默认值：`['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight',
    'bottomLeft', 'topLeft']`.

- grid (list of numbers; default [1, 1]):
    设置尺寸调整在水平和竖直方向上的最小调整像素步长  默认值：`[1, 1]`.

- bounds (a value equal to: 'window', 'parent'; default 'window'):
    设置尺寸调整组件的外边界类型，可选的有`'window'`、`'parent'`  默认值：`'window'`.

- boundsSelector (string; optional):
    用于指定边界元素的`css`选择器，优先级高于`bounds`.

- handleStyles (dict; optional):
    用于分别设置不同方向上拖拽控件部分的`css`样式.

    `handleStyles` is a dict with keys:

    - top (dict; optional)

    - right (dict; optional)

    - bottom (dict; optional)

    - left (dict; optional)

    - topRight (dict; optional)

    - bottomRight (dict; optional)

    - bottomLeft (dict; optional)

    - topLeft (dict; optional)

- handleClassNames (dict; optional):
    用于分别设置不同方向上拖拽控件部分的`css`类名.

    `handleClassNames` is a dict with keys:

    - top (string; optional)

    - right (string; optional)

    - bottom (string; optional)

    - left (string; optional)

    - topRight (string; optional)

    - bottomRight (string; optional)

    - bottomLeft (string; optional)

    - topLeft (string; optional)"""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyResizable'
    DefaultSize = TypedDict(
        "DefaultSize",
            {
            "width": NotRequired[typing.Union[NumberType, str]],
            "height": NotRequired[typing.Union[NumberType, str]]
        }
    )

    Size = TypedDict(
        "Size",
            {
            "width": NotRequired[typing.Union[NumberType, str]],
            "height": NotRequired[typing.Union[NumberType, str]]
        }
    )

    HandleStyles = TypedDict(
        "HandleStyles",
            {
            "top": NotRequired[dict],
            "right": NotRequired[dict],
            "bottom": NotRequired[dict],
            "left": NotRequired[dict],
            "topRight": NotRequired[dict],
            "bottomRight": NotRequired[dict],
            "bottomLeft": NotRequired[dict],
            "topLeft": NotRequired[dict]
        }
    )

    HandleClassNames = TypedDict(
        "HandleClassNames",
            {
            "top": NotRequired[str],
            "right": NotRequired[str],
            "bottom": NotRequired[str],
            "left": NotRequired[str],
            "topRight": NotRequired[str],
            "bottomRight": NotRequired[str],
            "bottomLeft": NotRequired[str],
            "topLeft": NotRequired[str]
        }
    )


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        defaultSize: typing.Optional["DefaultSize"] = None,
        size: typing.Optional["Size"] = None,
        minWidth: typing.Optional[typing.Union[NumberType, str]] = None,
        minHeight: typing.Optional[typing.Union[NumberType, str]] = None,
        maxWidth: typing.Optional[typing.Union[NumberType, str]] = None,
        maxHeight: typing.Optional[typing.Union[NumberType, str]] = None,
        direction: typing.Optional[typing.Sequence[Literal["top", "right", "bottom", "left", "topRight", "bottomRight", "bottomLeft", "topLeft"]]] = None,
        grid: typing.Optional[typing.Sequence[NumberType]] = None,
        bounds: typing.Optional[Literal["window", "parent"]] = None,
        boundsSelector: typing.Optional[str] = None,
        handleStyles: typing.Optional["HandleStyles"] = None,
        handleClassNames: typing.Optional["HandleClassNames"] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'defaultSize', 'size', 'minWidth', 'minHeight', 'maxWidth', 'maxHeight', 'direction', 'grid', 'bounds', 'boundsSelector', 'handleStyles', 'handleClassNames']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'defaultSize', 'size', 'minWidth', 'minHeight', 'maxWidth', 'maxHeight', 'direction', 'grid', 'bounds', 'boundsSelector', 'handleStyles', 'handleClassNames']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyResizable, self).__init__(children=children, **args)

setattr(FefferyResizable, "__init__", _explicitize_args(FefferyResizable.__init__))
