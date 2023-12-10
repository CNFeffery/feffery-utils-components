# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyLocalStorage(Component):
    """A FefferyLocalStorage component.


Keyword arguments:

- id (string; required):
    组件id.

- data (boolean | number | string | dict | list; optional):
    设置或监听当前id对应的localStorage数据.

- initialSync (boolean; default False):
    设置初始化时是否从localStorage中尝试读取id对应的值并更新到data中  默认：False.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyLocalStorage'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, data=Component.UNDEFINED, initialSync=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'initialSync', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'initialSync', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyLocalStorage, self).__init__(**args)
