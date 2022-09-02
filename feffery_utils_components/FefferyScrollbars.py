# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyScrollbars(Component):
    """A FefferyScrollbars component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- autoHide (boolean; default True)

- className (string; optional)

- classNames (dict; optional)

    `classNames` is a dict with keys:

    - content (string; optional)

    - scrollContent (string; optional)

    - scrollbar (string; optional)

    - track (string; optional)

- forceVisible (boolean | a value equal to: 'x', 'y'; default False)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- scrollbarMaxSize (number; optional)

- scrollbarMinSize (number; default 25)

- style (dict; optional)

- timeout (number; default 1000)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyScrollbars'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, autoHide=Component.UNDEFINED, classNames=Component.UNDEFINED, forceVisible=Component.UNDEFINED, timeout=Component.UNDEFINED, scrollbarMinSize=Component.UNDEFINED, scrollbarMaxSize=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'autoHide', 'className', 'classNames', 'forceVisible', 'loading_state', 'scrollbarMaxSize', 'scrollbarMinSize', 'style', 'timeout']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'autoHide', 'className', 'classNames', 'forceVisible', 'loading_state', 'scrollbarMaxSize', 'scrollbarMinSize', 'style', 'timeout']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyScrollbars, self).__init__(children=children, **args)
