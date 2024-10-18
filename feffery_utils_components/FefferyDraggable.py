# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDraggable(Component):
    """A FefferyDraggable component.
可拖拽组件FefferyDraggable

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- draggable (boolean; default True):
    是否开启可拖拽  默认值：`True`.

- initialX (number; required):
    必填，设置初始状态下当前可拖拽组件左上角距离页面顶端的像素距离.

- initialY (number; required):
    必填，设置初始状态下当前可拖拽组件左上角距离页面左侧的像素距离.

- showDragLine (boolean; default False):
    设置是否在拖拽时显示相关辅助线  默认值：`False`.

- dragLineColors (list of strings; default ['#d9d9d9', '#8c8c8c']):
    设置拖拽辅助线颜色  默认值：`['#d9d9d9', '#8c8c8c']`.

- focusWithinStyle (dict; default {    boxShadow: 'rgba(0, 0, 0, 0.08) 0px 6px 16px -8px, rgba(0, 0, 0, 0.05) 0px 9px 28px, rgba(0, 0, 0, 0.03) 0px 12px 48px 16px'}):
    设置聚焦状态下的额外`css`样式.

- boundsSelector (string; optional):
    设置可拖拽范围边界容器对应的`css`选择器，设置后拖拽将基于*相对-绝对布局*被限制在边界容器内部.

- x (number; optional):
    只读，用于监听当前可拖拽组件左上角距离页面顶端的像素距离.

- y (number; optional):
    只读，用于监听当前可拖拽组件左上角距离页面左侧的像素距离.

- isFocusWithin (boolean; optional):
    只读，用于监听当前可拖拽组件是否处于聚焦状态.

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
    _type = 'FefferyDraggable'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, draggable=Component.UNDEFINED, initialX=Component.REQUIRED, initialY=Component.REQUIRED, showDragLine=Component.UNDEFINED, dragLineColors=Component.UNDEFINED, focusWithinStyle=Component.UNDEFINED, boundsSelector=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, isFocusWithin=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'draggable', 'initialX', 'initialY', 'showDragLine', 'dragLineColors', 'focusWithinStyle', 'boundsSelector', 'x', 'y', 'isFocusWithin', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'draggable', 'initialX', 'initialY', 'showDragLine', 'dragLineColors', 'focusWithinStyle', 'boundsSelector', 'x', 'y', 'isFocusWithin', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['initialX', 'initialY']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyDraggable, self).__init__(children=children, **args)
