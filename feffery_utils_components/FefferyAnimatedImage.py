# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyAnimatedImage(Component):
    """A FefferyAnimatedImage component.


Keyword arguments:

- id (string; optional):
    组件id.

- alt (string; optional):
    动图alt信息.

- className (string; optional):
    css类名.

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

- play (boolean; default False):
    初始化是否自动播放动图  默认：False.

- src (string; required):
    必填，定义动图资源地址.

- style (dict; optional):
    自定义css字典."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyAnimatedImage'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, src=Component.REQUIRED, alt=Component.UNDEFINED, play=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'alt', 'className', 'key', 'loading_state', 'play', 'src', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'alt', 'className', 'key', 'loading_state', 'play', 'src', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['src']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyAnimatedImage, self).__init__(**args)
