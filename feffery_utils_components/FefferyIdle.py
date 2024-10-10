# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyIdle(Component):
    """A FefferyIdle component.


Keyword arguments:

- id (string; optional):
    组件id.

- isIdle (boolean; optional):
    监听当前应用是否处于闲置状态.

- waitDuration (number; default 3000):
    设置经过多长时间（单位：毫秒）没有操作后视作闲置状态  默认：3000.

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
    _type = 'FefferyIdle'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, isIdle=Component.UNDEFINED, waitDuration=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'isIdle', 'waitDuration', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'isIdle', 'waitDuration', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyIdle, self).__init__(**args)
