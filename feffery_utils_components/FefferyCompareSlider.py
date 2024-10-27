# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCompareSlider(Component):
    """A FefferyCompareSlider component.
卷帘比较组件FefferyCompareSlider

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- firstItem (a list of or a singular dash component, string or number; optional):
    组件型，设置进行比较的第一个元素.

- secondItem (a list of or a singular dash component, string or number; optional):
    组件型，设置进行比较的第二个元素.

- position (number; default 50):
    设置或监听当前卷帘比较组件的卷帘位置百分比，取值在`0`到`100`之间  默认值：`50`.

- onlyHandleDraggable (boolean; default True):
    是否仅拖拽控件部分可用于调整卷帘  默认值：`True`.

- boundsPadding (number; default 0):
    设置卷帘移动到两侧时，进行留白的像素距离  默认值：`0`.

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    设置卷帘方向，可选项有`'horizontal'`、`'vertical'`  默认值：`'horizontal'`.

- buttonStyle (dict; optional):
    拖拽控件按钮部分`css`样式.

- linesStyle (dict; optional):
    拖拽控件线条部分`css`样式.

- rootStyle (dict; optional):
    拖拽控件根元素部分`css`样式.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['firstItem', 'secondItem']
    _base_nodes = ['firstItem', 'secondItem', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCompareSlider'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, firstItem=Component.UNDEFINED, secondItem=Component.UNDEFINED, position=Component.UNDEFINED, onlyHandleDraggable=Component.UNDEFINED, boundsPadding=Component.UNDEFINED, direction=Component.UNDEFINED, buttonStyle=Component.UNDEFINED, linesStyle=Component.UNDEFINED, rootStyle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'firstItem', 'secondItem', 'position', 'onlyHandleDraggable', 'boundsPadding', 'direction', 'buttonStyle', 'linesStyle', 'rootStyle', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'firstItem', 'secondItem', 'position', 'onlyHandleDraggable', 'boundsPadding', 'direction', 'buttonStyle', 'linesStyle', 'rootStyle', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyCompareSlider, self).__init__(**args)
