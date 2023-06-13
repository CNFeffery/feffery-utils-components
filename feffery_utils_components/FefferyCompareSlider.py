# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyCompareSlider(Component):
    """A FefferyCompareSlider component.


Keyword arguments:

- id (string; optional)

- boundsPadding (number; default 0)

- buttonStyle (dict; optional):
    设置拖拽控件按钮部分的css样式.

- className (string; optional)

- direction (a value equal to: 'horizontal', 'vertical'; default 'horizontal')

- firstItem (a list of or a singular dash component, string or number; optional)

- linesStyle (dict; optional):
    设置拖拽控件线条部分的css样式.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- onlyHandleDraggable (boolean; default True)

- position (number; default 50)

- rootStyle (dict; optional):
    设置拖拽控件根元素部分的css样式.

- secondItem (a list of or a singular dash component, string or number; optional)

- style (dict; optional)"""
    _children_props = ['firstItem', 'secondItem']
    _base_nodes = ['firstItem', 'secondItem', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyCompareSlider'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, firstItem=Component.UNDEFINED, secondItem=Component.UNDEFINED, position=Component.UNDEFINED, onlyHandleDraggable=Component.UNDEFINED, boundsPadding=Component.UNDEFINED, direction=Component.UNDEFINED, buttonStyle=Component.UNDEFINED, linesStyle=Component.UNDEFINED, rootStyle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'boundsPadding', 'buttonStyle', 'className', 'direction', 'firstItem', 'linesStyle', 'loading_state', 'onlyHandleDraggable', 'position', 'rootStyle', 'secondItem', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'boundsPadding', 'buttonStyle', 'className', 'direction', 'firstItem', 'linesStyle', 'loading_state', 'onlyHandleDraggable', 'position', 'rootStyle', 'secondItem', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyCompareSlider, self).__init__(**args)
