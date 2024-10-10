# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyHaloBackground(Component):
    """A FefferyHaloBackground component.


Keyword arguments:

- id (string; optional):
    组件id.

- children (a list of or a singular dash component, string or number; optional):
    设置内嵌元素内容.

- className (string | dict; optional):
    css类名.

- style (dict; optional):
    自定义css字典.

- key (string; optional):
    辅助刷新用唯一标识key值.

- mouseControls (boolean; default True):
    设置是否开启鼠标控制，默认为True.

- touchControls (boolean; default True):
    设置是否开启触摸控制，默认为True.

- gyroControls (boolean; default False):
    设置是否开启陀螺仪控制，默认为False.

- minHeight (number; default 200.00):
    设置最小高度，默认为200.00.

- minWidth (number; default 200.00):
    设置最小宽度，默认为200.00.

- backgroundColor (string; default '#131a43'):
    设置背景颜色，默认为'#131a43'.

- baseColor (string; default '#112966'):
    设置基本颜色，默认为'#112966'.

- size (number; default 1):
    设置动画大小，范围0.1到3，默认为1.

- amplitudeFactor (number; default 1):
    设置动画振幅因子，范围0到3，默认为1.

- xOffset (number; default 0):
    设置x轴偏移量，范围为-0.5到0.5，默认为0.

- yOffset (number; default 0):
    设置y轴偏移量，范围为-0.5到0.5，默认为0.

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
    _type = 'FefferyHaloBackground'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, mouseControls=Component.UNDEFINED, touchControls=Component.UNDEFINED, gyroControls=Component.UNDEFINED, minHeight=Component.UNDEFINED, minWidth=Component.UNDEFINED, backgroundColor=Component.UNDEFINED, baseColor=Component.UNDEFINED, size=Component.UNDEFINED, amplitudeFactor=Component.UNDEFINED, xOffset=Component.UNDEFINED, yOffset=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'children', 'className', 'style', 'key', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'backgroundColor', 'baseColor', 'size', 'amplitudeFactor', 'xOffset', 'yOffset', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'children', 'className', 'style', 'key', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'backgroundColor', 'baseColor', 'size', 'amplitudeFactor', 'xOffset', 'yOffset', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyHaloBackground, self).__init__(children=children, **args)
