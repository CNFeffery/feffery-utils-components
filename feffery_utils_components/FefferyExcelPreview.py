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


class FefferyExcelPreview(Component):
    """A FefferyExcelPreview component.
excel文件预览组件FefferyExcelPreview

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- src (string; required):
    必填，设置目标`excel`文件资源地址.

- minColLength (number; optional):
    至少渲染的列数，当设置为`0`时会自动根据数据列数进行渲染.

- minRowLength (number; optional):
    至少渲染的行数，当设置为`0`时会自动根据数据行数进行渲染.

- widthOffset (number; optional):
    默认列宽的基础上额外增加的像素列宽.

- heightOffset (number; optional):
    默认行高的基础上额外增加的像素行高."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyExcelPreview'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        src: typing.Optional[str] = None,
        minColLength: typing.Optional[NumberType] = None,
        minRowLength: typing.Optional[NumberType] = None,
        widthOffset: typing.Optional[NumberType] = None,
        heightOffset: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'src', 'minColLength', 'minRowLength', 'widthOffset', 'heightOffset']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'src', 'minColLength', 'minRowLength', 'widthOffset', 'heightOffset']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['src']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyExcelPreview, self).__init__(**args)

setattr(FefferyExcelPreview, "__init__", _explicitize_args(FefferyExcelPreview.__init__))
