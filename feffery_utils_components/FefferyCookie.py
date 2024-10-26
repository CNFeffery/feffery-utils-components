# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCookie(Component):
    """A FefferyCookie component.
Cookie控制组件FefferyCookie

Keyword arguments:

- id (string; optional):
    组件唯一id.

- cookieKey (string; required):
    必填，设置要绑定的`cookie`键名.

- defaultValue (string; optional):
    为当前所绑定的`cookie`设定缺省时的默认值，当所绑定的`cookie`本身有值时，该值将不会影响原本的`cookie`值.

- value (string; optional):
    用于更新当前绑定的`cookie`值.

- expires (number; optional):
    设置当前`cookie`值的有效存储时间，单位：秒.

- pathname (string; default '/'):
    设置当前`cookie`值可用的`pathname`  默认值：`'/'`.

- secure (boolean; default False):
    设置当前`cookie`是否仅允许通过`https`安全传输  默认值：`False`.

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
    _type = 'FefferyCookie'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, cookieKey=Component.REQUIRED, defaultValue=Component.UNDEFINED, value=Component.UNDEFINED, expires=Component.UNDEFINED, pathname=Component.UNDEFINED, secure=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'cookieKey', 'defaultValue', 'value', 'expires', 'pathname', 'secure', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'cookieKey', 'defaultValue', 'value', 'expires', 'pathname', 'secure', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['cookieKey']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyCookie, self).__init__(**args)
