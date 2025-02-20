# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyImageGallery(Component):
    """A FefferyImageGallery component.
相册组件FefferyImageGallery

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string; optional):
    当前组件css类名.

- images (list; optional):
    必填，用于定义相册内部各图片相关信息数组.

- infinite (boolean; default True):
    是否启用无限轮播  默认值：`True`.

- lazyLoad (boolean; default False):
    是否为图片启用懒加载功能  默认值：`False`.

- showNav (boolean; default True):
    是否展示导航按钮  默认值：`True`.

- showThumbnails (boolean; default True):
    是否展示缩略图列表  默认值：`True`.

- thumbnailPosition (a value equal to: 'top', 'right', 'bottom', 'left'; default 'bottom'):
    设置缩略图方位，可选项有`'top'`、`'right'`、`'bottom'`、`'left'`  默认值：`'bottom'`.

- showFullscreenButton (boolean; default True):
    是否展示全屏功能按钮  默认值：`True`.

- useBrowserFullscreen (boolean; default True):
    是否使用原生全屏化功能  默认值：`True`.

- showPlayButton (boolean; default True):
    是否展示播放功能按钮  默认值：`True`.

- showBullets (boolean; default False):
    是否展示快捷跳转指示器  默认值：`False`.

- showIndex (boolean; default False):
    是否展示图片序号信息  默认值：`False`.

- autoPlay (boolean; default False):
    是否启用自动播放  默认值：`False`.

- slideDuration (number; default 450):
    设置图片轮播动画的持续时长，单位：毫秒  默认值：`450`.

- slideInterval (number; default 3000):
    设置图片轮播动画的间隔时长，单位：毫秒  默认值：`3000`.

- startIndex (number; default 0):
    设置初始化图片下标，从0开始  默认值：`0`.

- isFullscreen (boolean; default False):
    监听当前相册是否处于全屏化状态  默认值：`False`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyImageGallery'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[str] = None,
        images: typing.Optional[typing.Sequence] = None,
        infinite: typing.Optional[bool] = None,
        lazyLoad: typing.Optional[bool] = None,
        showNav: typing.Optional[bool] = None,
        showThumbnails: typing.Optional[bool] = None,
        thumbnailPosition: typing.Optional[Literal["top", "right", "bottom", "left"]] = None,
        showFullscreenButton: typing.Optional[bool] = None,
        useBrowserFullscreen: typing.Optional[bool] = None,
        showPlayButton: typing.Optional[bool] = None,
        showBullets: typing.Optional[bool] = None,
        showIndex: typing.Optional[bool] = None,
        autoPlay: typing.Optional[bool] = None,
        slideDuration: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        slideInterval: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        startIndex: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        isFullscreen: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'images', 'infinite', 'lazyLoad', 'showNav', 'showThumbnails', 'thumbnailPosition', 'showFullscreenButton', 'useBrowserFullscreen', 'showPlayButton', 'showBullets', 'showIndex', 'autoPlay', 'slideDuration', 'slideInterval', 'startIndex', 'isFullscreen']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'images', 'infinite', 'lazyLoad', 'showNav', 'showThumbnails', 'thumbnailPosition', 'showFullscreenButton', 'useBrowserFullscreen', 'showPlayButton', 'showBullets', 'showIndex', 'autoPlay', 'slideDuration', 'slideInterval', 'startIndex', 'isFullscreen']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyImageGallery, self).__init__(**args)
