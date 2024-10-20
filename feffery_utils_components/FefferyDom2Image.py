# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDom2Image(Component):
    """A FefferyDom2Image component.
元素转图片组件FefferyDom2Image

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- targetSelector (string; optional):
    设置目标元素选择器，每次执行转换操作后都会重置为空值.

- scale (number; default 1):
    精度缩放比例  默认值：`1`.

- screenshotResult (dict; optional):
    监听最近一次元素转图片的结果数据.

    `screenshotResult` is a dict with keys:

    - selector (string; optional):
        记录本次转换结果对应的选择器.

    - status (a value equal to: 'success', 'failed'; optional):
        记录本次转换任务的执行状态，可选项有`'success'`、`'failed'`.

    - dataUrl (string; optional):
        若本次转换成功，则记录转换后的图片dataUrl信息.

    - timestamp (number; optional):
        对应当前任务完成的时间戳.

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
    _type = 'FefferyDom2Image'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, targetSelector=Component.UNDEFINED, scale=Component.UNDEFINED, screenshotResult=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'targetSelector', 'scale', 'screenshotResult', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'targetSelector', 'scale', 'screenshotResult', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDom2Image, self).__init__(**args)
