# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyFancyButton(Component):
    """A FefferyFancyButton component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    设置按钮内嵌元素内容.

- id (string; optional):
    部件id.

- after (a list of or a singular dash component, string or number; optional):
    设置按钮后缀图标元素.

- before (a list of or a singular dash component, string or number; optional):
    设置按钮前缀图标元素.

- className (string | dict; optional):
    css类名.

- debounceWait (number; default 0):
    用于配置value变化更新的防抖等待时长（单位：毫秒），默认为0.

- disabled (boolean; optional):
    设置是否禁用当前按钮，默认为False.

- href (string; optional):
    当按钮充当链接功能时，用于设置链接地址.

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

- nClicks (number; default 0):
    记录按钮从渲染后开始被点击的次数，默认为0.

- ripple (boolean; optional):
    设置是否开启点击涟漪效果，默认为False.

- style (dict; optional):
    自定义css字典.

- target (string; default '_blank'):
    设置按钮的target属性，默认为'_blank'.

- type (a value equal to: 'primary', 'secondary', 'danger'; optional):
    设置按钮类型，可选的有'primary'、'secondary'、'danger'  默认为'primary'."""
    _children_props = ['before', 'after']
    _base_nodes = ['before', 'after', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFancyButton'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, nClicks=Component.UNDEFINED, debounceWait=Component.UNDEFINED, type=Component.UNDEFINED, disabled=Component.UNDEFINED, href=Component.UNDEFINED, target=Component.UNDEFINED, before=Component.UNDEFINED, after=Component.UNDEFINED, ripple=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'after', 'before', 'className', 'debounceWait', 'disabled', 'href', 'key', 'loading_state', 'nClicks', 'ripple', 'style', 'target', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'after', 'before', 'className', 'debounceWait', 'disabled', 'href', 'key', 'loading_state', 'nClicks', 'ripple', 'style', 'target', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyFancyButton, self).__init__(children=children, **args)
