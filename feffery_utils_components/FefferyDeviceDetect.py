# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class FefferyDeviceDetect(Component):
    """A FefferyDeviceDetect component.
设备信息检测组件FefferyDeviceDetect

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- deviceInfo (dict; optional):
    监听当前访问设备的全部信息.

    `deviceInfo` is a dict with keys:

    - isMobile (boolean; optional):
        检测是否为手机、平板等移动设备.

    - isAndroid (boolean; optional):
        检测是否为安卓系统.

    - isIOS (boolean; optional):
        检测是否为ios系统.

    - isChrome (boolean; optional):
        检测是否为Chrome浏览器.

    - isFirefox (boolean; optional):
        检测是否为Firefox浏览器.

    - isSafari (boolean; optional):
        检测是否为Safari浏览器.

    - isIE (boolean; optional):
        检测是否为IE浏览器.

    - isEdge (boolean; optional):
        检测是否为Edge浏览器.

    - osVersion (string; optional):
        检测系统版本.

    - osName (string; optional):
        检测系统名称.

    - browserVersion (string; optional):
        检测浏览器缩略版本.

    - fullBrowserVersion (string; optional):
        检测完整的浏览器版本.

    - browserName (string; optional):
        检测浏览器名称.

    - ua (string; optional):
        检测`User-Agent`信息.

    - deviceType (string; optional):
        检测设备类型."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDeviceDetect'
    DeviceInfo = TypedDict(
        "DeviceInfo",
            {
            "isMobile": NotRequired[bool],
            "isAndroid": NotRequired[bool],
            "isIOS": NotRequired[bool],
            "isChrome": NotRequired[bool],
            "isFirefox": NotRequired[bool],
            "isSafari": NotRequired[bool],
            "isIE": NotRequired[bool],
            "isEdge": NotRequired[bool],
            "osVersion": NotRequired[str],
            "osName": NotRequired[str],
            "browserVersion": NotRequired[str],
            "fullBrowserVersion": NotRequired[str],
            "browserName": NotRequired[str],
            "ua": NotRequired[str],
            "deviceType": NotRequired[str]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        deviceInfo: typing.Optional["DeviceInfo"] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'deviceInfo']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'deviceInfo']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDeviceDetect, self).__init__(**args)

setattr(FefferyDeviceDetect, "__init__", _explicitize_args(FefferyDeviceDetect.__init__))
