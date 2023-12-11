# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyImageGallery(Component):
    """A FefferyImageGallery component.


Keyword arguments:

- id (string; optional):
    组件id.

- autoPlay (boolean; default False):
    是否启用自动播放  默认：False.

- className (string; optional):
    css类名.

- images (list; optional):
    必填，用于定义相册内部各图片相关信息数组.

- infinite (boolean; default True):
    是否启用无限轮播  默认：True.

- isFullscreen (boolean; default False):
    用于监听当前相册是否处于全屏化状态  默认：False.

- lazyLoad (boolean; default False):
    是否为图片启用懒加载功能  默认：False.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- showBullets (boolean; default False):
    是否展示快捷跳转指示器  默认：False.

- showFullscreenButton (boolean; default True):
    是否展示全屏功能按钮  默认：True.

- showIndex (boolean; default False):
    是否展示图片序号信息  默认：False.

- showNav (boolean; default True):
    是否展示导航按钮  默认：True.

- showPlayButton (boolean; default True):
    是否展示播放功能按钮  默认：True.

- showThumbnails (boolean; default True):
    是否展示缩略图列表  默认：True.

- slideDuration (number; default 450):
    设置图片轮播动画的持续时长，单位：毫秒  默认：450.

- slideInterval (number; default 3000):
    设置图片轮播动画的间隔时长，单位：毫秒  默认：3000.

- startIndex (number; default 0):
    设置初始化图片下标，从0开始  默认：0.

- style (dict; optional):
    css样式.

- thumbnailPosition (a value equal to: 'top', 'right', 'bottom', 'left'; default 'bottom'):
    设置缩略图方位，可选的有'top'、'right'、'bottom'、'left'  默认：'bottom'.

- useBrowserFullscreen (boolean; default True):
    是否使用原生全屏化功能  默认：True."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyImageGallery'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, images=Component.UNDEFINED, infinite=Component.UNDEFINED, lazyLoad=Component.UNDEFINED, showNav=Component.UNDEFINED, showThumbnails=Component.UNDEFINED, thumbnailPosition=Component.UNDEFINED, showFullscreenButton=Component.UNDEFINED, useBrowserFullscreen=Component.UNDEFINED, showPlayButton=Component.UNDEFINED, showBullets=Component.UNDEFINED, showIndex=Component.UNDEFINED, autoPlay=Component.UNDEFINED, slideDuration=Component.UNDEFINED, slideInterval=Component.UNDEFINED, startIndex=Component.UNDEFINED, isFullscreen=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autoPlay', 'className', 'images', 'infinite', 'isFullscreen', 'lazyLoad', 'loading_state', 'showBullets', 'showFullscreenButton', 'showIndex', 'showNav', 'showPlayButton', 'showThumbnails', 'slideDuration', 'slideInterval', 'startIndex', 'style', 'thumbnailPosition', 'useBrowserFullscreen']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autoPlay', 'className', 'images', 'infinite', 'isFullscreen', 'lazyLoad', 'loading_state', 'showBullets', 'showFullscreenButton', 'showIndex', 'showNav', 'showPlayButton', 'showThumbnails', 'slideDuration', 'slideInterval', 'startIndex', 'style', 'thumbnailPosition', 'useBrowserFullscreen']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyImageGallery, self).__init__(**args)
