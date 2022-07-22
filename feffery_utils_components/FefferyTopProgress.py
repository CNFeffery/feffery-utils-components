# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyTopProgress(Component):
    """A FefferyTopProgress component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the tab - will only be displayed if this tab is
    selected.

- id (string; optional)

- className (string; optional)

- debug (boolean; default False)

- easing (string; optional)

- excludeProps (list of strings; optional)

- includeProps (list of strings; optional)

- listenPropsMode (a value equal to: 'default', 'exclude', 'include'; default 'default')

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- minimum (number; optional)

- showSpinner (boolean; optional)

- speed (number; optional)

- spinning (boolean; default False)

- style (dict; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTopProgress'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, spinning=Component.UNDEFINED, minimum=Component.UNDEFINED, easing=Component.UNDEFINED, speed=Component.UNDEFINED, showSpinner=Component.UNDEFINED, debug=Component.UNDEFINED, listenPropsMode=Component.UNDEFINED, excludeProps=Component.UNDEFINED, includeProps=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'debug', 'easing', 'excludeProps', 'includeProps', 'listenPropsMode', 'loading_state', 'minimum', 'showSpinner', 'speed', 'spinning', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'debug', 'easing', 'excludeProps', 'includeProps', 'listenPropsMode', 'loading_state', 'minimum', 'showSpinner', 'speed', 'spinning', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyTopProgress, self).__init__(children=children, **args)
