# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferySliderCaptcha(Component):
    """A FefferySliderCaptcha component.


Keyword arguments:

- id (string; optional):
    组件id.

- className (string; optional):
    css类名.

- style (dict; optional):
    css样式.

- imgSrc (string; optional):
    用于生成拼图的完整图片地址.

- imgWidth (number; default 320):
    声明用于生成拼图的完整图片像素宽度值  默认值：`320`.

- imgHeight (number; default 160):
    声明用于生成拼图的完整图片像素高度值  默认值：`160`.

- xOffset (number; default 5):
    拼图合法验证像素偏移量  默认值：`5`.

- mode (a value equal to: 'embed', 'float', 'slider'; default 'embed'):
    显示模式，可选项有`'embed'`、`'float'`、`'slider'`  默认值：`'embed'`.

- tipText (dict; optional):
    配置相关文案提示内容.

    `tipText` is a dict with keys:

    - default (a list of or a singular dash component, string or number; optional):
        默认提示内容.

    - loading (a list of or a singular dash component, string or number; optional):
        加载中提示内容.

    - moving (a list of or a singular dash component, string or number; optional):
        移动中提示内容.

    - verifying (a list of or a singular dash component, string or number; optional):
        验证中提示内容.

    - success (a list of or a singular dash component, string or number; optional):
        验证成功提示内容.

    - error (a list of or a singular dash component, string or number; optional):
        验证失败提示内容.

- showRefreshIcon (boolean; default True):
    显示右上角刷新按钮  默认值：`True`.

- autoRefreshOnError (boolean; default True):
    验证失败后是否自动刷新  默认值：`True`.

- errorHoldDuration (number; default 500):
    当`autoRefreshOnError=True`时，每次验证失败后停顿多少毫秒自动刷新  默认值：`500`.

- placement (a value equal to: 'top', 'bottom'; default 'top'):
    拼图图片显示方位，可选项有`'top'`、`'bottom'`  默认值：`'top'`.

- refresh (boolean; optional):
    手动刷新用，每次更新为`True`时会主动触发刷新，每次成功刷新后会重置为`False`.

- verifyResult (dict; optional):
    监听最近一次验证结果.

    `verifyResult` is a dict with keys:

    - status (a value equal to: 'success', 'error'; optional):
        验证状态，`'success'`表示验证成功，`'error'`表示验证失败.

    - timestamp (number; optional):
        事件发生时间戳.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['tipText.default', 'tipText.loading', 'tipText.moving', 'tipText.verifying', 'tipText.success', 'tipText.error']
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferySliderCaptcha'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, imgSrc=Component.UNDEFINED, imgWidth=Component.UNDEFINED, imgHeight=Component.UNDEFINED, xOffset=Component.UNDEFINED, mode=Component.UNDEFINED, tipText=Component.UNDEFINED, showRefreshIcon=Component.UNDEFINED, autoRefreshOnError=Component.UNDEFINED, errorHoldDuration=Component.UNDEFINED, placement=Component.UNDEFINED, refresh=Component.UNDEFINED, verifyResult=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'imgSrc', 'imgWidth', 'imgHeight', 'xOffset', 'mode', 'tipText', 'showRefreshIcon', 'autoRefreshOnError', 'errorHoldDuration', 'placement', 'refresh', 'verifyResult', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'imgSrc', 'imgWidth', 'imgHeight', 'xOffset', 'mode', 'tipText', 'showRefreshIcon', 'autoRefreshOnError', 'errorHoldDuration', 'placement', 'refresh', 'verifyResult', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferySliderCaptcha, self).__init__(**args)
