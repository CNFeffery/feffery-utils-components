# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyGuide(Component):
    """A FefferyGuide component.


Keyword arguments:

- id (optional)

- arrow (optional)

- className (optional)

- closable (optional)

- hotspot (optional)

- loading_state (optional)

- localKey (optional)

- locale (default 'zh')

- mask (optional)

- maskClassName (optional)

- modalClassName (optional)

- nextText (optional)

- okText (optional)

- prevText (optional)

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes  to Dash, to make them available for callbacks.

- showPreviousBtn (default True)

- step (optional)

- stepText (optional)

- steps (optional)

- style (optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, locale=Component.UNDEFINED, steps=Component.UNDEFINED, localKey=Component.UNDEFINED, closable=Component.UNDEFINED, modalClassName=Component.UNDEFINED, maskClassName=Component.UNDEFINED, mask=Component.UNDEFINED, arrow=Component.UNDEFINED, hotspot=Component.UNDEFINED, stepText=Component.UNDEFINED, nextText=Component.UNDEFINED, prevText=Component.UNDEFINED, showPreviousBtn=Component.UNDEFINED, okText=Component.UNDEFINED, step=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'arrow', 'className', 'closable', 'hotspot', 'loading_state', 'localKey', 'locale', 'mask', 'maskClassName', 'modalClassName', 'nextText', 'okText', 'prevText', 'setProps', 'showPreviousBtn', 'step', 'stepText', 'steps', 'style']
        self._type = 'FefferyGuide'
        self._namespace = 'feffery_utils_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'arrow', 'className', 'closable', 'hotspot', 'loading_state', 'localKey', 'locale', 'mask', 'maskClassName', 'modalClassName', 'nextText', 'okText', 'prevText', 'setProps', 'showPreviousBtn', 'step', 'stepText', 'steps', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyGuide, self).__init__(**args)
