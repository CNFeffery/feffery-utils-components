# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyListenScroll(Component):
    """A FefferyListenScroll component.
滚动条监听组件FefferyListenScroll

Keyword arguments:

- id (string; optional):
    组件id.

- arrivedState (dict; optional):
    监听目标滚动条的到达边界状态.

- directions (dict; optional):
    监听目标滚动条的滚动方向.

- idle (number; optional):
    滚动结束行为的检查时长，单位：毫秒，当`throttle>0`时，检查时长将为`throttle+idle`  默认：`0`.

- isScrolling (boolean; optional):
    监听目标滚动条是否正在滚动中.

- key (string; optional):
    强制刷新用key值.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- offset (number; optional):
    针对到达边界状态，设置像素阈值  默认：`0`.

- position (dict; optional):
    监听目标滚动条的水平及竖直方向上的像素偏移量.

- target (string; optional):
    设置滚动条监听目标元素id，默认为整个页面.

- throttle (number; optional):
    滚动事件监听节流时长，单位：毫秒  默认：`0`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyListenScroll'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, target=Component.UNDEFINED, position=Component.UNDEFINED, isScrolling=Component.UNDEFINED, arrivedState=Component.UNDEFINED, directions=Component.UNDEFINED, throttle=Component.UNDEFINED, idle=Component.UNDEFINED, offset=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'arrivedState', 'directions', 'idle', 'isScrolling', 'key', 'loading_state', 'offset', 'position', 'target', 'throttle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'arrivedState', 'directions', 'idle', 'isScrolling', 'key', 'loading_state', 'offset', 'position', 'target', 'throttle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyListenScroll, self).__init__(**args)
