# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyScroll(Component):
    """A FefferyScroll component.


Keyword arguments:

- id (string; optional)

- containerId (string; optional)

- delay (number; optional)

- duration (number; optional)

- executeScroll (boolean; default False)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- offset (number; optional)

- scrollMode (a value equal to: 'to-top', 'to-bottom', 'top-offset', 'relative-offset', 'target'; default 'to-top')

- scrollRelativeOffset (number; optional)

- scrollTargetId (string; optional)

- scrollTopOffset (number; optional)

- smooth (a value equal to: 'linear', 'easeInQuad', 'easeOutQuad', 'easeInOutQuad', 'easeInCubic', 'easeOutCubic', 'easeInOutCubic', 'easeInQuart', 'easeOutQuart', 'easeInOutQuart', 'easeInQuint', 'easeOutQuint', 'easeInOutQuint'; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyScroll'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, scrollMode=Component.UNDEFINED, executeScroll=Component.UNDEFINED, scrollTopOffset=Component.UNDEFINED, scrollRelativeOffset=Component.UNDEFINED, scrollTargetId=Component.UNDEFINED, duration=Component.UNDEFINED, smooth=Component.UNDEFINED, delay=Component.UNDEFINED, containerId=Component.UNDEFINED, offset=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'containerId', 'delay', 'duration', 'executeScroll', 'loading_state', 'offset', 'scrollMode', 'scrollRelativeOffset', 'scrollTargetId', 'scrollTopOffset', 'smooth']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'containerId', 'delay', 'duration', 'executeScroll', 'loading_state', 'offset', 'scrollMode', 'scrollRelativeOffset', 'scrollTargetId', 'scrollTopOffset', 'smooth']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyScroll, self).__init__(**args)
