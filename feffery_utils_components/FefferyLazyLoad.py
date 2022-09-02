# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyLazyLoad(Component):
    """A FefferyLazyLoad component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- height (number | string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- offset (number; optional)

- style (dict; optional)

- throttle (number; optional)

- visible (boolean; default False)

- width (number | string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyLazyLoad'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, offset=Component.UNDEFINED, visible=Component.UNDEFINED, throttle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'height', 'loading_state', 'offset', 'style', 'throttle', 'visible', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'height', 'loading_state', 'offset', 'style', 'throttle', 'visible', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyLazyLoad, self).__init__(children=children, **args)
