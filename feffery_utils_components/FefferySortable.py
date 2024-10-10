# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferySortable(Component):
    """A FefferySortable component.


Keyword arguments:

- id (string; optional):
    组件id.

- style (dict; optional):
    组件css样式.

- handleStyle (dict; optional):
    拖拽手柄css样式.

- handleClassName (string | dict; optional):
    拖拽手柄css类.

- className (string | dict; optional):
    组件css类.

- key (string; optional):
    强制刷新用.

- items (list of dicts; required):
    必填参数，用于定义子项源数组，数组顺序不会受拖拽排序结果影响.

    `items` is a list of dicts with keys:

    - key (number | string; required):
        对应当前子元素的唯一标识.

    - content (a list of or a singular dash component, string or number; optional):
        当前子元素内容.

    - style (dict; optional):
        当前子元素容器css样式.

    - className (string | dict; optional):
        当前子元素容器css类.

    - draggingStyle (dict; optional):
        当前子元素处于拖拽中状态下的css样式.

    - draggingClassName (string | dict; optional):
        当前子元素处于拖拽中状态下的css类.

- direction (a value equal to: 'vertical', 'horizontal'; default 'vertical'):
    设置排序列表的方向，可选的有'vertical'和'horizontal'  默认：'vertical'.

- itemDraggingScale (number; default 1):
    设置子项处于拖拽中状态下的缩放比例，默认为1即不缩放.

- handlePosition (a value equal to: 'start', 'end'; default 'end'):
    设置拖拽手柄位置，默认为'end'.

- handleType (a value equal to: 'holder', 'menu', 'drag'; default 'holder'):
    设置内置的推拽手柄图标类型，默认为'holder'.

- maxTranslateX (number; optional):
    限制横向拖拽最大像素偏移距离，默认无限制.

- maxTranslateY (number; optional):
    限制纵向拖拽最大像素偏移距离，默认无限制.

- currentOrder (list of number | strings; optional):
    监听或设置当前各子项呈现的顺序.

- value (number | string | list of number | strings; optional):
    设置或监听当前处于选中状态的子项key值.

- multiple (boolean; default False):
    是否允许多选  默认：False.

- allowNoValue (boolean; default True):
    是否允许无选中项  默认：True.

- selectedStyle (dict; optional):
    针对已选中项设置额外的css样式.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['items[].content']
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferySortable'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, handleStyle=Component.UNDEFINED, handleClassName=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, items=Component.REQUIRED, direction=Component.UNDEFINED, itemDraggingScale=Component.UNDEFINED, handlePosition=Component.UNDEFINED, handleType=Component.UNDEFINED, maxTranslateX=Component.UNDEFINED, maxTranslateY=Component.UNDEFINED, currentOrder=Component.UNDEFINED, value=Component.UNDEFINED, multiple=Component.UNDEFINED, allowNoValue=Component.UNDEFINED, selectedStyle=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'style', 'handleStyle', 'handleClassName', 'className', 'key', 'items', 'direction', 'itemDraggingScale', 'handlePosition', 'handleType', 'maxTranslateX', 'maxTranslateY', 'currentOrder', 'value', 'multiple', 'allowNoValue', 'selectedStyle', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'style', 'handleStyle', 'handleClassName', 'className', 'key', 'items', 'direction', 'itemDraggingScale', 'handlePosition', 'handleType', 'maxTranslateX', 'maxTranslateY', 'currentOrder', 'value', 'multiple', 'allowNoValue', 'selectedStyle', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['items']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferySortable, self).__init__(**args)
