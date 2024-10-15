# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyFancyButton(Component):
    """A FefferyFancyButton component.
美观按钮组件FefferyFancyButton

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- style (dict; optional):
    当前组件css样式.

- className (string | dict; optional):
    当前组件css类名.

- nClicks (number; default 0):
    按钮累计点击次数，用于监听按钮点击行为  默认值：`0`.

- debounceWait (number; default 0):
    按钮点击事件监听防抖延时，单位：毫秒  默认值：`0`.

- type (a value equal to: 'primary', 'secondary', 'danger'; optional):
    按钮类型，可选项有`'primary'`、`'secondary'`、`'danger'`  默认值：`'primary'`.

- disabled (boolean; optional):
    是否禁用当前组件  默认值：`False`.

- href (string; optional):
    按钮点击跳转链接地址.

- target (string; default '_blank'):
    按钮点击跳转链接方式  默认值：`'_blank'`.

- before (a list of or a singular dash component, string or number; optional):
    组件型，按钮前缀元素.

- after (a list of or a singular dash component, string or number; optional):
    组件型，按钮后缀元素.

- ripple (boolean; optional):
    是否开启点击涟漪效果  默认值：`False`.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['before', 'after']
    _base_nodes = ['before', 'after', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFancyButton'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, nClicks=Component.UNDEFINED, debounceWait=Component.UNDEFINED, type=Component.UNDEFINED, disabled=Component.UNDEFINED, href=Component.UNDEFINED, target=Component.UNDEFINED, before=Component.UNDEFINED, after=Component.UNDEFINED, ripple=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'nClicks', 'debounceWait', 'type', 'disabled', 'href', 'target', 'before', 'after', 'ripple', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'nClicks', 'debounceWait', 'type', 'disabled', 'href', 'target', 'before', 'after', 'ripple', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyFancyButton, self).__init__(children=children, **args)
