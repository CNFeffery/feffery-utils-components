# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyLocation(Component):
    """A FefferyLocation component.
地址监听组件FefferyLocation

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- href (string; optional):
    监听最新的`href`信息.

- pathname (string; optional):
    监听最新的`pathname`信息.

- search (string; optional):
    监听最新的`search`信息.

- hash (string; optional):
    监听最新的`hash`信息.

- host (string; optional):
    监听最新的`host`信息.

- hostname (string; optional):
    监听最新的`hostname`信息.

- port (string; optional):
    监听最新的`port`信息.

- protocol (string; optional):
    监听最新的`protocol`信息.

- trigger (a value equal to: 'load', 'pushstate', 'popstate'; optional):
    监听最近一次地址更新行为触发类型，`'load'`表示页面重载行为，`'pushstate'`表示动态更新行为，`'popstate'`表示返回上一步地址.

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
    _type = 'FefferyLocation'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, href=Component.UNDEFINED, pathname=Component.UNDEFINED, search=Component.UNDEFINED, hash=Component.UNDEFINED, host=Component.UNDEFINED, hostname=Component.UNDEFINED, port=Component.UNDEFINED, protocol=Component.UNDEFINED, trigger=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'href', 'pathname', 'search', 'hash', 'host', 'hostname', 'port', 'protocol', 'trigger', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'href', 'pathname', 'search', 'hash', 'host', 'hostname', 'port', 'protocol', 'trigger', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyLocation, self).__init__(**args)
