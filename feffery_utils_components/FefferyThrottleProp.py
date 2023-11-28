# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyThrottleProp(Component):
    """A FefferyThrottleProp component.


Keyword arguments:

- id (string; optional):
    组件唯一id，用于编排回调角色等.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- sourceProp (boolean | number | string | dict | list; optional):
    用于同步目标属性，请通过回调函数更新.

- throttleProp (boolean | number | string | dict | list; optional):
    对应sourceProp的节流控制状态.

- throttleWait (number; default 200):
    设置节流延时时长，单位：毫秒  默认：200."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyThrottleProp'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, sourceProp=Component.UNDEFINED, throttleProp=Component.UNDEFINED, throttleWait=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'loading_state', 'sourceProp', 'throttleProp', 'throttleWait']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'loading_state', 'sourceProp', 'throttleProp', 'throttleWait']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyThrottleProp, self).__init__(**args)
