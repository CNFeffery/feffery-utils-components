# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyGrid(Component):
    """A FefferyGrid component.


Keyword arguments:

- id (string; optional):
    组件id.

- children (a list of or a singular dash component, string or number; optional):
    传入内部的各个FefferyGridItem元素.

- placeholder (a list of or a singular dash component, string or number; optional):
    占位元素，用于在children为空时呈现相关提示信息.

- key (string; optional):
    强制刷新用.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- height (number; optional):
    设置网格容器固定像素高度.

- autoSize (boolean; default True):
    设置当前网格容器是否自使用内部元素而调整高度，默认为True.

- compactType (a value equal to: 'vertical', 'horizontal'; default 'vertical'):
    设置网格项的自动调整约束方向，默认无约束.

- margin (list of numbers | dict with strings as keys and values of type list of numbers; default [10, 10]):
    用于设置当前网格容器内子元素之间的像素margin，格式：[x, y]  也可以传入以断点为键的字典从而实现响应式.

- containerPadding (list of numbers | dict with strings as keys and values of type list of numbers; optional):
    用于设置当前网格容器内部像素padding，格式：[x, y]  也可以传入以断点为键的字典从而实现响应式.

- rowHeight (number; default 150):
    用于设置网格中每行的像素高度，默认为150.

- isDraggable (boolean; default True):
    设置是否开启当前网格内部的拖拽行为，默认为True.

- isResizable (boolean; default True):
    设置是否开启当前网格内部的尺寸调整行为，默认为True.

- isBounded (boolean; default False):
    设置是否限制当前网格内部的拖拽行为仅限于内部，默认为False.

- allowOverlap (boolean; default False):
    设置是否允许相互压盖，默认为False.

- breakpoints (dict with strings as keys and values of type number; default { lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0 }):
    用于自定义断点及其对应的像素值映射对象  默认为{lg: 1200, md: 996, sm: 768, xs: 480, xxs:
    0}.

- cols (dict with strings as keys and values of type number | number; default 12):
    与breakpoints对应，用于设置不同断点下网格系统的列数  默认为{lg: 12, md: 10, sm: 6, xs: 4,
    xxs: 2}.

- layouts (dict; optional):
    用于定义不同断点下的各个网格项布局相关参数.

    `layouts` is a dict with strings as keys and values of type list
    of dicts with keys:

    - i (string; optional):
        对应当前网格项的key值.

    - x (number; optional):
        对应当前网格项的锚点x单位坐标.

    - y (number; optional):
        对应当前网格项的锚点y单位坐标.

    - w (number; optional):
        对应当前网格项的网格单位宽度.

    - h (number; optional):
        对应当前网格项的网格单位高度.

    - minW (number; optional):
        对应当前网格项的最小网格单位宽度，默认为0.

    - maxW (number; optional):
        对应当前网格项的最大网格单位宽度，默认无限制.

    - minH (number; optional):
        对应当前网格项的最小网格单位高度，默认为0.

    - maxH (number; optional):
        对应当前网格项的最大网格单位高度，默认无限制.

    - static (boolean; optional):
        设置当前网格项是否静态，默认为False.

    - isDraggable (boolean; optional):
        设置当前网格项是否允许被拖拽，默认为True.

    - isResizable (boolean; optional):
        设置当前网格项是否允许被调整尺寸，默认为True.

    - isBounded (boolean; optional):
        设置是否为当前网格项施加边界约束，默认为False.

    - moved (boolean | number | string | dict | list; optional) | list of dicts with keys:

    - i (string; optional):
        对应当前网格项的key值.

    - x (number; optional):
        对应当前网格项的锚点x单位坐标.

    - y (number; optional):
        对应当前网格项的锚点y单位坐标.

    - w (number; optional):
        对应当前网格项的网格单位宽度.

    - h (number; optional):
        对应当前网格项的网格单位高度.

    - minW (number; optional):
        对应当前网格项的最小网格单位宽度，默认为0.

    - maxW (number; optional):
        对应当前网格项的最大网格单位宽度，默认无限制.

    - minH (number; optional):
        对应当前网格项的最小网格单位高度，默认为0.

    - maxH (number; optional):
        对应当前网格项的最大网格单位高度，默认无限制.

    - static (boolean; optional):
        设置当前网格项是否静态，默认为False.

    - isDraggable (boolean; optional):
        设置当前网格项是否允许被拖拽，默认为True.

    - isResizable (boolean; optional):
        设置当前网格项是否允许被调整尺寸，默认为True.

    - isBounded (boolean; optional):
        设置是否为当前网格项施加边界约束，默认为False.

    - moved (boolean | number | string | dict | list; optional) | boolean | number | string | dict | list

- placeholderBackground (string; default '#3b3a39'):
    自定义样式相关快捷样式参数  自定义拖拽预览占位的background属性，默认为'#3b3a39'.

- placeholderOpacity (number; default 0.2):
    自定义拖拽预览占位的opacity属性，默认为0.2.

- placeholderBorder (string; default 'none'):
    自定义拖拽预览占位的border属性，默认为'none'.

- placeholderBorderRadius (string; default '0px'):
    自定义拖拽预览占位的border-radius属性，默认为'0px'.

- debug (boolean; default False):
    设置是否开启debug模式，开启后，每次布局参数更新，都会在浏览器开发者工具控制台进行打印  默认：False.

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
    def __init__(self, children=None, id=Component.UNDEFINED, placeholder=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, height=Component.UNDEFINED, autoSize=Component.UNDEFINED, compactType=Component.UNDEFINED, margin=Component.UNDEFINED, containerPadding=Component.UNDEFINED, rowHeight=Component.UNDEFINED, isDraggable=Component.UNDEFINED, isResizable=Component.UNDEFINED, isBounded=Component.UNDEFINED, allowOverlap=Component.UNDEFINED, breakpoints=Component.UNDEFINED, cols=Component.UNDEFINED, layouts=Component.UNDEFINED, placeholderBackground=Component.UNDEFINED, placeholderOpacity=Component.UNDEFINED, placeholderBorder=Component.UNDEFINED, placeholderBorderRadius=Component.UNDEFINED, debug=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'children', 'placeholder', 'key', 'style', 'className', 'height', 'autoSize', 'compactType', 'margin', 'containerPadding', 'rowHeight', 'isDraggable', 'isResizable', 'isBounded', 'allowOverlap', 'breakpoints', 'cols', 'layouts', 'placeholderBackground', 'placeholderOpacity', 'placeholderBorder', 'placeholderBorderRadius', 'debug', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'children', 'placeholder', 'key', 'style', 'className', 'height', 'autoSize', 'compactType', 'margin', 'containerPadding', 'rowHeight', 'isDraggable', 'isResizable', 'isBounded', 'allowOverlap', 'breakpoints', 'cols', 'layouts', 'placeholderBackground', 'placeholderOpacity', 'placeholderBorder', 'placeholderBorderRadius', 'debug', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyGrid, self).__init__(children=children, **args)
