# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyShortcutPanel(Component):
    """A FefferyShortcutPanel component.


Keyword arguments:

- id (string; optional)

- close (boolean; default False)

- data (list of dicts; required)

    `data` is a list of dicts with keys:

    - children (list of strings; optional)

    - handler (string; optional)

    - hotkey (string; optional)

    - id (string; required)

    - keywords (string; optional)

    - parent (string; optional)

    - section (string; optional)

    - title (string; required)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'en', 'zh'; default 'zh')

- open (boolean; default False)

- openHotkey (string; default 'cmd+k,ctrl+k')

- panelStyles (dict; optional)

    `panelStyles` is a dict with keys:

    - accentColor (string; optional)

    - actionsHeight (string; optional)

    - fontSize (string; optional)

    - groupTextColor (string; optional)

    - overflowBackground (string; optional)

    - secondaryBackgroundColor (string; optional)

    - secondaryTextColor (string; optional)

    - selectedBackground (string; optional)

    - textColor (string; optional)

    - top (string; optional)

    - width (string; optional)

    - zIndex (number; optional)

- placeholder (string; optional)

- searchValue (string; optional)

- theme (a value equal to: 'light', 'dark'; default 'light')

- triggeredHotkey (dict; optional)

    `triggeredHotkey` is a dict with keys:

    - id (string; optional)

    - timestamp (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyShortcutPanel'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, locale=Component.UNDEFINED, data=Component.REQUIRED, triggeredHotkey=Component.UNDEFINED, placeholder=Component.UNDEFINED, openHotkey=Component.UNDEFINED, theme=Component.UNDEFINED, open=Component.UNDEFINED, close=Component.UNDEFINED, panelStyles=Component.UNDEFINED, searchValue=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'close', 'data', 'loading_state', 'locale', 'open', 'openHotkey', 'panelStyles', 'placeholder', 'searchValue', 'theme', 'triggeredHotkey']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'close', 'data', 'loading_state', 'locale', 'open', 'openHotkey', 'panelStyles', 'placeholder', 'searchValue', 'theme', 'triggeredHotkey']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyShortcutPanel, self).__init__(**args)
