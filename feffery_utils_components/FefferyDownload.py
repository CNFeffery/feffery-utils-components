# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDownload(Component):
    """A FefferyDownload component.
文件下载组件FefferyDownload

Keyword arguments:

- id (string; optional):
    组件id.

- file (dict; optional):
    设置新的下载任务对应文件信息，每次触发下载后都会重置为空置.

    `file` is a dict with keys:

    - url (string; required):
        必填，文件资源地址.

    - name (string; optional):
        自定义文件下载后的文件名，可省略后缀名.

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
    _type = 'FefferyDownload'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, file=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'file', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'file', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDownload, self).__init__(**args)
