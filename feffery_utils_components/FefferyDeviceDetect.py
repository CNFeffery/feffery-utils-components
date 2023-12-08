# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDeviceDetect(Component):
    """A FefferyDeviceDetect component.


Keyword arguments:

- id (string; optional):
    组件id.

- deviceInfo (dict; optional):
    监听当前访问设备的全部信息.

    `deviceInfo` is a dict with keys:

    - browserName (string; optional)

    - browserVersion (string; optional)

    - deviceType (string; optional)

    - fullBrowserVersion (string; optional)

    - isAndroid (boolean; optional)

    - isChrome (boolean; optional)

    - isEdge (boolean; optional)

    - isFirefox (boolean; optional)

    - isIE (boolean; optional)

    - isIOS (boolean; optional)

    - isMobile (boolean; optional)

    - isSafari (boolean; optional)

    - osName (string; optional)

    - osVersion (string; optional)

    - ua (string; optional)

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
    _type = 'FefferyDeviceDetect'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, deviceInfo=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'deviceInfo', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'deviceInfo', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDeviceDetect, self).__init__(**args)
