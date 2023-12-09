# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyTimeout(Component):
    """A FefferyTimeout component.


Keyword arguments:

- id (string; optional):
    组件id.

- delay (number; optional):
    用于设置距离下一次超时事件触发的倒计时间隔（单位：毫秒），  每次有效的delay对应超时事件结束后都会被重置为undefined.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- timeoutCount (number; default 0):
    监听超时事件完成次数，默认为0."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTimeout'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, timeoutCount=Component.UNDEFINED, delay=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'delay', 'loading_state', 'timeoutCount']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'delay', 'loading_state', 'timeoutCount']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyTimeout, self).__init__(**args)
