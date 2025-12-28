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


class FefferyBarcode(Component):
    """A FefferyBarcode component.
条形码组件FefferyBarcode

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- renderer (a value equal to: 'img', 'svg', 'canvas'; default 'canvas'):
    渲染类型，可选的有`'img'`、`'svg'`、`'canvas'`  默认值：`'canvas'`.

- value (string; optional):
    设置条形码所表达的信息值.

- format (a value equal to: 'CODE128', 'CODE128A', 'CODE128B', 'CODE128C', 'EAN2', 'EAN5', 'EAN8', 'EAN13', 'UPC', 'CODE39', 'ITF14', 'MSI', 'MSI10', 'MSI11', 'MSI1010', 'MSI1110', 'pharmacode', 'codabar'; default 'CODE128'):
    设置要使用的条形码类型，可选的有`'CODE128'`、`'CODE128A'`、`'CODE128B'`、`'CODE128C'`、`'EAN2'`、`'EAN5'`、`'EAN8'`、`'EAN13'`、`'UPC'`、`'CODE39'`、`'ITF14'`、`'MSI'`、`'MSI10'`、`'MSI11'`、`'MSI1010'`、`'MSI1110'`、`'pharmacode'`、`'codabar'`
    默认值：`'CODE128'`.

- width (number; default 2):
    设置条形码宽度  默认值：`2`.

- height (number; default 100):
    设置条形码高度  默认值：`100`.

- displayValue (boolean; default True):
    设置是否显示条形码所表达的信息值  默认值：`True`.

- text (string; optional):
    设置条形码显示的文本.

- fontOptions (string; default ''):
    设置条形码显示文本的字体样式  默认值：''.

- font (string; default 'monospace'):
    设置条形码显示文本的字体种类  默认值：'monospace'.

- fontSize (number; default 20):
    设置条形码显示文本的字体大小  默认值：`20`.

- textAlign (a value equal to: 'left', 'center', 'right'; default 'center'):
    设置条形码显示文本的水平对齐方式，可选的有`'left'`、`'center'`、`'right'`
    默认值：`'center'`.

- textPosition (a value equal to: 'top', 'bottom'; default 'bottom'):
    设置条形码显示文本的垂直位置，可选的有`'top'`、`'bottom'`  默认值：`'bottom'`.

- textMargin (number; default 2):
    设置条形码和显示文本之间的间距  默认值：`2`.

- background (string; default '#ffffff'):
    设置条形码的背景颜色  默认值：`'#ffffff'`.

- lineColor (string; default '#000000'):
    设置条形码的线条和显示文本颜色  默认值：`'#000000'`.

- margin (number; default 10):
    设置条形码周围的间距边距，如果未设置`marginTop`、`marginBottom`、`marginLeft`、`marginRight`，则这四个参数将继承`margins`的值
    默认值：`10`.

- marginTop (number; optional):
    设置条形码周围的上间距边距.

- marginBottom (number; optional):
    设置条形码周围的下间距边距.

- marginLeft (number; optional):
    设置条形码周围的左间距边距.

- marginRight (number; optional):
    设置条形码周围的右间距边距.

- flat (boolean; default False):
    设置条形码是否保持平整，仅适用于`EAN8`和`EAN13`  默认值：`False`."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyBarcode'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        renderer: typing.Optional[Literal["img", "svg", "canvas"]] = None,
        value: typing.Optional[str] = None,
        format: typing.Optional[Literal["CODE128", "CODE128A", "CODE128B", "CODE128C", "EAN2", "EAN5", "EAN8", "EAN13", "UPC", "CODE39", "ITF14", "MSI", "MSI10", "MSI11", "MSI1010", "MSI1110", "pharmacode", "codabar"]] = None,
        width: typing.Optional[NumberType] = None,
        height: typing.Optional[NumberType] = None,
        displayValue: typing.Optional[bool] = None,
        text: typing.Optional[str] = None,
        fontOptions: typing.Optional[str] = None,
        font: typing.Optional[str] = None,
        fontSize: typing.Optional[NumberType] = None,
        textAlign: typing.Optional[Literal["left", "center", "right"]] = None,
        textPosition: typing.Optional[Literal["top", "bottom"]] = None,
        textMargin: typing.Optional[NumberType] = None,
        background: typing.Optional[str] = None,
        lineColor: typing.Optional[str] = None,
        margin: typing.Optional[NumberType] = None,
        marginTop: typing.Optional[NumberType] = None,
        marginBottom: typing.Optional[NumberType] = None,
        marginLeft: typing.Optional[NumberType] = None,
        marginRight: typing.Optional[NumberType] = None,
        flat: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'renderer', 'value', 'format', 'width', 'height', 'displayValue', 'text', 'fontOptions', 'font', 'fontSize', 'textAlign', 'textPosition', 'textMargin', 'background', 'lineColor', 'margin', 'marginTop', 'marginBottom', 'marginLeft', 'marginRight', 'flat']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'renderer', 'value', 'format', 'width', 'height', 'displayValue', 'text', 'fontOptions', 'font', 'fontSize', 'textAlign', 'textPosition', 'textMargin', 'background', 'lineColor', 'margin', 'marginTop', 'marginBottom', 'marginLeft', 'marginRight', 'flat']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyBarcode, self).__init__(**args)

setattr(FefferyBarcode, "__init__", _explicitize_args(FefferyBarcode.__init__))
