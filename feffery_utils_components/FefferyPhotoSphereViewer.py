# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyPhotoSphereViewer(Component):
    """A FefferyPhotoSphereViewer component.


Keyword arguments:

- id (string; optional):
    组件id.

- caption (string; optional):
    导航栏标题内容，支持HTML字符串，仅当navbar中包含'caption'时有效.

- containerClass (string; optional):
    设置查看器所在容器css类名.

- fisheye (boolean; default False):
    是否开启鱼眼模式  默认：False.

- height (string; optional):
    设置查看器高度，同css中的height属性.

- key (string; optional):
    辅助刷新用唯一标识key值.

- littlePlanet (boolean; default False):
    是否开启小星球模式  默认：False.

- loadingImg (string; optional):
    自定义载入阶段过场图片地址.

- loadingTxt (string; optional):
    自定义载入阶段文字提示内容.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- mousemove (boolean; default True):
    是否允许鼠标拖拽平移  默认：True.

- mousewheel (boolean; default True):
    是否允许鼠标滚轮缩放  默认：True.

- moveSpeed (number; default 1):
    设置鼠标平移速度  默认：1.

- navbar (list of a value equal to: 'zoom', 'move', 'download', 'caption', 'fullscreen's; default ['caption']):
    配置导航栏中需要显示的功能项及顺序
    可选的有'zoom'、'move'、'download'、'caption'、'fullscreen'
    默认：['caption'].

- src (string; optional):
    设置全景图片资源地址.

- width (string; optional):
    设置查看器宽度，同css中的width属性.

- zoomSpeed (number; default 1):
    设置鼠标滚轮缩放速度  默认：1."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyPhotoSphereViewer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, src=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, littlePlanet=Component.UNDEFINED, containerClass=Component.UNDEFINED, navbar=Component.UNDEFINED, caption=Component.UNDEFINED, loadingImg=Component.UNDEFINED, loadingTxt=Component.UNDEFINED, mousewheel=Component.UNDEFINED, mousemove=Component.UNDEFINED, moveSpeed=Component.UNDEFINED, zoomSpeed=Component.UNDEFINED, fisheye=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'caption', 'containerClass', 'fisheye', 'height', 'key', 'littlePlanet', 'loadingImg', 'loadingTxt', 'loading_state', 'mousemove', 'mousewheel', 'moveSpeed', 'navbar', 'src', 'width', 'zoomSpeed']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'caption', 'containerClass', 'fisheye', 'height', 'key', 'littlePlanet', 'loadingImg', 'loadingTxt', 'loading_state', 'mousemove', 'mousewheel', 'moveSpeed', 'navbar', 'src', 'width', 'zoomSpeed']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyPhotoSphereViewer, self).__init__(**args)
