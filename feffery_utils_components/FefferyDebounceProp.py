# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDebounceProp(Component):
    """A FefferyDebounceProp component.


Keyword arguments:

- id (string; optional):
    组件id.

- sourceProp (boolean | number | string | dict | list; optional):
    用于同步目标属性，请通过回调函数更新.

- debounceProp (boolean | number | string | dict | list; optional):
    对应sourceProp的防抖控制状态.

- debounceWait (number; default 200):
    设置防抖延时时长，单位：毫秒  默认：200.

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
    _type = 'FefferyDebounceProp'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, sourceProp=Component.UNDEFINED, debounceProp=Component.UNDEFINED, debounceWait=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'sourceProp', 'debounceProp', 'debounceWait', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'sourceProp', 'debounceProp', 'debounceWait', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDebounceProp, self).__init__(**args)
