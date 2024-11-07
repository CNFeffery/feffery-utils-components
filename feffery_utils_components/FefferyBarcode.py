# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyBarcode(Component):
    """A FefferyBarcode component.
条形码组件FefferyBarcode

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

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
    设置条形码是否保持平整，仅适用于`EAN8`和`EAN13`  默认值：`False`.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyBarcode'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, renderer=Component.UNDEFINED, value=Component.UNDEFINED, format=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, displayValue=Component.UNDEFINED, text=Component.UNDEFINED, fontOptions=Component.UNDEFINED, font=Component.UNDEFINED, fontSize=Component.UNDEFINED, textAlign=Component.UNDEFINED, textPosition=Component.UNDEFINED, textMargin=Component.UNDEFINED, background=Component.UNDEFINED, lineColor=Component.UNDEFINED, margin=Component.UNDEFINED, marginTop=Component.UNDEFINED, marginBottom=Component.UNDEFINED, marginLeft=Component.UNDEFINED, marginRight=Component.UNDEFINED, flat=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'renderer', 'value', 'format', 'width', 'height', 'displayValue', 'text', 'fontOptions', 'font', 'fontSize', 'textAlign', 'textPosition', 'textMargin', 'background', 'lineColor', 'margin', 'marginTop', 'marginBottom', 'marginLeft', 'marginRight', 'flat', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'renderer', 'value', 'format', 'width', 'height', 'displayValue', 'text', 'fontOptions', 'font', 'fontSize', 'textAlign', 'textPosition', 'textMargin', 'background', 'lineColor', 'margin', 'marginTop', 'marginBottom', 'marginLeft', 'marginRight', 'flat', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyBarcode, self).__init__(**args)
