# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyVirtualList(Component):
    """A FefferyVirtualList component.


Keyword arguments:

- id (string; optional):
    组件id.

- children (a list of or a singular dash component, string or number; optional):
    组件子元素.

- style (dict; optional):
    设置css样式.

- className (string; optional):
    设置css类名.

- key (string; optional):
    辅助刷新用唯一标识key值.

- height (number; required):
    虚拟化区域像素高度.

- itemHeight (number; required):
    每个子元素区域的像素高度.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyVirtualList'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, height=Component.REQUIRED, itemHeight=Component.REQUIRED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'children', 'style', 'className', 'key', 'height', 'itemHeight', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'children', 'style', 'className', 'key', 'height', 'itemHeight', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['height', 'itemHeight']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyVirtualList, self).__init__(children=children, **args)
