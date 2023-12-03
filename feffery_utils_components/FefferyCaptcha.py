# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCaptcha(Component):
    """A FefferyCaptcha component.


Keyword arguments:

- id (string; optional):
    部件id.

- bgColor (string; optional):
    设置验证码图片背景色，默认为'#DFF0D8'.

- captcha (string; optional):
    对应当前的验证码字符串.

- charNum (number; default 4):
    设置验证码字符数量.

- className (string; optional):
    css类名.

- fontSize (number; optional):
    设置验证码字体像素大小，默认为25.

- height (number; optional):
    设置验证码的像素高度，默认为40.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- refresh (boolean; optional):
    用于手动刷新验证码，当传入True时会强制刷新验证码，再自动重置为False.

- style (dict; optional):
    自定义css字典.

- width (number; optional):
    设置验证码的像素宽度，默认为100."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCaptcha'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, captcha=Component.UNDEFINED, charNum=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, bgColor=Component.UNDEFINED, fontSize=Component.UNDEFINED, refresh=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'bgColor', 'captcha', 'charNum', 'className', 'fontSize', 'height', 'loading_state', 'refresh', 'style', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'bgColor', 'captcha', 'charNum', 'className', 'fontSize', 'height', 'loading_state', 'refresh', 'style', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyCaptcha, self).__init__(**args)
