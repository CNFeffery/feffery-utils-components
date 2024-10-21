# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyGuide(Component):
    """A FefferyGuide component.
引导部件FefferyGuide

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- locale (a value equal to: 'zh', 'en'; default 'zh'):
    设置语言，可选项有`'zh'`、`'en'`  默认值：`'zh'`.

- steps (list of dicts; required):
    必填，用于构造每一步锚定的页面元素.

    `steps` is a list of dicts with keys:

    - selector (string; optional):
        对应当前步骤锚定的元素对应的`css`选择器.

    - targetPos (dict; optional):
        当`selector`参数缺省时，可用`targetPos`参数基于绝对位置进行步骤锚定.

        `targetPos` is a dict with keys:

        - top (number; optional):
            设置距离顶部的像素距离.

        - left (number; optional):
            设置距离左端的像素距离.

        - width (number; optional):
            设置锚定范围像素宽度.

        - height (number; optional):
            设置锚定范围像素高度.

    - title (a list of or a singular dash component, string or number; optional):
        设置展示面板的标题内容.

    - content (a list of or a singular dash component, string or number; optional):
        设置展示面板的描述内容.

    - placement (a value equal to: 'top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right', 'left-top', 'left-bottom', 'right-top', 'right-bottom'; optional):
        设置展示面板相对锚点的方位，可选项有`'top'`、`'bottom'`、`'left'`、`'right'`、`'top-left'`、`'top-right'`、`'bottom-left'`、`'bottom-right'`、`'left-top'`、`'left-bottom'`、`'right-top'`、`'right-bottom'`
        默认值：`'bottom'`.

    - offset (dict; optional):
        设置展示面板的像素偏移量.

        `offset` is a dict with keys:

        - x (number; optional):
            水平方向偏移像素距离.

        - y (number; optional):
            竖直方向偏移像素距离.

- localKey (string; required):
    用于设置本地缓存唯一标识`key`，从而辅助应用判断是否已展示过该引导页.

- closable (boolean; optional):
    设置是否允许跳过引导  默认值：`True`.

- modalClassName (string; optional):
    弹窗css类名.

- maskClassName (string; optional):
    蒙版层css类名.

- mask (boolean; default True):
    是否展示蒙版层  默认值：`True`.

- arrow (boolean; optional):
    展示面板是否添加箭头  默认值：`True`.

- hotspot (boolean; optional):
    展示面板是否展示热点标识  默认值：`False`.

- stepText (string; optional):
    自定义步骤信息展示内容的回调函数  默认值：`\"(stepIndex, stepCount) => { return
    '第${stepIndex}步，共${stepCount}步'; }\"`.

- nextText (string; optional):
    “下一步”按钮文案信息.

- prevText (string; optional):
    “上一步”按钮文案信息.

- showPreviousBtn (boolean; default True):
    是否显示“上一步”按钮  默认值：`True`.

- okText (string; optional):
    确认按钮的文案信息.

- step (number; optional):
    设置初始化时的起始步骤，为`-1`时则不显示引导组件  默认值：`0`.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['steps[].title', 'steps[].content']
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyGuide'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, locale=Component.UNDEFINED, steps=Component.REQUIRED, localKey=Component.REQUIRED, closable=Component.UNDEFINED, modalClassName=Component.UNDEFINED, maskClassName=Component.UNDEFINED, mask=Component.UNDEFINED, arrow=Component.UNDEFINED, hotspot=Component.UNDEFINED, stepText=Component.UNDEFINED, nextText=Component.UNDEFINED, prevText=Component.UNDEFINED, showPreviousBtn=Component.UNDEFINED, okText=Component.UNDEFINED, step=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'locale', 'steps', 'localKey', 'closable', 'modalClassName', 'maskClassName', 'mask', 'arrow', 'hotspot', 'stepText', 'nextText', 'prevText', 'showPreviousBtn', 'okText', 'step', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'locale', 'steps', 'localKey', 'closable', 'modalClassName', 'maskClassName', 'mask', 'arrow', 'hotspot', 'stepText', 'nextText', 'prevText', 'showPreviousBtn', 'okText', 'step', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['steps', 'localKey']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyGuide, self).__init__(**args)
