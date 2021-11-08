# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferySyntaxHighlighter(Component):
    """A FefferySyntaxHighlighter component.


Keyword arguments:

- id (string; optional)

- codeString (string; required)

- codeStyle (string; default 'prism')

- language (string; required)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- showInlineLineNumbers (boolean; optional)

- showLineNumbers (boolean; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, codeStyle=Component.UNDEFINED, codeString=Component.REQUIRED, language=Component.REQUIRED, showLineNumbers=Component.UNDEFINED, showInlineLineNumbers=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'codeString', 'codeStyle', 'language', 'loading_state', 'showInlineLineNumbers', 'showLineNumbers']
        self._type = 'FefferySyntaxHighlighter'
        self._namespace = 'feffery_utils_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'codeString', 'codeStyle', 'language', 'loading_state', 'showInlineLineNumbers', 'showLineNumbers']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['codeString', 'language']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferySyntaxHighlighter, self).__init__(**args)
