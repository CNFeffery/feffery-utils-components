# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyMotion(Component):
    """A FefferyMotion component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- animate (dict | string; optional)

- className (string; optional)

- exit (dict | string; optional)

- initial (dict | boolean | string; optional)

- key (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- style (dict; optional)

- transition (dict; optional)

    `transition` is a dict with keys:

    - delay (number; optional)

    - duration (number; optional)

    - ease (a value equal to: 'linear', 'easeIn', 'easeOut', 'easeInOut', 'circIn', 'circOut', 'circInOut', 'backIn', 'backOut', 'backInOut', 'anticipate'; optional)

    - repeat (number | a value equal to: 'infinity'; optional)

    - repeatDelay (number; optional)

    - repeatType (a value equal to: 'loop', 'reverse', 'mirror'; optional)

    - times (list of numbers; optional)

    - type (a value equal to: 'spring', 'tween'; optional)

- variants (dict; optional)

- viewport (dict; optional)

    `viewport` is a dict with keys:

    - amount (a value equal to: 'some', 'all'; optional)

    - margin (string; optional)

    - once (boolean; optional)

- whileHover (dict | string; optional)

- whileInView (dict | string; optional)

- whileTap (dict | string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyMotion'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, initial=Component.UNDEFINED, animate=Component.UNDEFINED, exit=Component.UNDEFINED, whileHover=Component.UNDEFINED, whileTap=Component.UNDEFINED, transition=Component.UNDEFINED, whileInView=Component.UNDEFINED, viewport=Component.UNDEFINED, variants=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'animate', 'className', 'exit', 'initial', 'key', 'loading_state', 'style', 'transition', 'variants', 'viewport', 'whileHover', 'whileInView', 'whileTap']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'animate', 'className', 'exit', 'initial', 'key', 'loading_state', 'style', 'transition', 'variants', 'viewport', 'whileHover', 'whileInView', 'whileTap']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyMotion, self).__init__(children=children, **args)
