# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyFancyButton(Component):
    """A FefferyFancyButton component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- after (a list of or a singular dash component, string or number; optional)

- before (a list of or a singular dash component, string or number; optional)

- className (string | dict; optional)

- debounceWait (number; default 0)

- disabled (boolean; optional)

- href (string; optional)

- key (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- nClicks (number; default 0)

- ripple (boolean; optional)

- style (dict; optional)

- target (string; default '_blank')

- type (a value equal to: 'primary', 'secondary', 'danger'; optional)"""
    _children_props = ['before', 'after']
    _base_nodes = ['before', 'after', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFancyButton'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, nClicks=Component.UNDEFINED, debounceWait=Component.UNDEFINED, type=Component.UNDEFINED, disabled=Component.UNDEFINED, href=Component.UNDEFINED, target=Component.UNDEFINED, before=Component.UNDEFINED, after=Component.UNDEFINED, ripple=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'after', 'before', 'className', 'debounceWait', 'disabled', 'href', 'key', 'loading_state', 'nClicks', 'ripple', 'style', 'target', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'after', 'before', 'className', 'debounceWait', 'disabled', 'href', 'key', 'loading_state', 'nClicks', 'ripple', 'style', 'target', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyFancyButton, self).__init__(children=children, **args)
