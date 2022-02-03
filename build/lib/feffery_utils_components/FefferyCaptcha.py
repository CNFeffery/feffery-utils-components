# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCaptcha(Component):
    """A FefferyCaptcha component.


Keyword arguments:

- id (optional)

- bgColor (optional)

- captcha (optional)

- charNum (default 4)

- className (optional)

- fontSize (optional)

- height (optional)

- loading_state (optional)

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes  to Dash, to make them available for callbacks.

- style (optional)

- width (optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, captcha=Component.UNDEFINED, charNum=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, bgColor=Component.UNDEFINED, fontSize=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'bgColor', 'captcha', 'charNum', 'className', 'fontSize', 'height', 'loading_state', 'setProps', 'style', 'width']
        self._type = 'FefferyCaptcha'
        self._namespace = 'feffery_utils_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'bgColor', 'captcha', 'charNum', 'className', 'fontSize', 'height', 'loading_state', 'setProps', 'style', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyCaptcha, self).__init__(**args)
