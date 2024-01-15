# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCellsBackground(Component):
    """A FefferyCellsBackground component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    设置内嵌元素内容.

- id (string; optional):
    组件id.

- className (string | dict; optional):
    css类名.

- color1 (string; default '#109090'):
    设置cells颜色1，默认为'#109090'.

- color2 (string; default '#f2e735'):
    设置cells颜色2，默认为'#f2e735'.

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

- scale (number; default 1.00):
    设置比例，默认为1.00.

- size (number; default 1.5):
    设置cells大小，范围0.2到5，默认为1.5.

- speed (number; default 1):
    设置cells动画速度，范围0到5，默认为1.

- style (dict; optional):
    自定义css字典.

- touchControls (boolean; default True):
    设置是否开启触摸控制，默认为True."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCellsBackground'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, mouseControls=Component.UNDEFINED, touchControls=Component.UNDEFINED, gyroControls=Component.UNDEFINED, minHeight=Component.UNDEFINED, minWidth=Component.UNDEFINED, scale=Component.UNDEFINED, color1=Component.UNDEFINED, color2=Component.UNDEFINED, size=Component.UNDEFINED, speed=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'color1', 'color2', 'gyroControls', 'key', 'loading_state', 'minHeight', 'minWidth', 'mouseControls', 'scale', 'size', 'speed', 'style', 'touchControls']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'color1', 'color2', 'gyroControls', 'key', 'loading_state', 'minHeight', 'minWidth', 'mouseControls', 'scale', 'size', 'speed', 'style', 'touchControls']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyCellsBackground, self).__init__(children=children, **args)
