# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferySeamlessScroll(Component):
    """A FefferySeamlessScroll component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    需要滚动展示的内容.

- id (string; optional):
    组件id.

- className (string | dict; optional):
    css类名.

- classOption (dict; default {    step: 1,    limitMoveNum: 5,    hoverStop: True,    direction: 1,    openTouch: True,    singleHeight: 0,    singleWidth: 0,    waitTime: 1000,    switchOffset: 30,    autoPlay: True,    switchSingleStep: 134,    switchDelay: 400,    switchDisabledClass: 'disabled',    isSingleRemUnit: False,    navigation: False}):
    设置配置项.

    `classOption` is a dict with keys:

    - autoPlay (boolean; optional):
        是否开启自动滚动，默认为True.

    - direction (number; optional):
        设置方向: 0往下，1往上，2向左，3向右，默认为1.

    - hoverStop (boolean; optional):
        设置是否启用鼠标hover控制，默认为True.

    - isSingleRemUnit (boolean; optional):
        设置singleHeight and singleWidth 是否开启rem度量，默认为False.

    - limitMoveNum (number; optional):
        设置开启无缝滚动的数据量，默认为5  默认：False.

    - navigation (boolean; optional):
        设置左右方向的滚动是否显示控制器按钮，True的时候autoPlay自动变为False，默认为False.

    - openTouch (boolean; optional):
        设置移动端是否开启touch滑动，默认为True.

    - singleHeight (number; optional):
        设置单步运动停止的高度(默认值0是无缝不停止的滚动)，direction为0|1时生效，默认为0.

    - singleWidth (number; optional):
        设置单步运动停止的宽度(默认值0是无缝不停止的滚动)，direction为2|3时生效，默认为0.

    - step (number; optional):
        设置滚动速度，数值越大速度滚动越快，默认为1。  step
        值不建议太小,不然会有卡顿效果(如果设置了单步滚动,step需是单步大小的约数,否则无法保证单步滚动结束的位置是否准确。
        比如单步设置的 30,step 不能为 4)。.

    - switchDelay (number; optional):
        设置单步切换的动画时间(ms)，默认为400.

    - switchDisabledClass (string; optional):
        设置不可以点击状态的switch按钮父元素的类名，默认为'disabled'.

    - switchOffset (number; optional):
        设置左右切换按钮距离左右边界的边距(px)，默认为30.

    - switchSingleStep (number; optional):
        设置手动单步切换step值(px)，默认为134.

    - waitTime (number; optional):
        设置单步停止等待时间(默认值 1000ms).

- data (list; required):
    无缝滚动list数据，组件内部只关注 data 数组的 length.

- key (string; optional):
    辅助刷新用唯一标识key值.

- leftSwitchChildren (a list of or a singular dash component, string or number; optional):
    左右切换时左切换区域内容.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- rightSwitchChildren (a list of or a singular dash component, string or number; optional):
    左右切换时右切换区域内容.

- style (dict; optional):
    自定义css字典."""
    _children_props = ['leftSwitchChildren', 'rightSwitchChildren']
    _base_nodes = ['leftSwitchChildren', 'rightSwitchChildren', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferySeamlessScroll'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, leftSwitchChildren=Component.UNDEFINED, rightSwitchChildren=Component.UNDEFINED, data=Component.REQUIRED, classOption=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classOption', 'data', 'key', 'leftSwitchChildren', 'loading_state', 'rightSwitchChildren', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classOption', 'data', 'key', 'leftSwitchChildren', 'loading_state', 'rightSwitchChildren', 'style']
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
