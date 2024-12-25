# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyFullscreen(Component):
    """A FefferyFullscreen component.
全屏化组件FefferyFullscreen

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- targetId (string; optional):
    设置要全屏化的目标元素id，缺省时会以整个页面作为全屏化目标.

- isFullscreen (boolean; default False):
    设置或监听目标元素的全屏化状态  默认值：`False`.

- pageFullscreen (dict; default False):
    配置是否启用页面全屏，可进一步设置页面全屏根元素对应的css类名及`z-index`值  默认值：`False`.

    `pageFullscreen` is a boolean | dict with keys:

    - className (string; optional):
        设置页面全屏根元素对应的css类名.

    - zIndex (number; optional):
        设置页面全屏根元素对应的`z-index`值.

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
    _type = 'FefferyFullscreen'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, targetId=Component.UNDEFINED, isFullscreen=Component.UNDEFINED, pageFullscreen=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'targetId', 'isFullscreen', 'pageFullscreen', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'targetId', 'isFullscreen', 'pageFullscreen', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyFullscreen, self).__init__(**args)
