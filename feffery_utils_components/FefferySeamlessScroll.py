# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferySeamlessScroll(Component):
    """A FefferySeamlessScroll component.
无缝滚动组件FefferySeamlessScroll

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，设置需要滚动展示的内容.

- style (dict; optional):
    当前组件css样式.

- className (string | dict; optional):
    当前组件css类名.

- leftSwitchChildren (a list of or a singular dash component, string or number; optional):
    组件型，左右切换时左切换区域内容.

- rightSwitchChildren (a list of or a singular dash component, string or number; optional):
    组件型，左右切换时右切换区域内容.

- data (list; required):
    无缝滚动对应列表数据.

- classOption (dict; default {    step: 1,    limitMoveNum: 5,    hoverStop: True,    direction: 1,    openTouch: True,    singleHeight: 0,    singleWidth: 0,    waitTime: 1000,    switchOffset: 30,    autoPlay: True,    switchSingleStep: 134,    switchDelay: 400,    switchDisabledClass: 'disabled',    isSingleRemUnit: False,    navigation: False}):
    配置功能.

    `classOption` is a dict with keys:

    - step (number; optional):
        滚动速度，数值越大速度滚动越快  默认值：`1`.

    - limitMoveNum (number; optional):
        开启无缝滚动的数据量  默认值：`5`.

    - hoverStop (boolean; optional):
        是否启用鼠标移入控制  默认值：`True`.

    - direction (number; optional):
        方向，可选项有`0`（向下）、`1`（向上）、`2`（向左）、`3`（向右）  默认值：`1`.

    - openTouch (boolean; optional):
        移动端是否开启触碰滑动  默认值：`True`.

    - singleHeight (number; optional):
        单步运动停止的高度，`direction`为`0`、`1`时生效  默认值：`0`.

    - singleWidth (number; optional):
        单步运动停止的宽度，`direction`为`2`、`3`时生效  默认值：`0`.

    - waitTime (number; optional):
        单步停止等待时间，单位：毫秒  默认值：`1000`.

    - switchOffset (number; optional):
        左右切换按钮距离左右边界的像素边距  默认值：`30`.

    - autoPlay (boolean; optional):
        是否开启自动滚动  默认值：`True`.

    - switchSingleStep (number; optional):
        手动单步切换像素`step`值  默认值：`134`.

    - switchDelay (number; optional):
        单步切换的动画时间，单位：毫秒  默认值：`400`.

    - switchDisabledClass (string; optional):
        不可点击状态对应控件父元素`css`类名  默认值：`'disabled'`.

    - isSingleRemUnit (boolean; optional):
        `singleHeight`、`singleWidth`是否开启`rem`度量  默认值：`False`.

    - navigation (boolean; optional):
        左右方向的滚动是否显示控制器按钮，传入`True`时`autoPlay`将自动变为`False`  默认值：`False`.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['leftSwitchChildren', 'rightSwitchChildren']
    _base_nodes = ['leftSwitchChildren', 'rightSwitchChildren', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferySeamlessScroll'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, leftSwitchChildren=Component.UNDEFINED, rightSwitchChildren=Component.UNDEFINED, data=Component.REQUIRED, classOption=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'leftSwitchChildren', 'rightSwitchChildren', 'data', 'classOption', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'leftSwitchChildren', 'rightSwitchChildren', 'data', 'classOption', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferySeamlessScroll, self).__init__(children=children, **args)
