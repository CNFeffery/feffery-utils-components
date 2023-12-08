# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyResizable(Component):
    """A FefferyResizable component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    设置内部嵌套的子元素.

- id (string; optional):
    组件id.

- bounds (a value equal to: 'window', 'parent'; default 'window'):
    设置尺寸调整组件的外边界类型，可选的有'window'、'parent'  默认为'window'.

- className (string; optional):
    设置css类名.

- defaultSize (dict; optional):
    监听或设置尺寸调整组件初始化时的宽度、高度，可传入如300、'300px'、'50%'、'50vh'等形式.

    `defaultSize` is a dict with keys:

    - height (number | string; optional):
        设置高度.

    - width (number | string; optional):
        设置宽度.

- direction (list of a value equal to: 'top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft's; default ['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft']):
    设置允许进行尺寸调整的方向，多选，可选项有'top'、'right'、'bottom'、'left'、'topRight'、'bottomRight'、'bottomLeft'、'topLeft'
    默认为['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight',
    'bottomLeft', 'topLeft'].

- grid (list of numbers; default [1, 1]):
    设置尺寸调整在水平和竖直方向上的最小调整像素步长，默认为[1, 1].

- handleClassNames (dict; optional):
    用于分别设置不同方向上拖拽控件部分的css类名.

    `handleClassNames` is a dict with keys:

    - bottom (string; optional)

    - bottomLeft (string; optional)

    - bottomRight (string; optional)

    - left (string; optional)

    - right (string; optional)

    - top (string; optional)

    - topLeft (string; optional)

    - topRight (string; optional)

- handleStyles (dict; optional):
    用于分别设置不同方向上拖拽控件部分的css样式.

    `handleStyles` is a dict with keys:

    - bottom (dict; optional)

    - bottomLeft (dict; optional)

    - bottomRight (dict; optional)

    - left (dict; optional)

    - right (dict; optional)

    - top (dict; optional)

    - topLeft (dict; optional)

    - topRight (dict; optional)

- key (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- maxHeight (number | string; optional):
    设置尺寸调整组件的最大高度.

- maxWidth (number | string; optional):
    设置尺寸调整组件的最大宽度.

- minHeight (number | string; default 10):
    设置尺寸调整组件的最小高度，默认为10.

- minWidth (number | string; default 10):
    设置尺寸调整组件的最小宽度，默认为10.

- style (dict; optional):
    设置css样式."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyResizable'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, defaultSize=Component.UNDEFINED, minWidth=Component.UNDEFINED, minHeight=Component.UNDEFINED, maxWidth=Component.UNDEFINED, maxHeight=Component.UNDEFINED, direction=Component.UNDEFINED, grid=Component.UNDEFINED, bounds=Component.UNDEFINED, handleStyles=Component.UNDEFINED, handleClassNames=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bounds', 'className', 'defaultSize', 'direction', 'grid', 'handleClassNames', 'handleStyles', 'key', 'loading_state', 'maxHeight', 'maxWidth', 'minHeight', 'minWidth', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bounds', 'className', 'defaultSize', 'direction', 'grid', 'handleClassNames', 'handleStyles', 'key', 'loading_state', 'maxHeight', 'maxWidth', 'minHeight', 'minWidth', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyResizable, self).__init__(children=children, **args)
