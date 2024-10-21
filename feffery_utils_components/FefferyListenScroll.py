# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyListenScroll(Component):
    """A FefferyListenScroll component.
滚动条监听组件FefferyListenScroll

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- target (string; optional):
    设置滚动条监听目标元素`id`，默认为整个页面.

- position (dict; optional):
    监听目标滚动条的水平及竖直方向上的像素偏移量.

- isScrolling (boolean; optional):
    监听目标滚动条是否正在滚动中.

- arrivedState (dict; optional):
    监听目标滚动条的到达边界状态.

- directions (dict; optional):
    监听目标滚动条的滚动方向.

- throttle (number; optional):
    滚动事件监听节流时长，单位：毫秒  默认值：`0`.

- idle (number; optional):
    滚动结束行为的检查时长，单位：毫秒，当`throttle>0`时，检查时长将为`throttle+idle`  默认值：`0`.

- offset (dict; optional):
    针对各个方向的到达边界状态，设置像素阈值.

    `offset` is a dict with keys:

    - top (number; optional):
        上顶端到达边界像素阈值.

    - bottom (number; optional):
        下底部到达边界像素阈值.

    - left (number; optional):
        左侧到达边界像素阈值.

    - right (number; optional):
        右侧到达边界像素阈值.

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
    _type = 'FefferyListenScroll'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, target=Component.UNDEFINED, position=Component.UNDEFINED, isScrolling=Component.UNDEFINED, arrivedState=Component.UNDEFINED, directions=Component.UNDEFINED, throttle=Component.UNDEFINED, idle=Component.UNDEFINED, offset=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'target', 'position', 'isScrolling', 'arrivedState', 'directions', 'throttle', 'idle', 'offset', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'target', 'position', 'isScrolling', 'arrivedState', 'directions', 'throttle', 'idle', 'offset', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyListenScroll, self).__init__(**args)
