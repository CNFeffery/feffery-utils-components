# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferySticky(Component):
    """A FefferySticky component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    组件子元素.

- id (string; optional):
    组件id.

- bottomBoundary (number | string; optional):
    设置粘性布局元素底部距离文档顶部的像素距离阈值，  当超出这个阈值范围时，粘性状态会被解除；
    当传入字符型时，字符应为css选择器规则，则此时当目标元素底部  到达粘性布局元素底部时，粘性状态会被解除.

- enabled (boolean; default True):
    设置是否启用粘性布局效果，默认为True.

- key (string; optional):
    辅助刷新用唯一标识key值.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- top (number | string; default 0):
    用于设置触发粘性布局效果对应的顶部距离阈值，  当传入字符型时，字符应为css选择器规则，则此时的顶部距离阈值  默认为0，
    为选择器对应目标元素的高度.

- zIndex (number; optional):
    设置粘性布局元素的z-index属性."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferySticky'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, enabled=Component.UNDEFINED, top=Component.UNDEFINED, bottomBoundary=Component.UNDEFINED, zIndex=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bottomBoundary', 'enabled', 'key', 'loading_state', 'top', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bottomBoundary', 'enabled', 'key', 'loading_state', 'top', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferySticky, self).__init__(children=children, **args)
