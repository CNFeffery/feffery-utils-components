# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyScrollbars(Component):
    """A FefferyScrollbars component.


Keyword arguments:

- children (optional)

- id (optional)

- autoHide (default False)

- autoHideDuration (default 200)

- autoHideTimeout (default 1000)

- className (optional)

- loading_state (optional)

- style (optional)

- thumbSize (default 30)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, thumbSize=Component.UNDEFINED, autoHide=Component.UNDEFINED, autoHideTimeout=Component.UNDEFINED, autoHideDuration=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'autoHide', 'autoHideDuration', 'autoHideTimeout', 'className', 'loading_state', 'style', 'thumbSize']
        self._type = 'FefferyScrollbars'
        self._namespace = 'feffery_utils_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'autoHide', 'autoHideDuration', 'autoHideTimeout', 'className', 'loading_state', 'style', 'thumbSize']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyScrollbars, self).__init__(children=children, **args)
