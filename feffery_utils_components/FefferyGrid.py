# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyGrid(Component):
    """A FefferyGrid component.
可拖拽网格组件FefferyGrid

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    传入内部的各`FefferyGridItem`组件.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- placeholder (a list of or a singular dash component, string or number; optional):
    组件型，占位元素，用于在`children`为空时呈现相关提示信息.

- height (number; optional):
    网格容器固定像素高度.

- autoSize (boolean; default True):
    当前网格容器是否受内部元素影响调整高度  默认值：`True`.

- compactType (a value equal to: 'vertical', 'horizontal'; default 'vertical'):
    网格项自动调整约束方向，可选项有`'vertical'`、`'horizontal'`  默认值：`'vertical'`.

- margin (list of numbers | dict with strings as keys and values of type list of numbers; default [10, 10]):
    网格容器内子元素之间的像素间距，格式：`[水平间距, 竖直间距]`，也可以传入以断点为键的字典从而实现响应式  默认值：`[10,
    10]`.

- containerPadding (list of numbers | dict with strings as keys and values of type list of numbers; optional):
    用于设置当前网格容器内部像素padding，格式：[x, y]，支持响应式.

- rowHeight (number; default 150):
    网格中每行像素高度  默认值：`150`.

- isDraggable (boolean; default True):
    内部网格项是否可拖拽  默认值：`True`.

- isResizable (boolean; default True):
    内部网格项尺寸是否可调整  默认值：`True`.

- isBounded (boolean; default False):
    是否允许内部网格项拖拽出界  默认值：`False`.

- allowOverlap (boolean; default False):
    是否允许内部网格项重叠  默认值：`False`.

- breakpoints (dict with strings as keys and values of type number; default { lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0 }):
    自定义断点键及对应断点像素宽度值  默认值：`{lg: 1200, md: 996, sm: 768, xs: 480, xxs:
    0}`.

- cols (dict with strings as keys and values of type number | number; default 12):
    与`breakpoints`对应，设置不同断点下网格系统的列数  默认值：`12`.

- layouts (dict; optional):
    配置各网格项.

    `layouts` is a dict with strings as keys and values of type list
    of dicts with keys:

    - i (string; optional):
        对应当前网格项的`key`值.

    - x (number; optional):
        对应当前网格项的锚点`x`单位坐标.

    - y (number; optional):
        对应当前网格项的锚点`y`单位坐标.

    - w (number; optional):
        对应当前网格项的网格单位宽度.

    - h (number; optional):
        对应当前网格项的网格单位高度.

    - minW (number; optional):
        对应当前网格项的最小网格单位宽度  默认值：`0`.

    - maxW (number; optional):
        对应当前网格项的最大网格单位宽度，默认无限制.

    - minH (number; optional):
        对应当前网格项的最小网格单位高度  默认值：`0`.

    - maxH (number; optional):
        对应当前网格项的最大网格单位高度，默认无限制.

    - static (boolean; optional):
        设置当前网格项是否静态  默认值：`False`.

    - isDraggable (boolean; optional):
        设置当前网格项是否允许被拖拽  默认值：`True`.

    - isResizable (boolean; optional):
        设置当前网格项是否允许被调整尺寸  默认值：`True`.

    - isBounded (boolean; optional):
        设置是否为当前网格项施加边界约束  默认值：`False`. | list of dicts with keys:

    - i (string; optional):
        对应当前网格项的`key`值.

    - x (number; optional):
        对应当前网格项的锚点`x`单位坐标.

    - y (number; optional):
        对应当前网格项的锚点`y`单位坐标.

    - w (number; optional):
        对应当前网格项的网格单位宽度.

    - h (number; optional):
        对应当前网格项的网格单位高度.

    - minW (number; optional):
        对应当前网格项的最小网格单位宽度  默认值：`0`.

    - maxW (number; optional):
        对应当前网格项的最大网格单位宽度，默认无限制.

    - minH (number; optional):
        对应当前网格项的最小网格单位高度  默认值：`0`.

    - maxH (number; optional):
        对应当前网格项的最大网格单位高度，默认无限制.

    - static (boolean; optional):
        设置当前网格项是否静态  默认值：`False`.

    - isDraggable (boolean; optional):
        设置当前网格项是否允许被拖拽  默认值：`True`.

    - isResizable (boolean; optional):
        设置当前网格项是否允许被调整尺寸  默认值：`True`.

    - isBounded (boolean; optional):
        设置是否为当前网格项施加边界约束  默认值：`False`. | boolean | number | string | dict | list

- placeholderBackground (string; default '#3b3a39'):
    拖拽预览占位对应`css`的`background`属性  默认值：`'#3b3a39'`.

- placeholderOpacity (number; default 0.2):
    拖拽预览占位对应`css`的`opacity`属性  默认值：`0.2`.

- placeholderBorder (string; default 'none'):
    拖拽预览占位对应`css`的`border`属性  默认值：`'none'`.

- placeholderBorderRadius (string; default '0px'):
    拖拽预览占位对应`css`的`border-radius`属性  默认值：`'0px'`.

- debug (boolean; default False):
    是否开启调试模式，开启后，每次布局参数更新，都会在浏览器开发者工具控制台打印相关参数  默认值：`False`.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['placeholder']
    _base_nodes = ['placeholder', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyGrid'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, placeholder=Component.UNDEFINED, height=Component.UNDEFINED, autoSize=Component.UNDEFINED, compactType=Component.UNDEFINED, margin=Component.UNDEFINED, containerPadding=Component.UNDEFINED, rowHeight=Component.UNDEFINED, isDraggable=Component.UNDEFINED, isResizable=Component.UNDEFINED, isBounded=Component.UNDEFINED, allowOverlap=Component.UNDEFINED, breakpoints=Component.UNDEFINED, cols=Component.UNDEFINED, layouts=Component.UNDEFINED, placeholderBackground=Component.UNDEFINED, placeholderOpacity=Component.UNDEFINED, placeholderBorder=Component.UNDEFINED, placeholderBorderRadius=Component.UNDEFINED, debug=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'placeholder', 'height', 'autoSize', 'compactType', 'margin', 'containerPadding', 'rowHeight', 'isDraggable', 'isResizable', 'isBounded', 'allowOverlap', 'breakpoints', 'cols', 'layouts', 'placeholderBackground', 'placeholderOpacity', 'placeholderBorder', 'placeholderBorderRadius', 'debug', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'placeholder', 'height', 'autoSize', 'compactType', 'margin', 'containerPadding', 'rowHeight', 'isDraggable', 'isResizable', 'isBounded', 'allowOverlap', 'breakpoints', 'cols', 'layouts', 'placeholderBackground', 'placeholderOpacity', 'placeholderBorder', 'placeholderBorderRadius', 'debug', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyGrid, self).__init__(children=children, **args)
