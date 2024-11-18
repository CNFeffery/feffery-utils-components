# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyThrottleProp(Component):
    """A FefferyThrottleProp component.
节流属性组件FefferyThrottleProp

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- sourceProp (boolean | number | string | dict | list; optional):
    用于同步目标属性，请通过回调函数更新.

- throttleProp (boolean | number | string | dict | list; optional):
    对应`sourceProp`的节流控制状态.

- throttleWait (number; default 200):
    设置节流延时时长，单位：毫秒  默认值：`200`.

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
    _type = 'FefferyThrottleProp'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, sourceProp=Component.UNDEFINED, throttleProp=Component.UNDEFINED, throttleWait=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'sourceProp', 'throttleProp', 'throttleWait', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'sourceProp', 'throttleProp', 'throttleWait', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyThrottleProp, self).__init__(**args)
