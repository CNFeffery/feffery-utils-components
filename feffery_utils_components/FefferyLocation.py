# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyLocation(Component):
    """A FefferyLocation component.


Keyword arguments:

- id (string; optional):
    组件id.

- hash (string; optional):
    监听最新的hash信息.

- host (string; optional):
    监听最新的host信息.

- hostname (string; optional):
    监听最新的hostname信息.

- href (string; optional):
    监听最新的href信息.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- pathname (string; optional):
    监听最新的pathname信息.

- port (string; optional):
    监听最新的port信息.

- protocol (string; optional):
    监听最新的protocol信息.

- search (string; optional):
    监听最新的search信息.

- trigger (a value equal to: 'load', 'pushstate', 'popstate'; optional):
    监听最近一次地址更新行为触发类型，'load'表示页面重载行为，'pushstate'表示动态更新行为，'popstate'表示返回上一步地址."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyLocation'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, href=Component.UNDEFINED, pathname=Component.UNDEFINED, search=Component.UNDEFINED, hash=Component.UNDEFINED, host=Component.UNDEFINED, hostname=Component.UNDEFINED, port=Component.UNDEFINED, protocol=Component.UNDEFINED, trigger=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'hash', 'host', 'hostname', 'href', 'loading_state', 'pathname', 'port', 'protocol', 'search', 'trigger']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'hash', 'host', 'hostname', 'href', 'loading_state', 'pathname', 'port', 'protocol', 'search', 'trigger']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyLocation, self).__init__(**args)
