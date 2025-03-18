# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyImageCropper(Component):
    """A FefferyImageCropper component.
图片裁剪组件FefferyImageCropper

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string | dict; optional):
    当前组件css类名.

- croppedImageData (string; optional):
    裁剪后的图片数据，`base64`格式.

- src (string; optional):
    裁切目标图片地址.

- alt (string; default 'picture'):
    图片占位名称  默认值：`'picture'`.

- crossOrigin (string; optional):
    图片跨域属性.

- viewMode (a value equal to: 0, 1, 2, 3; default 0):
    设置裁剪框的视图模式。
    如果将viewMode设置为0，裁剪框可以超出画布的范围，而设置为1、2或3的值将限制裁剪框的大小与画布一致。
    viewMode为2或3还会额外限制画布适应容器的大小，当画布和容器的比例相同时，2和3没有区别。  0：无限制。
    1：限制裁剪框不超过画布的大小。  2：限制最小画布尺寸适应容器。如果画布和容器的比例不同，最小画布将在一个维度上被额外空间包围。
    3：限制最小画布尺寸填满容器。如果画布和容器的比例不同，容器将无法在一个维度上容纳整个画布。  默认值：`0`.

- dragMode (a value equal to: 'crop', 'move', 'none'; default 'crop'):
    设置裁剪器的拖动模式。  'crop'：创建一个新的裁剪框。  'move'：移动画布。  'none'：无操作。
    默认值：`'crop'`.

- initialAspectRatio (number; optional):
    设置裁剪框的初始宽高比，默认与画布宽高比相同，仅在`aspectRatio`未设置时有效.

- aspectRatio (number; optional):
    设置裁剪框的固定宽高比，默认情况下，裁剪框具有自由比例.

- data (dict; optional):
    设置初始化时要传给setData方法的裁剪的数据，仅当autoCrop选项设置为True时才有效.

- preview (string | list of strings; default ''):
    设置预览的容器（选择器）。  注意：最大宽度是预览容器的初始宽度。  最大高度是预览容器的初始高度。
    如果您设置了宽高比选项，请务必为预览容器设置相同的宽高比。
    如果预览无法正确显示，请将预览容器设置为overflow:hidden样式。.

- responsive (boolean; default True):
    调整窗口大小时是否重新渲染裁剪器  默认值：`True`.

- restore (boolean; default True):
    调整窗口大小后是否恢复裁剪区域  默认值：`True`.

- checkCrossOrigin (boolean; default True):
    检查当前图片是否为跨域图片。
    如果是，则会在克隆的图片元素中添加一个crossOrigin属性，并在src属性中添加一个时间戳参数，以重新加载源图片，以避免浏览器缓存错误。
    向图片元素添加 crossOrigin 属性将停止向图片 URL 添加时间戳并停止重新加载图片。
    但是读取图片数据以进行方向检查的请求（XMLHttpRequest）将需要时间戳来破坏缓存以避免浏览器缓存错误。
    您可以将checkOrientation选项设置为False以取消此请求。
    如果图片的crossOrigin属性值为'use-credentials'，那么当通过XMLHttpRequest读取图片数据时，withCredentials属性将设置为True。
    默认值：`True`.

- checkOrientation (boolean; default True):
    检查当前图片的Exif方向信息。请注意，只有JPEG图片可能包含Exif方向信息。
    具体来说，读取旋转或翻转图片的方向值，然后用1（默认值）覆盖方向值，以避免iOS设备上的某些问题。
    需要同时将可旋转和可缩放选项设置为 True。  注意：不要总是相信这一点，因为某些 JPG
    图片可能具有不正确（非标准）的方向值，需要类型化数组支持（IE 10+）。  默认值：`True`.

- modal (boolean; default True):
    是否在图片上方和裁剪框下方显示黑色模态  默认值：`True`.

- guides (boolean; default True):
    是否显示裁剪框上方的虚线  默认值：`True`.

- center (boolean; default True):
    是否在裁剪框上方显示中心指示器  默认值：`True`.

- highlight (boolean; default True):
    是否在裁剪框上方显示白色模态（突出显示裁剪框）  默认值：`True`.

- background (boolean; default True):
    是否显示容器的网格背景  默认值：`True`.

- autoCrop (boolean; default True):
    是否在初始化时自动裁剪图片  默认值：`True`.

- autoCropArea (number; default 0.8):
    设置自动裁剪区域大小，为0到1之间的值  默认值：`0.8`.

- movable (boolean; default True):
    是否可以移动图片  默认值：`True`.

- rotatable (boolean; default True):
    是否可以旋转图片  默认值：`True`.

- scalable (boolean; default True):
    是否可以缩放图片（居中缩放）  默认值：`True`.

- zoomable (boolean; default True):
    是否可以缩放图片（相对于左上角）  默认值：`True`.

- zoomOnTouch (boolean; default True):
    是否可以通过拖动触摸来缩放图片  默认值：`True`.

- zoomOnWheel (boolean; default True):
    是否可以通过鼠标滚轮缩放图片  默认值：`True`.

- wheelZoomRatio (number; default 0.1):
    设置通过鼠标滚轮缩放图片时的缩放比例  默认值：`0.1`.

- cropBoxMovable (boolean; default True):
    是否可以通过拖动来移动裁剪框  默认值：`True`.

- cropBoxResizable (boolean; default True):
    是否可以通过拖动来调整裁剪框的大小  默认值：`True`.

- toggleDragModeOnDblclick (boolean; default True):
    单击裁剪器两次时，是否可以在'crop'和'move'之间切换拖动模式，需要支持dbclick事件，需要默认为True.

- minContainerWidth (number; default 200):
    设置容器的最小像素宽度  默认值：`200`.

- minContainerHeight (number; default 100):
    设置容器的最小像素高度  默认值：`100`.

- minCanvasWidth (number; default 0):
    设置画布的最小宽度\  默认值：`0`.

- minCanvasHeight (number; default 0):
    设置画布的最小高度  默认值：`0`.

- minCropBoxWidth (number; default 0):
    设置裁剪框的最小宽度（这个尺寸是相对于页面的，而不是图片的）  默认值：`0`.

- minCropBoxHeight (number; default 0):
    设置裁剪框的最小高度（这个尺寸是相对于页面的，而不是图片的）  默认值：`0`.

- reset (boolean; default False):
    将图片和裁剪框重置为初始状态，每次设置为`True`后执行完相应操作后会自动置为`False`.

- clear (boolean; default False):
    清除裁剪框，每次设置为`True`后执行完相应操作后会自动置为`False`.

- replace (dict; default { isReplace: False, hasSameSize: False }):
    替换图片的`src`并重新构建裁剪器，每次`isReplace`设置为`True`后执行完相应操作后会自动置为`False`.

    `replace` is a dict with keys:

    - isReplace (boolean; optional):
        是否启用.

    - url (string; optional):
        新的图片url.

    - hasSameSize (boolean; optional):
        如果新图片的大小与旧图片相同，则它不会重建裁剪器，而只会更新所有相关图片的url.

- enable (boolean; default False):
    启用裁剪器，每次设置为`True`后执行完相应操作后会自动置为`False`.

- disable (boolean; default False):
    禁用裁剪器，每次设置为`True`后执行完相应操作后会自动置为`False`.

- destroy (boolean; default False):
    销毁裁剪器并从图片中删除实例，每次设置为`True`后执行完相应操作后会自动置为`False`.

- move (dict; default { isMove: False }):
    使用相对偏移量移动画布，每次`isMove`设置为`True`后执行完相应操作后会自动置为`False`.

    `move` is a dict with keys:

    - isMove (boolean; optional):
        是否启用.

    - offsetX (number; optional):
        在水平方向上移动像素大小.

    - offsetY (number; optional):
        在垂直方向上移动像素大小，如果不存在，则其默认值为`offsetX`.

- moveTo (dict; default { isMoveTo: False }):
    将画布移动到绝对点，每次`isMoveTo`设置为`True`后执行完相应操作后会自动置为`False`.

    `moveTo` is a dict with keys:

    - isMoveTo (boolean; optional):
        是否启用.

    - x (number; optional):
        画布`left`的值.

    - y (number; optional):
        画布`top`的值，如果不存在，则其默认值为`x`.

- zoom (dict; default { isZoom: False }):
    使用相对比例缩放画布，每次`isZoom`设置为`True`后执行完相应操作后会自动置为`False`.

    `zoom` is a dict with keys:

    - isZoom (boolean; optional):
        是否启用.

    - ratio (number; optional):
        放大：需要一个正数（比率 > 0）；  缩小：需要负数（比率 < 0）.

- zoomTo (dict; default { isZoomTo: False }):
    将画布缩放到绝对比例，每次`isZoomTo`设置为`True`后执行完相应操作后会自动置为`False`.

    `zoomTo` is a dict with keys:

    - isZoomTo (boolean; optional):
        是否启用.

    - ratio (number; optional):
        需要一个正数（比率 > 0）.

    - pivot (dict; optional):
        用于缩放的中心点的坐标，基于裁剪器容器的左上角.

        `pivot` is a dict with keys:

        - x (number; optional)

        - y (number; optional)

- rotate (dict; default { isRotate: False }):
    将图片旋转到相对角度，每次`isRotate`设置为`True`后执行完相应操作后会自动置为`False`.

    `rotate` is a dict with keys:

    - isRotate (boolean; optional):
        是否启用.

    - degree (number; optional):
        向右旋转：需要正数（度数 > 0）；  向左旋转：需要负数（度数 < 0）.

- rotateTo (dict; default { isRotateTo: False }):
    将图片旋转到绝对角度，每次`isRotateTo`设置为`True`后执行完相应操作后会自动置为`False`.

    `rotateTo` is a dict with keys:

    - isRotateTo (boolean; optional):
        是否启用.

    - degree (number; optional):
        绝对角度的度数.

- scale (dict; default { isScale: False }):
    缩放图片，每次`isScale`设置为`True`后执行完相应操作后会自动置为`False`.

    `scale` is a dict with keys:

    - isScale (boolean; optional):
        是否启用.

    - scaleX (number; optional):
        要应用于图片横坐标的比例因子，当等于1时，图片保持不变.

    - scaleY (number; optional):
        要应用于图片纵坐标的比例因子，如果不存在，则其默认值为scaleX.

- scaleX (dict; default { isScaleX: False }):
    缩放图片的横坐标，每次`isScaleX`设置为`True`后执行完相应操作后会自动置为`False`.

    `scaleX` is a dict with keys:

    - isScaleX (boolean; optional):
        是否启用.

    - scaleX (number; optional):
        要应用于图片横坐标的比例因子，当等于1时，图片保持不变.

- scaleY (dict; default { isScaleY: False }):
    缩放图片的纵坐标，每次`isScaleY`设置为`True`后执行完相应操作后会自动置为`False`.

    `scaleY` is a dict with keys:

    - isScaleY (boolean; optional):
        是否启用.

    - scaleY (number; optional):
        要应用于图片纵坐标的比例因子，当等于1时，图片保持不变.

- outputData (dict; optional):
    输出的最终裁剪的区域位置和大小数据（基于原始图像的自然大小）.

    `outputData` is a dict with keys:

    - x (number; optional):
        裁剪区域的左侧偏移量.

    - y (number; optional):
        裁剪区域的顶部偏移量.

    - width (number; optional):
        裁剪区域的宽度.

    - height (number; optional):
        裁剪区域的高度.

    - rotate (number; optional):
        图片的旋转角度.

    - scaleX (number; optional):
        缩放后应用于图片横坐标的缩放因子.

    - scaleY (number; optional):
        缩放后应用于图片纵坐标的缩放因子.

- containerData (dict; optional):
    输出的容器大小数据.

    `containerData` is a dict with keys:

    - width (number; optional):
        容器的当前宽度.

    - height (number; optional):
        容器的当前高度.

- imageData (dict; optional):
    输出的图片数据.

    `imageData` is a dict with keys:

    - left (number; optional):
        图片的左侧偏移量.

    - top (number; optional):
        图片的顶部偏移量.

    - width (number; optional):
        图片的宽度.

    - height (number; optional):
        图片的高度.

    - naturalWidth (number; optional):
        图片的原始宽度.

    - naturalHeight (number; optional):
        图片的原始高度.

    - aspectRatio (number; optional):
        图片的纵横比.

    - rotate (number; optional):
        图片的旋转角度.

    - scaleX (number; optional):
        缩放后应用于图片横坐标的缩放因子.

    - scaleY (number; optional):
        缩放后应用于图片纵坐标的缩放因子.

- canvasData (dict; optional):
    输出的画布数据.

    `canvasData` is a dict with keys:

    - left (number; optional):
        画布的左侧偏移量.

    - top (number; optional):
        画布的顶部偏移量.

    - width (number; optional):
        画布的宽度.

    - height (number; optional):
        画布的高度.

    - naturalWidth (number; optional):
        画布的原始宽度（只读）.

    - naturalHeight (number; optional):
        画布的原始高度（只读）.

- cropBoxData (dict; optional):
    输出的裁剪框数据.

    `cropBoxData` is a dict with keys:

    - left (number; optional):
        裁剪框的左侧偏移量.

    - top (number; optional):
        裁剪框的顶部偏移量.

    - width (number; optional):
        裁剪框的宽度.

    - height (number; optional):
        裁剪框的高度."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyImageCropper'
    Replace = TypedDict(
        "Replace",
            {
            "isReplace": NotRequired[bool],
            "url": NotRequired[str],
            "hasSameSize": NotRequired[bool]
        }
    )

    Move = TypedDict(
        "Move",
            {
            "isMove": NotRequired[bool],
            "offsetX": NotRequired[typing.Union[int, float, numbers.Number]],
            "offsetY": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    MoveTo = TypedDict(
        "MoveTo",
            {
            "isMoveTo": NotRequired[bool],
            "x": NotRequired[typing.Union[int, float, numbers.Number]],
            "y": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    Zoom = TypedDict(
        "Zoom",
            {
            "isZoom": NotRequired[bool],
            "ratio": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    ZoomToPivot = TypedDict(
        "ZoomToPivot",
            {
            "x": NotRequired[typing.Union[int, float, numbers.Number]],
            "y": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    ZoomTo = TypedDict(
        "ZoomTo",
            {
            "isZoomTo": NotRequired[bool],
            "ratio": NotRequired[typing.Union[int, float, numbers.Number]],
            "pivot": NotRequired["ZoomToPivot"]
        }
    )

    Rotate = TypedDict(
        "Rotate",
            {
            "isRotate": NotRequired[bool],
            "degree": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    RotateTo = TypedDict(
        "RotateTo",
            {
            "isRotateTo": NotRequired[bool],
            "degree": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    Scale = TypedDict(
        "Scale",
            {
            "isScale": NotRequired[bool],
            "scaleX": NotRequired[typing.Union[int, float, numbers.Number]],
            "scaleY": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    ScaleX = TypedDict(
        "ScaleX",
            {
            "isScaleX": NotRequired[bool],
            "scaleX": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    ScaleY = TypedDict(
        "ScaleY",
            {
            "isScaleY": NotRequired[bool],
            "scaleY": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    OutputData = TypedDict(
        "OutputData",
            {
            "x": NotRequired[typing.Union[int, float, numbers.Number]],
            "y": NotRequired[typing.Union[int, float, numbers.Number]],
            "width": NotRequired[typing.Union[int, float, numbers.Number]],
            "height": NotRequired[typing.Union[int, float, numbers.Number]],
            "rotate": NotRequired[typing.Union[int, float, numbers.Number]],
            "scaleX": NotRequired[typing.Union[int, float, numbers.Number]],
            "scaleY": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    ContainerData = TypedDict(
        "ContainerData",
            {
            "width": NotRequired[typing.Union[int, float, numbers.Number]],
            "height": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    ImageData = TypedDict(
        "ImageData",
            {
            "left": NotRequired[typing.Union[int, float, numbers.Number]],
            "top": NotRequired[typing.Union[int, float, numbers.Number]],
            "width": NotRequired[typing.Union[int, float, numbers.Number]],
            "height": NotRequired[typing.Union[int, float, numbers.Number]],
            "naturalWidth": NotRequired[typing.Union[int, float, numbers.Number]],
            "naturalHeight": NotRequired[typing.Union[int, float, numbers.Number]],
            "aspectRatio": NotRequired[typing.Union[int, float, numbers.Number]],
            "rotate": NotRequired[typing.Union[int, float, numbers.Number]],
            "scaleX": NotRequired[typing.Union[int, float, numbers.Number]],
            "scaleY": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    CanvasData = TypedDict(
        "CanvasData",
            {
            "left": NotRequired[typing.Union[int, float, numbers.Number]],
            "top": NotRequired[typing.Union[int, float, numbers.Number]],
            "width": NotRequired[typing.Union[int, float, numbers.Number]],
            "height": NotRequired[typing.Union[int, float, numbers.Number]],
            "naturalWidth": NotRequired[typing.Union[int, float, numbers.Number]],
            "naturalHeight": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    CropBoxData = TypedDict(
        "CropBoxData",
            {
            "left": NotRequired[typing.Union[int, float, numbers.Number]],
            "top": NotRequired[typing.Union[int, float, numbers.Number]],
            "width": NotRequired[typing.Union[int, float, numbers.Number]],
            "height": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        croppedImageData: typing.Optional[str] = None,
        src: typing.Optional[str] = None,
        alt: typing.Optional[str] = None,
        crossOrigin: typing.Optional[str] = None,
        viewMode: typing.Optional[Literal[0, 1, 2, 3]] = None,
        dragMode: typing.Optional[Literal["crop", "move", "none"]] = None,
        initialAspectRatio: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        aspectRatio: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        data: typing.Optional[dict] = None,
        preview: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        responsive: typing.Optional[bool] = None,
        restore: typing.Optional[bool] = None,
        checkCrossOrigin: typing.Optional[bool] = None,
        checkOrientation: typing.Optional[bool] = None,
        modal: typing.Optional[bool] = None,
        guides: typing.Optional[bool] = None,
        center: typing.Optional[bool] = None,
        highlight: typing.Optional[bool] = None,
        background: typing.Optional[bool] = None,
        autoCrop: typing.Optional[bool] = None,
        autoCropArea: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        movable: typing.Optional[bool] = None,
        rotatable: typing.Optional[bool] = None,
        scalable: typing.Optional[bool] = None,
        zoomable: typing.Optional[bool] = None,
        zoomOnTouch: typing.Optional[bool] = None,
        zoomOnWheel: typing.Optional[bool] = None,
        wheelZoomRatio: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        cropBoxMovable: typing.Optional[bool] = None,
        cropBoxResizable: typing.Optional[bool] = None,
        toggleDragModeOnDblclick: typing.Optional[bool] = None,
        minContainerWidth: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        minContainerHeight: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        minCanvasWidth: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        minCanvasHeight: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        minCropBoxWidth: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        minCropBoxHeight: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        reset: typing.Optional[bool] = None,
        clear: typing.Optional[bool] = None,
        replace: typing.Optional["Replace"] = None,
        enable: typing.Optional[bool] = None,
        disable: typing.Optional[bool] = None,
        destroy: typing.Optional[bool] = None,
        move: typing.Optional["Move"] = None,
        moveTo: typing.Optional["MoveTo"] = None,
        zoom: typing.Optional["Zoom"] = None,
        zoomTo: typing.Optional["ZoomTo"] = None,
        rotate: typing.Optional["Rotate"] = None,
        rotateTo: typing.Optional["RotateTo"] = None,
        scale: typing.Optional["Scale"] = None,
        scaleX: typing.Optional["ScaleX"] = None,
        scaleY: typing.Optional["ScaleY"] = None,
        outputData: typing.Optional["OutputData"] = None,
        containerData: typing.Optional["ContainerData"] = None,
        imageData: typing.Optional["ImageData"] = None,
        canvasData: typing.Optional["CanvasData"] = None,
        cropBoxData: typing.Optional["CropBoxData"] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'croppedImageData', 'src', 'alt', 'crossOrigin', 'viewMode', 'dragMode', 'initialAspectRatio', 'aspectRatio', 'data', 'preview', 'responsive', 'restore', 'checkCrossOrigin', 'checkOrientation', 'modal', 'guides', 'center', 'highlight', 'background', 'autoCrop', 'autoCropArea', 'movable', 'rotatable', 'scalable', 'zoomable', 'zoomOnTouch', 'zoomOnWheel', 'wheelZoomRatio', 'cropBoxMovable', 'cropBoxResizable', 'toggleDragModeOnDblclick', 'minContainerWidth', 'minContainerHeight', 'minCanvasWidth', 'minCanvasHeight', 'minCropBoxWidth', 'minCropBoxHeight', 'reset', 'clear', 'replace', 'enable', 'disable', 'destroy', 'move', 'moveTo', 'zoom', 'zoomTo', 'rotate', 'rotateTo', 'scale', 'scaleX', 'scaleY', 'outputData', 'containerData', 'imageData', 'canvasData', 'cropBoxData']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'croppedImageData', 'src', 'alt', 'crossOrigin', 'viewMode', 'dragMode', 'initialAspectRatio', 'aspectRatio', 'data', 'preview', 'responsive', 'restore', 'checkCrossOrigin', 'checkOrientation', 'modal', 'guides', 'center', 'highlight', 'background', 'autoCrop', 'autoCropArea', 'movable', 'rotatable', 'scalable', 'zoomable', 'zoomOnTouch', 'zoomOnWheel', 'wheelZoomRatio', 'cropBoxMovable', 'cropBoxResizable', 'toggleDragModeOnDblclick', 'minContainerWidth', 'minContainerHeight', 'minCanvasWidth', 'minCanvasHeight', 'minCropBoxWidth', 'minCropBoxHeight', 'reset', 'clear', 'replace', 'enable', 'disable', 'destroy', 'move', 'moveTo', 'zoom', 'zoomTo', 'rotate', 'rotateTo', 'scale', 'scaleX', 'scaleY', 'outputData', 'containerData', 'imageData', 'canvasData', 'cropBoxData']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyImageCropper, self).__init__(**args)
