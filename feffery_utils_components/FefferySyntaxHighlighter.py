# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferySyntaxHighlighter(Component):
    """A FefferySyntaxHighlighter component.


Keyword arguments:

- id (string; optional)

- codeBlockStyle (dict; optional)

- codeString (string; required)

- codeStyle (dict; optional)

- codeTheme (a value equal to: 'a11y-dark', 'atom-dark', 'coldark-cold', 'coldark-dark', 'coy', 'coy-without-shadows', 'darcula', 'dracula', 'nord', 'okaidia', 'prism', 'solarizedlight', 'twilight', 'duotone-sea', 'duotone-dark', 'duotone-light', 'duotone-space', 'gh-colors', 'gruvbox-dark', 'material-dark', 'night-owl', 'one-light', 'pojoaque', 'solarized-dark-atom', 'synthwave84', 'z-touch'; default 'gh-colors')

- language (string; required)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- showLineNumbers (boolean; default True)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferySyntaxHighlighter'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, codeString=Component.REQUIRED, language=Component.REQUIRED, codeTheme=Component.UNDEFINED, codeBlockStyle=Component.UNDEFINED, codeStyle=Component.UNDEFINED, showLineNumbers=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'codeBlockStyle', 'codeString', 'codeStyle', 'codeTheme', 'language', 'loading_state', 'showLineNumbers']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'codeBlockStyle', 'codeString', 'codeStyle', 'codeTheme', 'language', 'loading_state', 'showLineNumbers']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['codeString', 'language']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferySyntaxHighlighter, self).__init__(**args)
