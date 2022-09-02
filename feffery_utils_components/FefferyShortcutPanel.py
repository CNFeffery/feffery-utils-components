# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyShortcutPanel(Component):
    """A FefferyShortcutPanel component.


Keyword arguments:

- id (string; optional)

- data (list of dicts; optional)

    `data` is a list of dicts with keys:

    - children (list of strings; optional)

    - handler (string; optional)

    - hotkey (string; optional)

    - id (string; required)

    - keywords (string; optional)

    - parent (string; optional)

    - section (string; optional)

    - title (string; required)

- disableHotkeys (boolean; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'en', 'zh'; default 'zh')

- openHotkey (string; optional)

- placeholder (string; optional)

- style (dict; optional)

- theme (a value equal to: 'light', 'dark'; default 'light')

- triggeredHotkey (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyShortcutPanel'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, locale=Component.UNDEFINED, data=Component.UNDEFINED, triggeredHotkey=Component.UNDEFINED, placeholder=Component.UNDEFINED, disableHotkeys=Component.UNDEFINED, openHotkey=Component.UNDEFINED, theme=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'disableHotkeys', 'loading_state', 'locale', 'openHotkey', 'placeholder', 'style', 'theme', 'triggeredHotkey']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'disableHotkeys', 'loading_state', 'locale', 'openHotkey', 'placeholder', 'style', 'theme', 'triggeredHotkey']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyShortcutPanel, self).__init__(**args)
