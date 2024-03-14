# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyRND(Component):
    """A FefferyRND component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    内部元素.

- id (string; optional):
    组件id.

- bounds (a value equal to: 'window', 'parent'; optional):
    设置当前组件尺寸调整及拖拽的外边界类型，可选的有'window'、'parent'  默认为'window'.

- className (string; optional):
    css类名.

- defaultState (dict; optional):
    设置默认位置及尺寸信息.

    `defaultState` is a dict with keys:

    - height (number | string; optional):
        高度值，数值型表示像素高度，字符型与css相关属性值格式兼容，如'300px'、'50%'等.

    - width (number | string; optional):
        宽度值，数值型表示像素宽度，字符型与css相关属性值格式兼容，如'300px'、'50%'等.

    - x (number; optional):
        水平方向像素位置.

    - y (number; optional):
        竖直方向像素位置.

- direction (list of a value equal to: 'top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft's; default ['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft']):
    设置允许进行尺寸调整的方向，多选，可选项有'top'、'right'、'bottom'、'left'、'topRight'、'bottomRight'、'bottomLeft'、'topLeft'
    默认为['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight',
    'bottomLeft', 'topLeft'].

- disableDragging (boolean; optional):
    是否禁用拖拽功能.

- dragAxis (a value equal to: 'x', 'y', 'both', 'none'; optional):
    允许进行拖拽的方向，可选的有'x'、'y'、'both'、'none'.

- dragGrid (list of numbers; optional):
    针对位置拖拽行为，设置水平和竖直方向上拖拽的像素步长，格式为：[水平像素步长, 竖直像素步长]  默认：[1, 1].

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

- lockAspectRatio (boolean | number; optional):
    配置高宽比锁定  传入True时，将锁定初始尺寸对应高宽比  传入数值型时，用于指定具体的高宽比  默认：False.

- lockAspectRatioExtraHeight (number; optional):
    在lockAspectRatio基础上，设置额外像素高度  默认：0.

- lockAspectRatioExtraWidth (number; optional):
    在lockAspectRatio基础上，设置额外像素宽度  默认：0.

- maxHeight (number | string; optional):
    限制可调高度上限，数值型表示像素宽度，字符型与css相关属性值格式兼容，如'300px'、'50%'等.

- maxWidth (number | string; optional):
    限制可调宽度上限，数值型表示像素宽度，字符型与css相关属性值格式兼容，如'300px'、'50%'等.

- minHeight (number | string; optional):
    限制可调高度下限，数值型表示像素宽度，字符型与css相关属性值格式兼容，如'300px'、'50%'等.

- minWidth (number | string; optional):
    限制可调宽度下限，数值型表示像素宽度，字符型与css相关属性值格式兼容，如'300px'、'50%'等.

- position (dict; optional):
    设置或监听当前组件位置信息.

    `position` is a dict with keys:

    - x (number; optional):
        水平方向像素位置.

    - y (number; optional):
        竖直方向像素位置.

- resizeGrid (list of numbers; optional):
    针对尺寸调整行为，设置水平和竖直方向上调整的像素步长，格式为：[水平像素步长, 竖直像素步长]  默认：[1, 1].

- selected (boolean; default False):
    设置或监听当前组件是否处于选择状态  默认：False.

- selectedClassName (string; optional):
    配置当前组件在选中状态下的css类名.

- selectedStyle (dict; optional):
    设置当前组件在选中状态下的css样式.

- size (dict; optional):
    设置或监听当前组件尺寸信息.

    `size` is a dict with keys:

    - height (number | string; optional):
        高度值，数值型表示像素高度，字符型与css相关属性值格式兼容，如'300px'、'50%'等.

    - width (number | string; optional):
        宽度值，数值型表示像素宽度，字符型与css相关属性值格式兼容，如'300px'、'50%'等.

- style (dict; optional):
    css样式."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyRND'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, defaultState=Component.UNDEFINED, size=Component.UNDEFINED, position=Component.UNDEFINED, minWidth=Component.UNDEFINED, minHeight=Component.UNDEFINED, maxWidth=Component.UNDEFINED, maxHeight=Component.UNDEFINED, resizeGrid=Component.UNDEFINED, dragGrid=Component.UNDEFINED, lockAspectRatio=Component.UNDEFINED, lockAspectRatioExtraWidth=Component.UNDEFINED, lockAspectRatioExtraHeight=Component.UNDEFINED, direction=Component.UNDEFINED, disableDragging=Component.UNDEFINED, dragAxis=Component.UNDEFINED, bounds=Component.UNDEFINED, selected=Component.UNDEFINED, selectedStyle=Component.UNDEFINED, selectedClassName=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bounds', 'className', 'defaultState', 'direction', 'disableDragging', 'dragAxis', 'dragGrid', 'key', 'loading_state', 'lockAspectRatio', 'lockAspectRatioExtraHeight', 'lockAspectRatioExtraWidth', 'maxHeight', 'maxWidth', 'minHeight', 'minWidth', 'position', 'resizeGrid', 'selected', 'selectedClassName', 'selectedStyle', 'size', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bounds', 'className', 'defaultState', 'direction', 'disableDragging', 'dragAxis', 'dragGrid', 'key', 'loading_state', 'lockAspectRatio', 'lockAspectRatioExtraHeight', 'lockAspectRatioExtraWidth', 'maxHeight', 'maxWidth', 'minHeight', 'minWidth', 'position', 'resizeGrid', 'selected', 'selectedClassName', 'selectedStyle', 'size', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyRND, self).__init__(children=children, **args)
