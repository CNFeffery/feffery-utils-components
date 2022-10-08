# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyFancyMessage(Component):
    """A FefferyFancyMessage component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- containerClassName (string; optional)

- containerStyle (dict; optional)

- duration (number; default 4000)

- gutter (number; default 8)

- icon (a list of or a singular dash component, string or number; optional)

- key (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- position (a value equal to: 'top-left', 'top-center', 'top-right', 'bottom-left', 'bottom-center', 'bottom-right'; default 'top-center')

- reverseOrder (boolean; default True)

- style (dict; optional)

- type (a value equal to: 'blank', 'success', 'error'; default 'blank')

- visible (boolean; default True)"""
    _children_props = ['icon']
    _base_nodes = ['icon', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFancyMessage'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, visible=Component.UNDEFINED, position=Component.UNDEFINED, reverseOrder=Component.UNDEFINED, containerClassName=Component.UNDEFINED, containerStyle=Component.UNDEFINED, gutter=Component.UNDEFINED, type=Component.UNDEFINED, duration=Component.UNDEFINED, icon=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'containerClassName', 'containerStyle', 'duration', 'gutter', 'icon', 'key', 'loading_state', 'position', 'reverseOrder', 'style', 'type', 'visible']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'containerClassName', 'containerStyle', 'duration', 'gutter', 'icon', 'key', 'loading_state', 'position', 'reverseOrder', 'style', 'type', 'visible']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyFancyMessage, self).__init__(children=children, **args)
