# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyShortcutPanel(Component):
    """A FefferyShortcutPanel component.


Keyword arguments:

- id (optional)

- data (optional)

- disableHotkeys (optional)

- loading_state (optional)

- locale (default 'zh')

- openHotkey (optional)

- placeholder (optional)

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes  to Dash, to make them available for callbacks.

- style (optional)

- theme (default 'light')

- triggeredHotkey (optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, locale=Component.UNDEFINED, data=Component.UNDEFINED, triggeredHotkey=Component.UNDEFINED, placeholder=Component.UNDEFINED, disableHotkeys=Component.UNDEFINED, openHotkey=Component.UNDEFINED, theme=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'disableHotkeys', 'loading_state', 'locale', 'openHotkey', 'placeholder', 'setProps', 'style', 'theme', 'triggeredHotkey']
        self._type = 'FefferyShortcutPanel'
        self._namespace = 'feffery_utils_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'disableHotkeys', 'loading_state', 'locale', 'openHotkey', 'placeholder', 'setProps', 'style', 'theme', 'triggeredHotkey']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyShortcutPanel, self).__init__(**args)
