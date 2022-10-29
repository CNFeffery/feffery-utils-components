# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyLazyLoadImage(Component):
    """A FefferyLazyLoadImage component.


Keyword arguments:

- id (string; optional)

- alt (string; optional)

- height (string | number; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- placeholderSrc (string; optional)

- src (string; optional)

- threshold (number; default 100)

- width (string | number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyLazyLoadImage'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, alt=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, src=Component.UNDEFINED, placeholderSrc=Component.UNDEFINED, threshold=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'alt', 'height', 'loading_state', 'placeholderSrc', 'src', 'threshold', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'alt', 'height', 'loading_state', 'placeholderSrc', 'src', 'threshold', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyLazyLoadImage, self).__init__(**args)
