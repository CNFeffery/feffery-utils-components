# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyAutoFit(Component):
    """A FefferyAutoFit component.


Keyword arguments:

- id (string; optional):
    组件id.

- containerId (string; default 'body'):
    要进行自适应的目标元素id，默认为'body'.

- dw (number; default 1920):
    设计稿的宽度，默认是1920.

- dh (number; default 1080):
    设计稿的高度，默认是1080.

- resize (boolean; default True):
    是否监听resize事件，默认是True.

- ignore (list of dicts; optional):
    忽略缩放的元素列表（列表内的元素将反向缩放）.

    `ignore` is a list of dicts with keys:

    - el (string; optional):
        要忽略缩放的元素的选择器名.

- transition (number; default 0):
    过渡时间，默认是0.

- delay (number; default 0):
    延迟时间，默认是0.

- limit (number; default 0.1):
    默认是 0.1,当缩放阈值不大于此值时不缩放，比如设置为0.1时，0.9-1.1的范围会被重置为1.

- close (boolean; default False):
    关闭自适应，设置为True执行完相应操作后会自动重置为False，默认为False.

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
    _type = 'FefferyAutoFit'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, containerId=Component.UNDEFINED, dw=Component.UNDEFINED, dh=Component.UNDEFINED, resize=Component.UNDEFINED, ignore=Component.UNDEFINED, transition=Component.UNDEFINED, delay=Component.UNDEFINED, limit=Component.UNDEFINED, close=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'containerId', 'dw', 'dh', 'resize', 'ignore', 'transition', 'delay', 'limit', 'close', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'containerId', 'dw', 'dh', 'resize', 'ignore', 'transition', 'delay', 'limit', 'close', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyAutoFit, self).__init__(**args)
