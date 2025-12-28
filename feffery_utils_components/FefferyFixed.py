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


class FefferyFixed(Component):
    """A FefferyFixed component.
固定布局组件FefferyFixed

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- className (string | dict; optional):
    当前组件css类名.

- mode (a value equal to: 'follow-image'; required):
    必填，设置固定布局模式，可选的有`'follow-image'`（跟随对应`css`属性`object-fit`为`contain`的全屏图片）.

- followImageWidth (number; optional):
    当`mode='follow-image'`时，设置跟随目标图片原始像素宽度.

- followImageHeight (number; optional):
    当`mode='follow-image'`时，设置跟随目标图片原始像素高度.

- followImageContainerPosition (list of numbers; optional):
    当`mode='follow-image'`时，以目标图片左上角为原点，当前容器的左上角比例坐标，格式如`[x_ratio,
    y_ratio]`.

- followImageContainerSize (list of numbers; optional):
    当`mode='follow-image'`时，当前容器宽度、高度分别占目标图片对应宽度、高度的比例，格式如`[width_ratio,
    height_ratio]`."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFixed'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        mode: typing.Optional[Literal["follow-image"]] = None,
        followImageWidth: typing.Optional[NumberType] = None,
        followImageHeight: typing.Optional[NumberType] = None,
        followImageContainerPosition: typing.Optional[typing.Sequence[NumberType]] = None,
        followImageContainerSize: typing.Optional[typing.Sequence[NumberType]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'mode', 'followImageWidth', 'followImageHeight', 'followImageContainerPosition', 'followImageContainerSize']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'mode', 'followImageWidth', 'followImageHeight', 'followImageContainerPosition', 'followImageContainerSize']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['mode']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyFixed, self).__init__(children=children, **args)

setattr(FefferyFixed, "__init__", _explicitize_args(FefferyFixed.__init__))
