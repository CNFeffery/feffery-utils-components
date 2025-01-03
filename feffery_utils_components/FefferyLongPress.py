# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyLongPress(Component):
    """A FefferyLongPress component.
长按事件监听组件FefferyLongPress

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- targetId (string; optional):
    设置当前长按监听组件的监听目标元素`id`.

- pressCounts (number; default 0):
    监听目标组件累计被长按次数  默认值：`0`.

- isLongPressing (boolean; optional):
    监听目标组件是否正处于长按状态.

- delay (number; default 300):
    设置符合长按行为的持续时长，单位：毫秒  默认值：`300`.

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
    _type = 'FefferyLongPress'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, targetId=Component.UNDEFINED, pressCounts=Component.UNDEFINED, isLongPressing=Component.UNDEFINED, delay=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'targetId', 'pressCounts', 'isLongPressing', 'delay', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'targetId', 'pressCounts', 'isLongPressing', 'delay', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyLongPress, self).__init__(**args)
