# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyReload(Component):
    """A FefferyReload component.


Keyword arguments:

- id (string; optional):
    组件id.

- delay (number; optional):
    设置重载执行的延时时长（单位：毫秒）.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- reload (boolean; optional):
    执行页面重载操作的标志，当设置为True时会进行页面重载."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyReload'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, reload=Component.UNDEFINED, delay=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'delay', 'loading_state', 'reload']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'delay', 'loading_state', 'reload']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyReload, self).__init__(**args)
