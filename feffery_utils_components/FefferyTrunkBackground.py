# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyTrunkBackground(Component):
    """A FefferyTrunkBackground component.
3D-Trunk背景组件FefferyTrunkBackground

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，设置内嵌元素内容.

- style (dict; optional):
    当前组件css样式.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- mouseControls (boolean; default True):
    设置是否开启鼠标控制  默认为`True`.

- touchControls (boolean; default True):
    设置是否开启触摸控制  默认为`True`.

- gyroControls (boolean; default False):
    设置是否开启陀螺仪控制  默认为`False`.

- minHeight (number; default 200.00):
    设置最小高度  默认为`200.00`.

- minWidth (number; default 200.00):
    设置最小宽度  默认为`200.00`.

- scale (number; default 1.00):
    设置比例  默认为`1.00`.

- scaleMobile (number; default 1.00):
    设置移动端比例  默认为`1.00`.

- backgroundColor (string; default '#222426'):
    设置背景颜色  默认为`'#222426'`.

- color (string; default '#98465f'):
    设置`trunk`颜色  默认为`'#98465f'`.

- spacing (number; default 0):
    设置trunk间距，范围`0`到`10`  默认为`0`.

- chaos (number; default 1):
    设置`trunk`混乱程度，范围`0`到`10`  默认为`1`.

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
    _type = 'FefferyTrunkBackground'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, mouseControls=Component.UNDEFINED, touchControls=Component.UNDEFINED, gyroControls=Component.UNDEFINED, minHeight=Component.UNDEFINED, minWidth=Component.UNDEFINED, scale=Component.UNDEFINED, scaleMobile=Component.UNDEFINED, backgroundColor=Component.UNDEFINED, color=Component.UNDEFINED, spacing=Component.UNDEFINED, chaos=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'scale', 'scaleMobile', 'backgroundColor', 'color', 'spacing', 'chaos', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'scale', 'scaleMobile', 'backgroundColor', 'color', 'spacing', 'chaos', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyTrunkBackground, self).__init__(children=children, **args)
