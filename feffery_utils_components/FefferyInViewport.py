# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyInViewport(Component):
    """A FefferyInViewport component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    需要进行可见性监听的目标元素.

- id (string; optional):
    组件id.

- inViewport (boolean; optional):
    监听当前元素是否出现在可视范围内.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- threshold (number; optional):
    用于设置触发元素可见性状态切换的比例阈值."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyInViewport'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, inViewport=Component.UNDEFINED, threshold=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'inViewport', 'loading_state', 'threshold']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'inViewport', 'loading_state', 'threshold']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyInViewport, self).__init__(children=children, **args)
