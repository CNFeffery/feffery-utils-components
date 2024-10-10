# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyResizable(Component):
    """A FefferyResizable component.


Keyword arguments:

- id (string; optional):
    组件id.

- key (string; optional)

- children (a list of or a singular dash component, string or number; optional):
    设置内部嵌套的子元素.

- className (string; optional):
    设置css类名.

- style (dict; optional):
    设置css样式.

- defaultSize (dict; optional):
    设置尺寸调整组件初始化时的宽度、高度，可传入如300、'300px'、'50%'、'50vh'等形式.

    `defaultSize` is a dict with keys:

    - width (number | string; optional):
        设置宽度.

    - height (number | string; optional):
        设置高度.

- size (dict; optional):
    监听或设置尺寸调整组件的宽度、高度，可传入如300、'300px'、'50%'、'50vh'等形式.

    `size` is a dict with keys:

    - width (number | string; optional):
        设置宽度.

    - height (number | string; optional):
        设置高度.

- minWidth (number | string; default 10):
    设置尺寸调整组件的最小宽度，默认为10.

- minHeight (number | string; default 10):
    设置尺寸调整组件的最小高度，默认为10.

- maxWidth (number | string; optional):
    设置尺寸调整组件的最大宽度.

- maxHeight (number | string; optional):
    设置尺寸调整组件的最大高度.

- direction (list of a value equal to: 'top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft's; default ['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft']):
    设置允许进行尺寸调整的方向，多选，可选项有'top'、'right'、'bottom'、'left'、'topRight'、'bottomRight'、'bottomLeft'、'topLeft'
    默认为['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight',
    'bottomLeft', 'topLeft'].

- grid (list of numbers; default [1, 1]):
    设置尺寸调整在水平和竖直方向上的最小调整像素步长，默认为[1, 1].

- bounds (a value equal to: 'window', 'parent'; default 'window'):
    设置尺寸调整组件的外边界类型，可选的有'window'、'parent'  默认为'window'.

- boundsSelector (string; optional):
    用于指定边界元素的css选择器，优先级高于bounds.

- handleStyles (dict; optional):
    用于分别设置不同方向上拖拽控件部分的css样式.

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
    用于分别设置不同方向上拖拽控件部分的css类名.

    `handleClassNames` is a dict with keys:

    - top (string; optional)

    - right (string; optional)

    - bottom (string; optional)

    - left (string; optional)

    - topRight (string; optional)

    - bottomRight (string; optional)

    - bottomLeft (string; optional)

    - topLeft (string; optional)

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
    _type = 'FefferyResizable'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, defaultSize=Component.UNDEFINED, size=Component.UNDEFINED, minWidth=Component.UNDEFINED, minHeight=Component.UNDEFINED, maxWidth=Component.UNDEFINED, maxHeight=Component.UNDEFINED, direction=Component.UNDEFINED, grid=Component.UNDEFINED, bounds=Component.UNDEFINED, boundsSelector=Component.UNDEFINED, handleStyles=Component.UNDEFINED, handleClassNames=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'className', 'style', 'defaultSize', 'size', 'minWidth', 'minHeight', 'maxWidth', 'maxHeight', 'direction', 'grid', 'bounds', 'boundsSelector', 'handleStyles', 'handleClassNames', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'className', 'style', 'defaultSize', 'size', 'minWidth', 'minHeight', 'maxWidth', 'maxHeight', 'direction', 'grid', 'bounds', 'boundsSelector', 'handleStyles', 'handleClassNames', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyResizable, self).__init__(children=children, **args)
