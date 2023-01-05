# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyJsonViewer(Component):
    """A FefferyJsonViewer component.


Keyword arguments:

- id (string; optional)

- addible (boolean; default False)

- className (string | dict; optional)

- collapseStringsAfterLength (boolean | number; default False)

- collapsed (boolean | number; default False)

- data (dict; required)

- deletable (boolean; default False)

- displayArrayKey (boolean; default True)

- displayDataTypes (boolean; default True)

- displayObjectSize (boolean; default True)

- editable (boolean; default False)

- enableClipboard (boolean; default True)

- groupArraysAfterLength (number; default 100)

- iconStyle (a value equal to: 'circle', 'triangle', 'square'; default 'circle')

- indent (number; default 4)

- key (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- quotesOnKeys (boolean; default True)

- sortKeys (boolean; default False)

- style (dict; optional)

- theme (a value equal to: 'apathy', 'apathy:inverted', 'ashes', 'bespin', 'brewer', 'bright:inverted', 'bright', 'chalk', 'codeschool', 'colors', 'eighties', 'embers', 'flat', 'google', 'grayscale', 'grayscale:inverted', 'greenscreen', 'harmonic', 'hopscotch', 'isotope', 'marrakesh', 'mocha', 'monokai', 'ocean', 'paraiso', 'pop', 'railscasts', 'rjv-default', 'shapeshifter', 'shapeshifter:inverted', 'solarized', 'summerfruit', 'summerfruit:inverted', 'threezerotwofour', 'tomorrow', 'tube', 'twilight'; default 'summerfruit:inverted')"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyJsonViewer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, data=Component.REQUIRED, theme=Component.UNDEFINED, indent=Component.UNDEFINED, iconStyle=Component.UNDEFINED, collapsed=Component.UNDEFINED, collapseStringsAfterLength=Component.UNDEFINED, groupArraysAfterLength=Component.UNDEFINED, enableClipboard=Component.UNDEFINED, displayObjectSize=Component.UNDEFINED, displayDataTypes=Component.UNDEFINED, editable=Component.UNDEFINED, addible=Component.UNDEFINED, deletable=Component.UNDEFINED, sortKeys=Component.UNDEFINED, quotesOnKeys=Component.UNDEFINED, displayArrayKey=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'addible', 'className', 'collapseStringsAfterLength', 'collapsed', 'data', 'deletable', 'displayArrayKey', 'displayDataTypes', 'displayObjectSize', 'editable', 'enableClipboard', 'groupArraysAfterLength', 'iconStyle', 'indent', 'key', 'loading_state', 'quotesOnKeys', 'sortKeys', 'style', 'theme']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'addible', 'className', 'collapseStringsAfterLength', 'collapsed', 'data', 'deletable', 'displayArrayKey', 'displayDataTypes', 'displayObjectSize', 'editable', 'enableClipboard', 'groupArraysAfterLength', 'iconStyle', 'indent', 'key', 'loading_state', 'quotesOnKeys', 'sortKeys', 'style', 'theme']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyJsonViewer, self).__init__(**args)
