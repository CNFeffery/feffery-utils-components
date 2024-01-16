# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCloudsBackground(Component):
    """A FefferyCloudsBackground component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    设置内嵌元素内容.

- id (string; optional):
    组件id.

- backgroundColor (string; default '#ffffff'):
    设置背景颜色，默认为'#ffffff'.

- className (string | dict; optional):
    css类名.

- cloudColor (string; default '#adc1de'):
    设置云颜色，默认为'#adc1de'.

- cloudShadowColor (string; default '#183550'):
    设置云阴影颜色，默认为'#183550'.

- gyroControls (boolean; default False):
    设置是否开启陀螺仪控制，默认为False.

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

- minHeight (number; default 200.00):
    设置最小高度，默认为200.00.

- minWidth (number; default 200.00):
    设置最小宽度，默认为200.00.

- mouseControls (boolean; default True):
    设置是否开启鼠标控制，默认为True.

- skyColor (string; default '#68b8d7'):
    设置天空颜色，默认为'#68b8d7'.

- speed (number; default 1):
    设置动画速度，范围0到3，默认为1.

- style (dict; optional):
    自定义css字典.

- sunColor (string; default '#ff9919'):
    设置太阳颜色，默认为'#ff9919'.

- sunGlareColor (string; default '#ff6633'):
    设置太阳炫光颜色，默认为'#ff6633'.

- sunlightColor (string; default '#ff9933'):
    设置太阳光线颜色，默认为'#ff9933'.

- touchControls (boolean; default True):
    设置是否开启触摸控制，默认为True."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCloudsBackground'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, mouseControls=Component.UNDEFINED, touchControls=Component.UNDEFINED, gyroControls=Component.UNDEFINED, minHeight=Component.UNDEFINED, minWidth=Component.UNDEFINED, backgroundColor=Component.UNDEFINED, skyColor=Component.UNDEFINED, cloudColor=Component.UNDEFINED, cloudShadowColor=Component.UNDEFINED, sunColor=Component.UNDEFINED, sunGlareColor=Component.UNDEFINED, sunlightColor=Component.UNDEFINED, speed=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'backgroundColor', 'className', 'cloudColor', 'cloudShadowColor', 'gyroControls', 'key', 'loading_state', 'minHeight', 'minWidth', 'mouseControls', 'skyColor', 'speed', 'style', 'sunColor', 'sunGlareColor', 'sunlightColor', 'touchControls']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'backgroundColor', 'className', 'cloudColor', 'cloudShadowColor', 'gyroControls', 'key', 'loading_state', 'minHeight', 'minWidth', 'mouseControls', 'skyColor', 'speed', 'style', 'sunColor', 'sunGlareColor', 'sunlightColor', 'touchControls']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyCloudsBackground, self).__init__(children=children, **args)
