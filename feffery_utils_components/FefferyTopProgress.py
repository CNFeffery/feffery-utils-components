# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyTopProgress(Component):
    """A FefferyTopProgress component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the tab - will only be displayed if this tab is
    selected.

- id (string; optional):
    组件id.

- className (string; optional):
    css类名.

- color (string; default '#29d'):
    设置顶部进度条色彩，默认为'#29d'.

- debug (boolean; default False):
    设置是否开启debug模式，开启后，每次动画加载都会在开发者工具的控制台打印prop信息.

- easing (string; optional):
    用于设置同名css动画效果，默认为'ease'.

- excludeProps (list of strings; optional):
    设置需要忽略输出监听过程的组件信息列表,  仅在listenPropsMode为'exclude'时生效.

- includeProps (list of strings; optional):
    设置需要包含输出监听过程的组件信息列表,  仅在listenPropsMode为'include'时生效.

- key (string; optional):
    辅助刷新用唯一标识key值.

- listenPropsMode (a value equal to: 'default', 'exclude', 'include'; default 'default'):
    设置自定义监听组件的模式，可选的有'default'、'exclude'、'include'，默认为'default'.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- minimum (number; optional):
    设置顶端进度条的初始进度值，默认为0.33，取值在0到1之间.

- showSpinner (boolean; optional):
    设置是否渲染右上角圆圈加载动画，默认为True.

- speed (number; optional):
    设置进度条每步递增耗时（单位：毫秒），默认为200.

- spinning (boolean; default False):
    设置是否处于加载中状态.

- style (dict; optional):
    自定义css字典.

- zIndex (number; default 99999):
    设置顶部进度条的z-index，默认为99999."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTopProgress'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, spinning=Component.UNDEFINED, minimum=Component.UNDEFINED, easing=Component.UNDEFINED, speed=Component.UNDEFINED, showSpinner=Component.UNDEFINED, debug=Component.UNDEFINED, listenPropsMode=Component.UNDEFINED, excludeProps=Component.UNDEFINED, includeProps=Component.UNDEFINED, color=Component.UNDEFINED, zIndex=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'color', 'debug', 'easing', 'excludeProps', 'includeProps', 'key', 'listenPropsMode', 'loading_state', 'minimum', 'showSpinner', 'speed', 'spinning', 'style', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'color', 'debug', 'easing', 'excludeProps', 'includeProps', 'key', 'listenPropsMode', 'loading_state', 'minimum', 'showSpinner', 'speed', 'spinning', 'style', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyTopProgress, self).__init__(children=children, **args)
