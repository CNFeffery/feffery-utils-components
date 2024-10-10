# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyLongPress(Component):
    """A FefferyLongPress component.


Keyword arguments:

- id (string; optional):
    组件id.

- targetId (string; optional):
    设置当前长按监听组件的监听目标元素id.

- pressCounts (number; default 0):
    监听目标组件累计被长按次数  默认：0.

- delay (number; default 300):
    设置符合长按行为的持续时长，单位：毫秒  默认：300.

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
    def __init__(self, id=Component.UNDEFINED, targetId=Component.UNDEFINED, pressCounts=Component.UNDEFINED, delay=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'targetId', 'pressCounts', 'delay', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'targetId', 'pressCounts', 'delay', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyLongPress, self).__init__(**args)
