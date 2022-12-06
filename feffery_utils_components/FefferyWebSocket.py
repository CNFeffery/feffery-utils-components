# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyWebSocket(Component):
    """A FefferyWebSocket component.


Keyword arguments:

- id (string; optional)

- latestMessage (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- message (string; optional)

- operation (a value equal to: 'connect', 'disconnect', 'send'; optional)

- reconnectInterval (number; optional)

- reconnectLimit (number; optional)

- socketUrl (string; required)

- state (a value equal to: 'connecting', 'open', 'closing', 'closed'; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyWebSocket'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, socketUrl=Component.REQUIRED, reconnectLimit=Component.UNDEFINED, reconnectInterval=Component.UNDEFINED, operation=Component.UNDEFINED, message=Component.UNDEFINED, latestMessage=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'latestMessage', 'loading_state', 'message', 'operation', 'reconnectInterval', 'reconnectLimit', 'socketUrl', 'state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'latestMessage', 'loading_state', 'message', 'operation', 'reconnectInterval', 'reconnectLimit', 'socketUrl', 'state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['socketUrl']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyWebSocket, self).__init__(**args)
