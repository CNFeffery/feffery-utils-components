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


class FefferyPhotoSphereViewer(Component):
    """A FefferyPhotoSphereViewer component.
全景图片查看器组件FefferyPhotoSphereViewer

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- src (string; optional):
    全景图片资源地址.

- width (string; optional):
    设置查看器宽度，同`css`中的`width`属性.

- height (string; optional):
    设置查看器高度，同`css`中的`height`属性.

- littlePlanet (boolean; default False):
    是否开启小星球模式  默认值：`False`.

- containerClass (string; optional):
    设置查看器所在容器`css`类名.

- navbar (list of a value equal to: 'zoom', 'move', 'download', 'caption', 'fullscreen', 'autorotate's | boolean; default ['caption']):
    配置导航栏中需要显示的功能项及顺序，设置为`False`时将隐藏导航栏，可选项有`'zoom'`、`'move'`、`'download'`、`'caption'`、`'fullscreen'`、`'autorotate'`
    默认值：`['caption']`.

- caption (string; optional):
    导航栏标题内容，支持`HTML`字符串，仅当`navbar`中包含`'caption'`时有效.

- downloadUrl (string; optional):
    手动设置下载目标文件地址.

- loadingImg (string; optional):
    自定义载入阶段过场图片地址.

- loadingTxt (string; optional):
    自定义载入阶段文字提示内容.

- mousewheel (boolean; default True):
    是否允许鼠标滚轮缩放  默认值：`True`.

- mousemove (boolean; default True):
    是否允许鼠标拖拽平移  默认值：`True`.

- moveSpeed (number; default 1):
    设置鼠标平移速度  默认值：`1`.

- zoomSpeed (number; default 1):
    设置鼠标滚轮缩放速度  默认值：`1`.

- fisheye (boolean; default False):
    是否开启鱼眼模式  默认值：`False`.

- lang (dict; optional):
    为相关功能控件或场景设置鼠标悬停提示信息文案.

    `lang` is a dict with keys:

    - littlePlanetButton (string; optional):
        小星球模式.

    - zoomOut (string; optional):
        缩小操作.

    - zoomIn (string; optional):
        放大操作.

    - moveLeft (string; optional):
        左移操作.

    - moveRight (string; optional):
        右移操作.

    - moveUp (string; optional):
        上移操作.

    - moveDown (string; optional):
        下移操作.

    - download (string; optional):
        下载操作.

    - fullscreen (string; optional):
        全屏操作.

    - loadError (string; optional):
        资源加载失败.

    - autorotate (string; optional):
        自动旋转调节.

- hideNavbarButton (boolean; default False):
    是否渲染底部导航栏隐藏按钮  默认值：`False`.

- plugins (list of dicts; optional):
    用于配置额外插件功能.

    `plugins` is a list of dicts with keys:

    - type (a value equal to: 'Autorotate'; required):
        必填，插件类型，可选项有`'Autorotate'`.

    - autostartDelay (number; optional):
        `Autorotate`模式下，从用户无操作到恢复自动旋转的延时，单位：毫秒  默认值：`2000`.

    - autostartOnIdle (boolean; optional):
        `Autorotate`模式下，是否在用户无操作一段时间后恢复自动旋转  默认值：`True`.

    - autorotateSpeed (string; optional):
        `Autorotate`模式下，自动旋转速度  默认值：`2rpm`."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyPhotoSphereViewer'
    Lang = TypedDict(
        "Lang",
            {
            "littlePlanetButton": NotRequired[str],
            "zoomOut": NotRequired[str],
            "zoomIn": NotRequired[str],
            "moveLeft": NotRequired[str],
            "moveRight": NotRequired[str],
            "moveUp": NotRequired[str],
            "moveDown": NotRequired[str],
            "download": NotRequired[str],
            "fullscreen": NotRequired[str],
            "loadError": NotRequired[str],
            "autorotate": NotRequired[str]
        }
    )

    Plugins = TypedDict(
        "Plugins",
            {
            "type": Literal["Autorotate"],
            "autostartDelay": NotRequired[NumberType],
            "autostartOnIdle": NotRequired[bool],
            "autorotateSpeed": NotRequired[str]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        src: typing.Optional[str] = None,
        width: typing.Optional[str] = None,
        height: typing.Optional[str] = None,
        littlePlanet: typing.Optional[bool] = None,
        containerClass: typing.Optional[str] = None,
        navbar: typing.Optional[typing.Union[typing.Sequence[Literal["zoom", "move", "download", "caption", "fullscreen", "autorotate"]], bool]] = None,
        caption: typing.Optional[str] = None,
        downloadUrl: typing.Optional[str] = None,
        loadingImg: typing.Optional[str] = None,
        loadingTxt: typing.Optional[str] = None,
        mousewheel: typing.Optional[bool] = None,
        mousemove: typing.Optional[bool] = None,
        moveSpeed: typing.Optional[NumberType] = None,
        zoomSpeed: typing.Optional[NumberType] = None,
        fisheye: typing.Optional[bool] = None,
        lang: typing.Optional["Lang"] = None,
        hideNavbarButton: typing.Optional[bool] = None,
        plugins: typing.Optional[typing.Sequence["Plugins"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'src', 'width', 'height', 'littlePlanet', 'containerClass', 'navbar', 'caption', 'downloadUrl', 'loadingImg', 'loadingTxt', 'mousewheel', 'mousemove', 'moveSpeed', 'zoomSpeed', 'fisheye', 'lang', 'hideNavbarButton', 'plugins']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'src', 'width', 'height', 'littlePlanet', 'containerClass', 'navbar', 'caption', 'downloadUrl', 'loadingImg', 'loadingTxt', 'mousewheel', 'mousemove', 'moveSpeed', 'zoomSpeed', 'fisheye', 'lang', 'hideNavbarButton', 'plugins']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyPhotoSphereViewer, self).__init__(**args)

setattr(FefferyPhotoSphereViewer, "__init__", _explicitize_args(FefferyPhotoSphereViewer.__init__))
