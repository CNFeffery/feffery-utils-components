# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyScroll(Component):
    """A FefferyScroll component.
滚动操作组件FefferyScroll

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- scrollMode (a value equal to: 'to-top', 'to-bottom', 'top-offset', 'relative-offset', 'target'; default 'to-top'):
    设置页面滚动模式，可选的有`'to-top'`、`'to-bottom'`、`'top-offset'`、`'relative-offset'`、`'target'`
    默认值：`'to-top'`.

- executeScroll (boolean; default False):
    用于指示是否进行滚动操作，在回调中设置`executeScroll`参数Output为`True`从而触发新一次滚动，每次由`executeScroll=True`触发的滚动完成后，`executeScroll`会自动重置为`False`
    默认值：`False`.

- scrollTopOffset (number; optional):
    当`scrollMode='top-offset'`时，用于设置滚动终点距离页面顶端的像素.

- scrollRelativeOffset (number; optional):
    当`scrollMode='relative-offset'`时，用于设置相对滚动的像素距离，负数则为向上滚动.

- scrollTargetId (string; optional):
    当`scrollMode='target'`时，用于设置滚动目标元素的id信息.

- duration (number; default 500):
    用于设置滚动过程耗时（单位：毫秒）  默认值：`500`.

- smooth (boolean | a value equal to: 'linear', 'easeInQuad', 'easeOutQuad', 'easeInOutQuad', 'easeInCubic', 'easeOutCubic', 'easeInOutCubic', 'easeInQuart', 'easeOutQuart', 'easeInOutQuart', 'easeInQuint', 'easeOutQuint', 'easeInOutQuint'; default True):
    用于设置滚动过程动画模式  默认值：True.

- delay (number; default 0):
    用于设置滚动延时（单位：毫秒）  默认值：0.

- containerId (string; optional):
    当滚动目标位于局部滚动条内时，用于设置局部滚动条所在的容器id信息.

- offset (number; optional):
    设置滚动过程的额外偏移像素距离.

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
    _type = 'FefferyScroll'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, scrollMode=Component.UNDEFINED, executeScroll=Component.UNDEFINED, scrollTopOffset=Component.UNDEFINED, scrollRelativeOffset=Component.UNDEFINED, scrollTargetId=Component.UNDEFINED, duration=Component.UNDEFINED, smooth=Component.UNDEFINED, delay=Component.UNDEFINED, containerId=Component.UNDEFINED, offset=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'scrollMode', 'executeScroll', 'scrollTopOffset', 'scrollRelativeOffset', 'scrollTargetId', 'duration', 'smooth', 'delay', 'containerId', 'offset', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'scrollMode', 'executeScroll', 'scrollTopOffset', 'scrollRelativeOffset', 'scrollTargetId', 'duration', 'smooth', 'delay', 'containerId', 'offset', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyScroll, self).__init__(**args)
