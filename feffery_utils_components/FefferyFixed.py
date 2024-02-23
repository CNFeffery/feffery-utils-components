# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyFixed(Component):
    """A FefferyFixed component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    组件子元素.

- id (string; optional):
    组件id.

- className (string | dict; optional):
    css类名.

- followImageContainerPosition (list of numbers; optional):
    以目标图片左上角为原点下，当前容器的左上角比例坐标，格式：(x_ratio, y_ratio).

- followImageContainerSize (list of numbers; optional):
    当前容器宽度、高度分别占目标图片对应宽度、高度的比例，格式：(width_ratio, height_ratio).

- followImageHeight (number; optional):
    跟随目标图片原始像素高度.

- followImageWidth (number; optional):
    跟随目标图片原始像素宽度.

- key (string; optional):
    强制刷新用.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- mode (a value equal to: 'follow-image'; required):
    必填，用于设置固定布局模式，可选的有'follow-image'（跟随object-fit为contain的全屏图片）.

- style (dict; optional):
    自定义css字典."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyFixed'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, mode=Component.REQUIRED, followImageWidth=Component.UNDEFINED, followImageHeight=Component.UNDEFINED, followImageContainerPosition=Component.UNDEFINED, followImageContainerSize=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'followImageContainerPosition', 'followImageContainerSize', 'followImageHeight', 'followImageWidth', 'key', 'loading_state', 'mode', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'followImageContainerPosition', 'followImageContainerSize', 'followImageHeight', 'followImageWidth', 'key', 'loading_state', 'mode', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['mode']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyFixed, self).__init__(children=children, **args)
