# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyRND(Component):
    """A FefferyRND component.
尺寸可调可拖拽组件FefferyRND

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- defaultState (dict; optional):
    设置默认位置及尺寸状态.

    `defaultState` is a dict with keys:

    - x (number; optional):
        水平方向像素位置.

    - y (number; optional):
        竖直方向像素位置.

    - width (number | string; optional):
        宽度值，数值型表示像素宽度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等.

    - height (number | string; optional):
        高度值，数值型表示像素高度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等.

- size (dict; optional):
    设置或监听当前组件尺寸状态.

    `size` is a dict with keys:

    - width (number | string; optional):
        宽度值，数值型表示像素宽度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等.

    - height (number | string; optional):
        高度值，数值型表示像素高度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等.

- position (dict; optional):
    设置或监听当前组件位置状态.

    `position` is a dict with keys:

    - x (number; optional):
        水平方向像素位置.

    - y (number; optional):
        竖直方向像素位置.

- minWidth (number | string; optional):
    限制可调宽度下限，数值型表示像素宽度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等.

- minHeight (number | string; optional):
    限制可调高度下限，数值型表示像素宽度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等.

- maxWidth (number | string; optional):
    限制可调宽度上限，数值型表示像素宽度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等.

- maxHeight (number | string; optional):
    限制可调高度上限，数值型表示像素宽度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等.

- resizeGrid (list of numbers; optional):
    针对尺寸调整行为，设置水平和竖直方向上调整的像素步长，格式：`[水平像素步长, 竖直像素步长]`  默认值：`[1, 1]`.

- dragGrid (list of numbers; optional):
    针对位置拖拽行为，设置水平和竖直方向上拖拽的像素步长，格式：`[水平像素步长, 竖直像素步长]`  默认值：`[1, 1]`.

- lockAspectRatio (boolean | number; optional):
    配置高宽比锁定，传入`True`时，将锁定初始尺寸对应高宽比，传入数值型时，用于指定具体的高宽比  默认值：`False`.

- lockAspectRatioExtraWidth (number; optional):
    在`lockAspectRatio`基础上，设置额外像素宽度  默认值：`0`.

- lockAspectRatioExtraHeight (number; optional):
    在`lockAspectRatio`基础上，设置额外像素高度  默认值：`0`.

- direction (list of a value equal to: 'top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft's; default ['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft']):
    允许进行尺寸调整的方向，可多选，可选项有`'top'`、`'right'`、`'bottom'`、`'left'`、`'topRight'`、`'bottomRight'`、`'bottomLeft'`、`'topLeft'`
    默认值：`['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight',
    'bottomLeft', 'topLeft']`.

- disableDragging (boolean; optional):
    是否禁用拖拽功能.

- dragAxis (a value equal to: 'x', 'y', 'both', 'none'; optional):
    允许进行拖拽的方向，可选项有`'x'`、`'y'`、`'both'`、`'none'`.

- bounds (a value equal to: 'window', 'parent'; optional):
    设置当前组件尺寸调整及拖拽的外边界类型，可选项有`'window'`、`'parent'`  默认值：`'window'`.

- selected (boolean; default False):
    设置或监听当前组件是否处于选择状态  默认值：`False`.

- selectedStyle (dict; optional):
    设置当前组件在选中状态下的`css`样式.

- selectedClassName (string; optional):
    配置当前组件在选中状态下的`css`类名.

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
    _type = 'FefferyRND'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, defaultState=Component.UNDEFINED, size=Component.UNDEFINED, position=Component.UNDEFINED, minWidth=Component.UNDEFINED, minHeight=Component.UNDEFINED, maxWidth=Component.UNDEFINED, maxHeight=Component.UNDEFINED, resizeGrid=Component.UNDEFINED, dragGrid=Component.UNDEFINED, lockAspectRatio=Component.UNDEFINED, lockAspectRatioExtraWidth=Component.UNDEFINED, lockAspectRatioExtraHeight=Component.UNDEFINED, direction=Component.UNDEFINED, disableDragging=Component.UNDEFINED, dragAxis=Component.UNDEFINED, bounds=Component.UNDEFINED, selected=Component.UNDEFINED, selectedStyle=Component.UNDEFINED, selectedClassName=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'defaultState', 'size', 'position', 'minWidth', 'minHeight', 'maxWidth', 'maxHeight', 'resizeGrid', 'dragGrid', 'lockAspectRatio', 'lockAspectRatioExtraWidth', 'lockAspectRatioExtraHeight', 'direction', 'disableDragging', 'dragAxis', 'bounds', 'selected', 'selectedStyle', 'selectedClassName', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'defaultState', 'size', 'position', 'minWidth', 'minHeight', 'maxWidth', 'maxHeight', 'resizeGrid', 'dragGrid', 'lockAspectRatio', 'lockAspectRatioExtraWidth', 'lockAspectRatioExtraHeight', 'direction', 'disableDragging', 'dragAxis', 'bounds', 'selected', 'selectedStyle', 'selectedClassName', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyRND, self).__init__(children=children, **args)
