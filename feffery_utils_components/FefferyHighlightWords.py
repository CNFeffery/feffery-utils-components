# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyHighlightWords(Component):
    """A FefferyHighlightWords component.


Keyword arguments:

- id (string; optional)

- caseSensitive (boolean; default False)

- className (string; optional)

- highlightClassName (string; default 'feffery-highlight-words-highlight')

- highlightStyle (dict; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- searchWords (list of strings; optional)

- style (dict; optional)

- textToHighlight (string; optional)

- unhighlightClassName (string; optional)

- unhighlightStyle (dict; optional)

- useRegex (boolean; default False)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyHighlightWords'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, caseSensitive=Component.UNDEFINED, highlightClassName=Component.UNDEFINED, highlightStyle=Component.UNDEFINED, useRegex=Component.UNDEFINED, searchWords=Component.UNDEFINED, textToHighlight=Component.UNDEFINED, unhighlightClassName=Component.UNDEFINED, unhighlightStyle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'caseSensitive', 'className', 'highlightClassName', 'highlightStyle', 'loading_state', 'searchWords', 'style', 'textToHighlight', 'unhighlightClassName', 'unhighlightStyle', 'useRegex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'caseSensitive', 'className', 'highlightClassName', 'highlightStyle', 'loading_state', 'searchWords', 'style', 'textToHighlight', 'unhighlightClassName', 'unhighlightStyle', 'useRegex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyHighlightWords, self).__init__(**args)
