# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCountDown(Component):
    """A FefferyCountDown component.
倒计时组件FefferyCountDown

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- delay (number; optional):
    用于设置距离下一次超时事件触发的倒计时间隔，单位：秒，每次有效的`delay`对应超时事件结束后都会被重置为空值.

- interval (number; default 1):
    设置倒计时时间间隔，单位：秒  默认值：`1`.

- countdown (number; optional):
    监听当前剩余时间秒数.

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
    _type = 'FefferyCountDown'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, delay=Component.UNDEFINED, interval=Component.UNDEFINED, countdown=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'delay', 'interval', 'countdown', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'delay', 'interval', 'countdown', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyCountDown, self).__init__(**args)
