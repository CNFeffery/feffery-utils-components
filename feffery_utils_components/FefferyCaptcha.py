# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCaptcha(Component):
    """A FefferyCaptcha component.
验证码组件FefferyCaptcha

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- captcha (string; optional):
    对应当前的验证码字符串.

- charNum (number; default 4):
    设置验证码字符数量.

- height (number; optional):
    设置验证码的像素高度  默认值：`40`.

- width (number; optional):
    设置验证码的像素宽度  默认值：`100`.

- bgColor (string; optional):
    设置验证码图片背景色  默认值：`'#DFF0D8'`.

- fontSize (number; optional):
    设置验证码字体像素大小  默认值：`25`.

- refresh (boolean; optional):
    用于手动刷新验证码，当传入`True`时会强制刷新验证码，再自动重置为`False`.

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
    _type = 'FefferyCaptcha'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, captcha=Component.UNDEFINED, charNum=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, bgColor=Component.UNDEFINED, fontSize=Component.UNDEFINED, refresh=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'captcha', 'charNum', 'height', 'width', 'bgColor', 'fontSize', 'refresh', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'captcha', 'charNum', 'height', 'width', 'bgColor', 'fontSize', 'refresh', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyCaptcha, self).__init__(**args)
