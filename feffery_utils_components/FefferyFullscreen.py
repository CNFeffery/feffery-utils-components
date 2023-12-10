# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyFullscreen(Component):
    """A FefferyFullscreen component.


Keyword arguments:

- id (string; optional):
    组件id.

- isFullscreen (boolean; default False):
    设置或监听目标元素的全屏化状态，默认为False.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- targetId (string; optional):
    设置要全屏化的目标元素id，缺省时会以整个页面作为全屏化目标."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFullscreen'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, targetId=Component.UNDEFINED, isFullscreen=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'isFullscreen', 'loading_state', 'targetId']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'isFullscreen', 'loading_state', 'targetId']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyFullscreen, self).__init__(**args)
