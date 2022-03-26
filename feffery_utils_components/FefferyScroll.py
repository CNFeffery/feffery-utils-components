# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyScroll(Component):
    """A FefferyScroll component.


Keyword arguments:

- id (optional)

- containerId (optional)

- delay (optional)

- duration (optional)

- executeScroll (default False)

- loading_state (optional)

- offset (optional)

- scrollMode (default 'to-top')

- scrollRelativeOffset (optional)

- scrollTargetId (optional)

- scrollTopOffset (optional)

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes  to Dash, to make them available for callbacks.

- smooth (optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, scrollMode=Component.UNDEFINED, executeScroll=Component.UNDEFINED, scrollTopOffset=Component.UNDEFINED, scrollRelativeOffset=Component.UNDEFINED, scrollTargetId=Component.UNDEFINED, duration=Component.UNDEFINED, smooth=Component.UNDEFINED, delay=Component.UNDEFINED, containerId=Component.UNDEFINED, offset=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'containerId', 'delay', 'duration', 'executeScroll', 'loading_state', 'offset', 'scrollMode', 'scrollRelativeOffset', 'scrollTargetId', 'scrollTopOffset', 'setProps', 'smooth']
        self._type = 'FefferyScroll'
        self._namespace = 'feffery_utils_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'containerId', 'delay', 'duration', 'executeScroll', 'loading_state', 'offset', 'scrollMode', 'scrollRelativeOffset', 'scrollTargetId', 'scrollTopOffset', 'setProps', 'smooth']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyScroll, self).__init__(**args)
