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


class FefferyQRCode(Component):
    """A FefferyQRCode component.
二维码生成组件FefferyQRCode

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- value (string; required):
    设置二维码所表达的信息值.

- size (number; default 128):
    二维码像素边长  默认值：`128`.

- bgColor (string; default '#FFFFFF'):
    背景色  默认值：`'#FFFFFF'`.

- fgColor (string; default '#000000'):
    前景色  默认值：`'#000000'`.

- level (a value equal to: 'L', 'M', 'Q', 'H'; default 'L'):
    解析精度，可选项有`'L'`、'M'、'Q'、'H'  默认值：`'L'`.

- includeMargin (boolean; default False):
    是否添加外边距  默认值：`False`.

- imageSettings (dict; optional):
    配置二维码中心图片信息.

    `imageSettings` is a dict with keys:

    - src (string; optional):
        图片地址.

    - height (number; optional):
        图片像素高度，默认为二维码`size`的`10%`.

    - width (number; optional):
        图片像素宽度，默认为二维码`size`的`10%`.

    - excavate (boolean; optional):
        图片四周是否添加环绕白边  默认值：`True`.

- renderer (a value equal to: 'svg', 'canvas'; default 'svg'):
    指定渲染引擎，可选项有`'svg'`、`'canvas'`  默认值：`'svg'`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyQRCode'
    ImageSettings = TypedDict(
        "ImageSettings",
            {
            "src": NotRequired[str],
            "height": NotRequired[NumberType],
            "width": NotRequired[NumberType],
            "excavate": NotRequired[bool]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        size: typing.Optional[NumberType] = None,
        bgColor: typing.Optional[str] = None,
        fgColor: typing.Optional[str] = None,
        level: typing.Optional[Literal["L", "M", "Q", "H"]] = None,
        includeMargin: typing.Optional[bool] = None,
        imageSettings: typing.Optional["ImageSettings"] = None,
        renderer: typing.Optional[Literal["svg", "canvas"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'value', 'size', 'bgColor', 'fgColor', 'level', 'includeMargin', 'imageSettings', 'renderer']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'value', 'size', 'bgColor', 'fgColor', 'level', 'includeMargin', 'imageSettings', 'renderer']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['value']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyQRCode, self).__init__(**args)

setattr(FefferyQRCode, "__init__", _explicitize_args(FefferyQRCode.__init__))
