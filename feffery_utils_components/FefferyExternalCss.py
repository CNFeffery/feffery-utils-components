# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyExternalCss(Component):
    """A FefferyExternalCss component.
外部css资源动态注入组件FefferyExternalCss

Keyword arguments:

- id (string; optional):
    组件唯一id.

- cssUrl (string; default ''):
    设置对应绑定的css静态文件资源`url`  默认值：`''`.

- recentlyStatus (a value equal to: 'unset', 'loading', 'ready', 'error'; optional):
    监听最近一次资源变更操作后对应的状态.

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
    _type = 'FefferyExternalCss'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, cssUrl=Component.UNDEFINED, recentlyStatus=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'cssUrl', 'recentlyStatus', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'cssUrl', 'recentlyStatus', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyExternalCss, self).__init__(**args)
