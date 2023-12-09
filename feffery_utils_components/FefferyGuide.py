# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyGuide(Component):
    """A FefferyGuide component.


Keyword arguments:

- id (string; optional):
    组件id.

- arrow (boolean; optional):
    设置展示面板是否添加箭头，默认为True.

- className (string; optional):
    css类名.

- closable (boolean; optional):
    设置是否允许跳过引导，默认为True.

- hotspot (boolean; optional):
    设置展示面板是否展示热点标识，默认为False.

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

- localKey (string; required):
    用于设置本地缓存唯一标识key，从而辅助应用判断是否已展示过该引导页.

- locale (a value equal to: 'zh', 'en'; default 'zh'):
    设置语言，可选的有'en'、'zh'，默认为'zh'.

- mask (boolean; default True):
    设置是否展示蒙版层，默认为True.

- maskClassName (string; optional):
    设置蒙版层css类.

- modalClassName (string; optional):
    设置弹窗的css类.

- nextText (string; optional):
    设置“下一步”按钮的文案信息.

- okText (string; optional):
    设置确认按钮的文案信息.

- prevText (string; optional):
    设置“上一步”按钮的文案信息.

- showPreviousBtn (boolean; default True):
    设置是否显示“上一步”按钮，默认为True.

- step (number; optional):
    设置初始化时的起始步骤，为-1时则不显示引导组件，默认为0.

- stepText (string; optional):
    自定义步骤信息展示内容的回调函数，默认为\"(stepIndex, stepCount) => { return
    '第${stepIndex}步，共${stepCount}步'; }\".

- steps (list of dicts; required):
    必填，用于构造每一步锚定的页面元素.

    `steps` is a list of dicts with keys:

    - content (a list of or a singular dash component, string or number; optional):
        设置展示面板的描述内容.

    - offset (dict; optional):
        设置展示面板的像素偏移量.

        `offset` is a dict with keys:

        - x (number; optional):
            水平方向偏移像素距离.

        - y (number; optional):
            竖直方向偏移像素距离.

    - placement (a value equal to: 'top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right', 'left-top', 'left-bottom', 'right-top', 'right-bottom'; optional):
        设置展示面板相对锚点的方位，可选的有'top', 'bottom', 'left', 'right',
        'top-left', 'top-right', 'bottom-left', 'bottom-right',
        'left-top', 'left-bottom',  'right-top',
        'right-bottom'，默认为'bottom'.

    - selector (string; optional):
        对应当前步骤锚定的元素对应的css选择器.

    - targetPos (dict; optional):
        当selector参数缺省时，可用targetPos参数基于绝对位置进行步骤锚定.

        `targetPos` is a dict with keys:

        - height (number; optional):
            设置锚定范围像素高度.

        - left (number; optional):
            设置距离左端的像素距离.

        - top (number; optional):
            设置距离顶部的像素距离.

        - width (number; optional):
            设置锚定范围像素宽度.

    - title (a list of or a singular dash component, string or number; optional):
        设置展示面板的标题内容.

- style (dict; optional):
    自定义css字典."""
    _children_props = ['steps[].title', 'steps[].content']
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyGuide'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, locale=Component.UNDEFINED, steps=Component.REQUIRED, localKey=Component.REQUIRED, closable=Component.UNDEFINED, modalClassName=Component.UNDEFINED, maskClassName=Component.UNDEFINED, mask=Component.UNDEFINED, arrow=Component.UNDEFINED, hotspot=Component.UNDEFINED, stepText=Component.UNDEFINED, nextText=Component.UNDEFINED, prevText=Component.UNDEFINED, showPreviousBtn=Component.UNDEFINED, okText=Component.UNDEFINED, step=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'arrow', 'className', 'closable', 'hotspot', 'key', 'loading_state', 'localKey', 'locale', 'mask', 'maskClassName', 'modalClassName', 'nextText', 'okText', 'prevText', 'showPreviousBtn', 'step', 'stepText', 'steps', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'arrow', 'className', 'closable', 'hotspot', 'key', 'loading_state', 'localKey', 'locale', 'mask', 'maskClassName', 'modalClassName', 'nextText', 'okText', 'prevText', 'showPreviousBtn', 'step', 'stepText', 'steps', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['localKey', 'steps']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyGuide, self).__init__(**args)
