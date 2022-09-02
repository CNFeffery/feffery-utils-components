# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyGuide(Component):
    """A FefferyGuide component.


Keyword arguments:

- id (string; optional)

- arrow (boolean; optional)

- className (string; optional)

- closable (boolean; optional)

- hotspot (boolean; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- localKey (string; required)

- locale (a value equal to: 'zh', 'en'; default 'zh')

- mask (boolean; optional)

- maskClassName (string; optional)

- modalClassName (string; optional)

- nextText (string; optional)

- okText (string; optional)

- prevText (string; optional)

- showPreviousBtn (boolean; default True)

- step (number; optional)

- stepText (string; optional)

- steps (list of dicts; required)

    `steps` is a list of dicts with keys:

    - content (string; optional)

    - offset (dict; optional)

        `offset` is a dict with keys:

        - x (number; optional)

        - y (number; optional)

    - placement (a value equal to: 'top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right', 'left-top', 'left-bottom', 'right-top', 'right-bottom'; optional)

    - selector (string; optional)

    - targetPos (dict; optional)

        `targetPos` is a dict with keys:

        - height (number; optional)

        - left (number; optional)

        - top (number; optional)

        - width (number; optional)

    - title (string; optional)

- style (dict; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyGuide'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, locale=Component.UNDEFINED, steps=Component.REQUIRED, localKey=Component.REQUIRED, closable=Component.UNDEFINED, modalClassName=Component.UNDEFINED, maskClassName=Component.UNDEFINED, mask=Component.UNDEFINED, arrow=Component.UNDEFINED, hotspot=Component.UNDEFINED, stepText=Component.UNDEFINED, nextText=Component.UNDEFINED, prevText=Component.UNDEFINED, showPreviousBtn=Component.UNDEFINED, okText=Component.UNDEFINED, step=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'arrow', 'className', 'closable', 'hotspot', 'loading_state', 'localKey', 'locale', 'mask', 'maskClassName', 'modalClassName', 'nextText', 'okText', 'prevText', 'showPreviousBtn', 'step', 'stepText', 'steps', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'arrow', 'className', 'closable', 'hotspot', 'loading_state', 'localKey', 'locale', 'mask', 'maskClassName', 'modalClassName', 'nextText', 'okText', 'prevText', 'showPreviousBtn', 'step', 'stepText', 'steps', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['localKey', 'steps']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FefferyGuide, self).__init__(**args)
