# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyFancyMessage(Component):
    """A FefferyFancyMessage component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    组件子元素.

- id (string; optional):
    组件id.

- key (string; optional):
    辅助刷新用唯一标识key值.

- className (string; optional):
    设置容器的css类名.

- style (dict; optional):
    设置容器的css样式.

- visible (boolean; default True):
    主动设置是否可见，默认为False.

- position (a value equal to: 'top-left', 'top-center', 'top-right', 'bottom-left', 'bottom-center', 'bottom-right'; default 'top-center'):
    设置消息提示的弹出方位，可选的有'top-left'、'top-center'、'top-right'、'bottom-left'、'bottom-center'、'bottom-right'，默认为'top-center'.

- reverseOrder (boolean; default True):
    设置较新的消息提示是否从底部进行追加，默认为True.

- containerClassName (string; optional):
    设置容器的css类名.

- containerStyle (dict; optional):
    设置容器的css样式.

- gutter (number; default 8):
    设置相邻消息提示之间的像素间距，默认为8.

- type (a value equal to: 'blank', 'success', 'error'; default 'blank'):
    设置信息类型，可选的有'blank', 'success', 'error'  默认为'blank'.

- duration (number; default 4000):
    设置消息提示显示时长（单位：毫秒），默认为4000.

- icon (a list of or a singular dash component, string or number; optional):
    自定义消息提示图标.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['icon']
    _base_nodes = ['icon', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFancyMessage'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, visible=Component.UNDEFINED, position=Component.UNDEFINED, reverseOrder=Component.UNDEFINED, containerClassName=Component.UNDEFINED, containerStyle=Component.UNDEFINED, gutter=Component.UNDEFINED, type=Component.UNDEFINED, duration=Component.UNDEFINED, icon=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'key', 'className', 'style', 'visible', 'position', 'reverseOrder', 'containerClassName', 'containerStyle', 'gutter', 'type', 'duration', 'icon', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'key', 'className', 'style', 'visible', 'position', 'reverseOrder', 'containerClassName', 'containerStyle', 'gutter', 'type', 'duration', 'icon', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyFancyMessage, self).__init__(children=children, **args)
