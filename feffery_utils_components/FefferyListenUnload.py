# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyListenUnload(Component):
    """A FefferyListenUnload component.


Keyword arguments:

- id (string; optional):
    组件id.

- unloaded (boolean; optional):
    监听页面重载或关闭事件，每次页面关闭时会触发更新为True.

- confirmBeforeUnload (boolean; default False):
    是否在用户重载或关闭当前页面时，添加二次确认  默认值：`False`.

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
    _type = 'FefferyListenUnload'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, unloaded=Component.UNDEFINED, confirmBeforeUnload=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'unloaded', 'confirmBeforeUnload', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'unloaded', 'confirmBeforeUnload', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyListenUnload, self).__init__(**args)
