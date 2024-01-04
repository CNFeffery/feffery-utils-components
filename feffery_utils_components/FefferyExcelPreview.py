# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyExcelPreview(Component):
    """A FefferyExcelPreview component.


Keyword arguments:

- id (string; optional):
    组件id.

- className (string; optional):
    css类名.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- minColLength (number; optional):
    至少渲染的列数，当设置为0时会自动根据数据列数进行渲染.

- src (string; required):
    必填，设置目标excel文件资源地址.

- style (dict; optional):
    css样式."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyExcelPreview'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, src=Component.REQUIRED, minColLength=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'loading_state', 'minColLength', 'src', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'loading_state', 'minColLength', 'src', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['src']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FefferyExcelPreview, self).__init__(**args)
