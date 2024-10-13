# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyBirdsBackground(Component):
    """A FefferyBirdsBackground component.
3D-Birds背景组件FefferyBirdsBackground

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
    设置是否开启鼠标控  默认为`True`.

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

- backgroundColor (string; default '#000000'):
    设置背景颜色  默认为`'#000000'`.

- backgroundAlpha (number; default 1):
    设置背景颜色透明度，范围`0`到`1`  默认为`1`.

- color1 (string; default '#ff0000'):
    设置birds颜色1  默认为`'#ff0000'`.

- color2 (string; default '#13becf'):
    设置birds颜色2  默认为`'#13becf'`.

- colorMode (a value equal to: 'lerp', 'variance', 'lerpGradient', 'varianceGradient'; default 'varianceGradient'):
    设置颜色模式，可选的有`'lerp'`、`'variance'`、`'lerpGradient'`、`'varianceGradient'`
    默认为`'varianceGradient'`.

- quantity (number; default 5):
    设置背景质量，范围`1`到`5`  默认为`5`.

- birdSize (number; default 1):
    设置birds大小，范围`1`到`4`  默认为`1`.

- wingSpan (number; default 30):
    设置birds翼展，范围`10`到`40`  默认为`30`.

- speedLimit (number; default 5):
    设置birds速度限制，范围`1`到`10`  默认为`5`.

- separation (number; default 20):
    设置birds分离大小，范围`1`到`100  默认为`20`.

- alignment (number; default 20):
    设置birds对齐大小，范围`1`到`100`  默认为`20`.

- cohesion (number; default 20):
    设置birds内聚大小，范围`1`到`100`  默认为`20`.

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
    _type = 'FefferyBirdsBackground'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, mouseControls=Component.UNDEFINED, touchControls=Component.UNDEFINED, gyroControls=Component.UNDEFINED, minHeight=Component.UNDEFINED, minWidth=Component.UNDEFINED, scale=Component.UNDEFINED, scaleMobile=Component.UNDEFINED, backgroundColor=Component.UNDEFINED, backgroundAlpha=Component.UNDEFINED, color1=Component.UNDEFINED, color2=Component.UNDEFINED, colorMode=Component.UNDEFINED, quantity=Component.UNDEFINED, birdSize=Component.UNDEFINED, wingSpan=Component.UNDEFINED, speedLimit=Component.UNDEFINED, separation=Component.UNDEFINED, alignment=Component.UNDEFINED, cohesion=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'scale', 'scaleMobile', 'backgroundColor', 'backgroundAlpha', 'color1', 'color2', 'colorMode', 'quantity', 'birdSize', 'wingSpan', 'speedLimit', 'separation', 'alignment', 'cohesion', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'mouseControls', 'touchControls', 'gyroControls', 'minHeight', 'minWidth', 'scale', 'scaleMobile', 'backgroundColor', 'backgroundAlpha', 'color1', 'color2', 'colorMode', 'quantity', 'birdSize', 'wingSpan', 'speedLimit', 'separation', 'alignment', 'cohesion', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyBirdsBackground, self).__init__(children=children, **args)
