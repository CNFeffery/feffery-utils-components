# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDom2Image(Component):
    """A FefferyDom2Image component.


Keyword arguments:

- id (string; optional):
    组件id.

- key (string; optional):
    强制刷新用.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- scale (number; default 1):
    精度缩放比例，默认为1.

- screenshotResult (dict; optional):
    监听最近一次元素转图片的结果数据.

    `screenshotResult` is a dict with keys:

    - dataUrl (string; optional):
        若本次转换成功，则记录转换后的图片dataUrl信息.

    - selector (string; optional):
        记录本次转换结果对应的选择器.

    - status (a value equal to: 'success', 'failed'; optional):
        记录本次转换任务的执行状态，可选的有'success'、'failed'.

    - timestamp (number; optional):
        对应当前任务完成的时间戳.

- targetSelector (string; optional):
    设置目标元素选择器，每次执行转换操作后都会重置为空值."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDom2Image'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, targetSelector=Component.UNDEFINED, scale=Component.UNDEFINED, screenshotResult=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'loading_state', 'scale', 'screenshotResult', 'targetSelector']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'loading_state', 'scale', 'screenshotResult', 'targetSelector']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDom2Image, self).__init__(**args)
