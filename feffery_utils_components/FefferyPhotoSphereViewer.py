# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyPhotoSphereViewer(Component):
    """A FefferyPhotoSphereViewer component.


Keyword arguments:

- id (string; optional):
    组件id.

- key (string; optional):
    辅助刷新用唯一标识key值.

- src (string; optional):
    设置全景图片资源地址.

- width (string; optional):
    设置查看器宽度，同css中的width属性.

- height (string; optional):
    设置查看器高度，同css中的height属性.

- littlePlanet (boolean; default False):
    是否开启小星球模式  默认：False.

- containerClass (string; optional):
    设置查看器所在容器css类名.

- navbar (list of a value equal to: 'zoom', 'move', 'download', 'caption', 'fullscreen', 'autorotate's | boolean; default ['caption']):
    配置导航栏中需要显示的功能项及顺序，设置为`False`时将隐藏导航栏
    可选的有`'zoom'`、`'move'`、`'download'`、`'caption'`、`'fullscreen'`、`'autorotate'`
    默认值：`['caption']`.

- caption (string; optional):
    导航栏标题内容，支持HTML字符串，仅当navbar中包含'caption'时有效.

- downloadUrl (string; optional):
    手动设置下载目标文件地址.

- loadingImg (string; optional):
    自定义载入阶段过场图片地址.

- loadingTxt (string; optional):
    自定义载入阶段文字提示内容.

- mousewheel (boolean; default True):
    是否允许鼠标滚轮缩放  默认：True.

- mousemove (boolean; default True):
    是否允许鼠标拖拽平移  默认：True.

- moveSpeed (number; default 1):
    设置鼠标平移速度  默认：1.

- zoomSpeed (number; default 1):
    设置鼠标滚轮缩放速度  默认：1.

- fisheye (boolean; default False):
    是否开启鱼眼模式  默认：False.

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
        `Autorotate`模式下，自动旋转速度  默认值：`2rpm`.

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
    _type = 'FefferyPhotoSphereViewer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, src=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, littlePlanet=Component.UNDEFINED, containerClass=Component.UNDEFINED, navbar=Component.UNDEFINED, caption=Component.UNDEFINED, downloadUrl=Component.UNDEFINED, loadingImg=Component.UNDEFINED, loadingTxt=Component.UNDEFINED, mousewheel=Component.UNDEFINED, mousemove=Component.UNDEFINED, moveSpeed=Component.UNDEFINED, zoomSpeed=Component.UNDEFINED, fisheye=Component.UNDEFINED, lang=Component.UNDEFINED, hideNavbarButton=Component.UNDEFINED, plugins=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'src', 'width', 'height', 'littlePlanet', 'containerClass', 'navbar', 'caption', 'downloadUrl', 'loadingImg', 'loadingTxt', 'mousewheel', 'mousemove', 'moveSpeed', 'zoomSpeed', 'fisheye', 'lang', 'hideNavbarButton', 'plugins', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'src', 'width', 'height', 'littlePlanet', 'containerClass', 'navbar', 'caption', 'downloadUrl', 'loadingImg', 'loadingTxt', 'mousewheel', 'mousemove', 'moveSpeed', 'zoomSpeed', 'fisheye', 'lang', 'hideNavbarButton', 'plugins', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyPhotoSphereViewer, self).__init__(**args)
