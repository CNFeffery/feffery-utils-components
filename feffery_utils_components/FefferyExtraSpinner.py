# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyExtraSpinner(Component):
    """A FefferyExtraSpinner component.


Keyword arguments:

- id (string; optional):
    部件id.

- backColor (string; default '#1890ff'):
    设置背景色.

- className (string; optional)

- color (string; default '#1890ff'):
    设置颜色.

- frontColor (string; default '#def6ff'):
    设置前景色.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- size (number; optional):
    设置尺寸.

- sizeUnit (string; default 'px'):
    设置尺寸值单位，默认为'px'.

- style (dict; optional)

- type (a value equal to: "ball", "swap", "bars", "grid", "wave", "push", "firework", "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse", "swish", "sequence", "impulse", "cube", "magic", "flag", "fill", "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop", "flapper", "jellyfish", "trace", "classic", "whisper", "metro"; default 'ball'):
    加载动画类型."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyExtraSpinner'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, type=Component.UNDEFINED, size=Component.UNDEFINED, sizeUnit=Component.UNDEFINED, color=Component.UNDEFINED, frontColor=Component.UNDEFINED, backColor=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'backColor', 'className', 'color', 'frontColor', 'loading_state', 'size', 'sizeUnit', 'style', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'backColor', 'className', 'color', 'frontColor', 'loading_state', 'size', 'sizeUnit', 'style', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyExtraSpinner, self).__init__(**args)
