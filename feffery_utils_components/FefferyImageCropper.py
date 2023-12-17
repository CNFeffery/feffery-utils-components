# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyImageCropper(Component):
    """A FefferyImageCropper component.


Keyword arguments:

- id (string; optional):
    组件id.

- alt (string; default 'picture'):
    图片占位名称，默认为'picture'.

- aspectRatio (number; optional):
    设置裁剪框的固定宽高比。 默认情况下，裁剪框具有自由比例.

- autoCrop (boolean; default True):
    是否在初始化时自动裁剪图片，默认为True.

- autoCropArea (number; default 0.8):
    设置自动裁剪区域大小，为0到1之间的值，默认为0.8.

- background (boolean; default True):
    是否显示容器的网格背景，默认为True.

- canvasData (dict; optional):
    输出的画布数据.

    `canvasData` is a dict with keys:

    - height (number; optional):
        画布的高度.

    - left (number; optional):
        画布的左侧偏移量.

    - naturalHeight (number; optional):
        画布的原始高度（只读）.

    - naturalWidth (number; optional):
        画布的原始宽度（只读）.

    - top (number; optional):
        画布的顶部偏移量.

    - width (number; optional):
        画布的宽度.

- center (boolean; default True):
    是否在裁剪框上方显示中心指示器，默认为True.

- checkCrossOrigin (boolean; default True):
    检查当前图片是否为跨域图片。
    如果是，则会在克隆的图片元素中添加一个crossOrigin属性，并在src属性中添加一个时间戳参数，以重新加载源图片，以避免浏览器缓存错误。
    向图片元素添加 crossOrigin 属性将停止向图片 URL 添加时间戳并停止重新加载图片。
    但是读取图片数据以进行方向检查的请求（XMLHttpRequest）将需要时间戳来破坏缓存以避免浏览器缓存错误。
    您可以将checkOrientation选项设置为False以取消此请求。
    如果图片的crossOrigin属性值为'use-credentials'，那么当通过XMLHttpRequest读取图片数据时，withCredentials属性将设置为True。
    默认为True.

- checkOrientation (boolean; default True):
    检查当前图片的Exif方向信息。请注意，只有JPEG图片可能包含Exif方向信息。
    具体来说，读取旋转或翻转图片的方向值，然后用1（默认值）覆盖方向值，以避免iOS设备上的某些问题。
    需要同时将可旋转和可缩放选项设置为 True。  注意：不要总是相信这一点，因为某些 JPG
    图片可能具有不正确（非标准）的方向值，需要类型化数组支持（IE 10+）。  默认为True.

- className (string | dict; optional):
    css类名.

- clear (boolean; default False):
    清除裁剪框，每次设置为True后执行完相应操作后会自动置为False.

- containerData (dict; optional):
    输出的容器大小数据.

    `containerData` is a dict with keys:

    - height (number; optional):
        容器的当前高度.

    - width (number; optional):
        容器的当前宽度.

- cropBoxData (dict; optional):
    输出的裁剪框数据.

    `cropBoxData` is a dict with keys:

    - height (number; optional):
        裁剪框的高度.

    - left (number; optional):
        裁剪框的左侧偏移量.

    - top (number; optional):
        裁剪框的顶部偏移量.

    - width (number; optional):
        裁剪框的宽度.

- cropBoxMovable (boolean; default True):
    是否可以通过拖动来移动裁剪框，默认为True.

- cropBoxResizable (boolean; default True):
    是否可以通过拖动来调整裁剪框的大小，默认为True.

- croppedImageData (string; optional):
    裁剪后的图片数据，base64格式.

- crossOrigin (string; optional):
    图片跨域属性.

- data (dict; optional):
    设置初始化时要传给setData方法的裁剪的数据，仅当autoCrop选项设置为True时才有效.

- destroy (boolean; default False):
    销毁裁剪器并从图片中删除实例，每次设置为True后执行完相应操作后会自动置为False.

- disable (boolean; default False):
    禁用裁剪器，每次设置为True后执行完相应操作后会自动置为False.

- dragMode (a value equal to: 'crop', 'move', 'none'; default 'crop'):
    设置裁剪器的拖动模式。  'crop'：创建一个新的裁剪框。  'move'：移动画布。  'none'：无操作。
    默认为'crop'.

- enable (boolean; default False):
    启用裁剪器，每次设置为True后执行完相应操作后会自动置为False.

- guides (boolean; default True):
    是否显示裁剪框上方的虚线，默认为True.

- highlight (boolean; default True):
    是否在裁剪框上方显示白色模态（突出显示裁剪框），默认为True.

- imageData (dict; optional):
    输出的图片数据.

    `imageData` is a dict with keys:

    - aspectRatio (number; optional):
        图片的纵横比.

    - height (number; optional):
        图片的高度.

    - left (number; optional):
        图片的左侧偏移量.

    - naturalHeight (number; optional):
        图片的原始高度.

    - naturalWidth (number; optional):
        图片的原始宽度.

    - rotate (number; optional):
        图片的旋转角度.

    - scaleX (number; optional):
        缩放后应用于图片横坐标的缩放因子.

    - scaleY (number; optional):
        缩放后应用于图片纵坐标的缩放因子.

    - top (number; optional):
        图片的顶部偏移量.

    - width (number; optional):
        图片的宽度.

- initialAspectRatio (number; optional):
    设置裁剪框的初始宽高比，默认与画布宽高比相同，仅在aspectRatio未设置时有效.

- key (string; optional):
    辅助刷新用唯一标识key值.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- minCanvasHeight (number; default 0):
    设置画布的最小高度，默认为0.

- minCanvasWidth (number; default 0):
    设置画布的最小宽度，默认为0.

- minContainerHeight (number; default 100):
    设置容器的最小高度，默认为100.

- minContainerWidth (number; default 200):
    设置容器的最小宽度，默认为200.

- minCropBoxHeight (number; default 0):
    设置裁剪框的最小高度（这个尺寸是相对于页面的，而不是图片的），默认为0.

- minCropBoxWidth (number; default 0):
    设置裁剪框的最小宽度（这个尺寸是相对于页面的，而不是图片的），默认为0.

- modal (boolean; default True):
    是否在图片上方和裁剪框下方显示黑色模态，默认为True.

- movable (boolean; default True):
    是否可以移动图片，默认为True.

- move (dict; default {    isMove: False}):
    使用相对偏移量移动画布，每次isMove设置为True后执行完相应操作后会自动置为False.

    `move` is a dict with keys:

    - isMove (boolean; optional):
        是否启用.

    - offsetX (number; optional):
        在水平方向上移动大小 （px）.

    - offsetY (number; optional):
        在垂直方向上移动大小 （px），如果不存在，则其默认值为offsetX.

- moveTo (dict; default {    isMoveTo: False}):
    将画布移动到绝对点，每次isMoveTo设置为True后执行完相应操作后会自动置为False.

    `moveTo` is a dict with keys:

    - isMoveTo (boolean; optional):
        是否启用.

    - x (number; optional):
        画布left的值.

    - y (number; optional):
        画布top的值，如果不存在，则其默认值为x.

- outputData (dict; optional):
    输出的最终裁剪的区域位置和大小数据（基于原始图像的自然大小）.

    `outputData` is a dict with keys:

    - height (number; optional):
        裁剪区域的高度.

    - rotate (number; optional):
        图片的旋转角度.

    - scaleX (number; optional):
        缩放后应用于图片横坐标的缩放因子.

    - scaleY (number; optional):
        缩放后应用于图片纵坐标的缩放因子.

    - width (number; optional):
        裁剪区域的宽度.

    - x (number; optional):
        裁剪区域的左侧偏移量.

    - y (number; optional):
        裁剪区域的顶部偏移量.

- preview (string | list of strings; default ''):
    设置预览的容器（选择器）。  注意：最大宽度是预览容器的初始宽度。  最大高度是预览容器的初始高度。
    如果您设置了宽高比选项，请务必为预览容器设置相同的宽高比。
    如果预览无法正确显示，请将预览容器设置为overflow:hidden样式。.

- replace (dict; default {    isReplace: False,    hasSameSize: False}):
    替换图片的src并重新构建裁剪器，每次isReplace设置为True后执行完相应操作后会自动置为False.

    `replace` is a dict with keys:

    - hasSameSize (boolean; optional):
        如果新图片的大小与旧图片相同，则它不会重建裁剪器，而只会更新所有相关图片的url.

    - isReplace (boolean; optional):
        是否启用.

    - url (string; optional):
        新的图片url.

- reset (boolean; default False):
    将图片和裁剪框重置为初始状态，每次设置为True后执行完相应操作后会自动置为False.

- responsive (boolean; default True):
    调整窗口大小时s是否重新渲染裁剪器，默认为True.

- restore (boolean; default True):
    调整窗口大小后是否恢复裁剪区域，默认为True.

- rotatable (boolean; default True):
    是否可以旋转图片，默认为True.

- rotate (dict; default {    isRotate: False}):
    将图片旋转到相对角度，每次isRotate设置为True后执行完相应操作后会自动置为False.

    `rotate` is a dict with keys:

    - degree (number; optional):
        向右旋转：需要正数（度数 > 0）；  向左旋转：需要负数（度数 < 0）.

    - isRotate (boolean; optional):
        是否启用.

- rotateTo (dict; default {    isRotateTo: False}):
    将图片旋转到绝对角度，每次isRotateTo设置为True后执行完相应操作后会自动置为False.

    `rotateTo` is a dict with keys:

    - degree (number; optional):
        绝对角度的度数.

    - isRotateTo (boolean; optional):
        是否启用.

- scalable (boolean; default True):
    是否可以缩放图片（居中缩放），默认为True.

- scale (dict; default {    isScale: False}):
    缩放图片，每次isScale设置为True后执行完相应操作后会自动置为False.

    `scale` is a dict with keys:

    - isScale (boolean; optional):
        是否启用.

    - scaleX (number; optional):
        要应用于图片横坐标的比例因子，当等于1时，图片保持不变.

    - scaleY (number; optional):
        要应用于图片纵坐标的比例因子，如果不存在，则其默认值为scaleX.

- scaleX (dict; default {    isScaleX: False}):
    缩放图片的横坐标，每次isScaleX设置为True后执行完相应操作后会自动置为False.

    `scaleX` is a dict with keys:

    - isScaleX (boolean; optional):
        是否启用.

    - scaleX (number; optional):
        要应用于图片横坐标的比例因子，当等于1时，图片保持不变.

- scaleY (dict; default {    isScaleY: False}):
    缩放图片的纵坐标，每次isScaleY设置为True后执行完相应操作后会自动置为False.

    `scaleY` is a dict with keys:

    - isScaleY (boolean; optional):
        是否启用.

    - scaleY (number; optional):
        要应用于图片纵坐标的比例因子，当等于1时，图片保持不变.

- src (string; optional):
    要裁剪的图片的地址.

- style (dict; optional):
    自定义css字典.

- toggleDragModeOnDblclick (boolean; default True):
    单击裁剪器两次时，是否可以在'crop'和'move'之间切换拖动模式，需要支持dbclick事件，需要默认为True.

- viewMode (a value equal to: 0, 1, 2, 3; default 0):
    设置裁剪框的视图模式。
    如果将viewMode设置为0，裁剪框可以超出画布的范围，而设置为1、2或3的值将限制裁剪框的大小与画布一致。
    viewMode为2或3还会额外限制画布适应容器的大小，当画布和容器的比例相同时，2和3没有区别。  0：无限制。
    1：限制裁剪框不超过画布的大小。  2：限制最小画布尺寸适应容器。如果画布和容器的比例不同，最小画布将在一个维度上被额外空间包围。
    3：限制最小画布尺寸填满容器。如果画布和容器的比例不同，容器将无法在一个维度上容纳整个画布。  默认为0.

- wheelZoomRatio (number; default 0.1):
    设置通过鼠标滚轮缩放图片时的缩放比例，默认为0.1.

- zoom (dict; default {    isZoom: False}):
    使用相对比例缩放画布，每次isZoom设置为True后执行完相应操作后会自动置为False.

    `zoom` is a dict with keys:

    - isZoom (boolean; optional):
        是否启用.

    - ratio (number; optional):
        放大：需要一个正数（比率 > 0）；  缩小：需要负数（比率 < 0）.

- zoomOnTouch (boolean; default True):
    是否可以通过拖动触摸来缩放图片，默认为True.

- zoomOnWheel (boolean; default True):
    是否可以通过鼠标滚轮缩放图片，默认为True.

- zoomTo (dict; default {    isZoomTo: False}):
    将画布缩放到绝对比例，每次isZoomTo设置为True后执行完相应操作后会自动置为False.

    `zoomTo` is a dict with keys:

    - isZoomTo (boolean; optional):
        是否启用.

    - pivot (dict; optional):
        用于缩放的中心点的坐标，基于裁剪器容器的左上角.

        `pivot` is a dict with keys:

        - x (number; optional)

        - y (number; optional)

    - ratio (number; optional):
        需要一个正数（比率 > 0）.

- zoomable (boolean; default True):
    是否可以缩放图片（相对于左上角），默认为True."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyImageCropper'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, croppedImageData=Component.UNDEFINED, src=Component.UNDEFINED, alt=Component.UNDEFINED, crossOrigin=Component.UNDEFINED, viewMode=Component.UNDEFINED, dragMode=Component.UNDEFINED, initialAspectRatio=Component.UNDEFINED, aspectRatio=Component.UNDEFINED, data=Component.UNDEFINED, preview=Component.UNDEFINED, responsive=Component.UNDEFINED, restore=Component.UNDEFINED, checkCrossOrigin=Component.UNDEFINED, checkOrientation=Component.UNDEFINED, modal=Component.UNDEFINED, guides=Component.UNDEFINED, center=Component.UNDEFINED, highlight=Component.UNDEFINED, background=Component.UNDEFINED, autoCrop=Component.UNDEFINED, autoCropArea=Component.UNDEFINED, movable=Component.UNDEFINED, rotatable=Component.UNDEFINED, scalable=Component.UNDEFINED, zoomable=Component.UNDEFINED, zoomOnTouch=Component.UNDEFINED, zoomOnWheel=Component.UNDEFINED, wheelZoomRatio=Component.UNDEFINED, cropBoxMovable=Component.UNDEFINED, cropBoxResizable=Component.UNDEFINED, toggleDragModeOnDblclick=Component.UNDEFINED, minContainerWidth=Component.UNDEFINED, minContainerHeight=Component.UNDEFINED, minCanvasWidth=Component.UNDEFINED, minCanvasHeight=Component.UNDEFINED, minCropBoxWidth=Component.UNDEFINED, minCropBoxHeight=Component.UNDEFINED, reset=Component.UNDEFINED, clear=Component.UNDEFINED, replace=Component.UNDEFINED, enable=Component.UNDEFINED, disable=Component.UNDEFINED, destroy=Component.UNDEFINED, move=Component.UNDEFINED, moveTo=Component.UNDEFINED, zoom=Component.UNDEFINED, zoomTo=Component.UNDEFINED, rotate=Component.UNDEFINED, rotateTo=Component.UNDEFINED, scale=Component.UNDEFINED, scaleX=Component.UNDEFINED, scaleY=Component.UNDEFINED, outputData=Component.UNDEFINED, containerData=Component.UNDEFINED, imageData=Component.UNDEFINED, canvasData=Component.UNDEFINED, cropBoxData=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'alt', 'aspectRatio', 'autoCrop', 'autoCropArea', 'background', 'canvasData', 'center', 'checkCrossOrigin', 'checkOrientation', 'className', 'clear', 'containerData', 'cropBoxData', 'cropBoxMovable', 'cropBoxResizable', 'croppedImageData', 'crossOrigin', 'data', 'destroy', 'disable', 'dragMode', 'enable', 'guides', 'highlight', 'imageData', 'initialAspectRatio', 'key', 'loading_state', 'minCanvasHeight', 'minCanvasWidth', 'minContainerHeight', 'minContainerWidth', 'minCropBoxHeight', 'minCropBoxWidth', 'modal', 'movable', 'move', 'moveTo', 'outputData', 'preview', 'replace', 'reset', 'responsive', 'restore', 'rotatable', 'rotate', 'rotateTo', 'scalable', 'scale', 'scaleX', 'scaleY', 'src', 'style', 'toggleDragModeOnDblclick', 'viewMode', 'wheelZoomRatio', 'zoom', 'zoomOnTouch', 'zoomOnWheel', 'zoomTo', 'zoomable']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'alt', 'aspectRatio', 'autoCrop', 'autoCropArea', 'background', 'canvasData', 'center', 'checkCrossOrigin', 'checkOrientation', 'className', 'clear', 'containerData', 'cropBoxData', 'cropBoxMovable', 'cropBoxResizable', 'croppedImageData', 'crossOrigin', 'data', 'destroy', 'disable', 'dragMode', 'enable', 'guides', 'highlight', 'imageData', 'initialAspectRatio', 'key', 'loading_state', 'minCanvasHeight', 'minCanvasWidth', 'minContainerHeight', 'minContainerWidth', 'minCropBoxHeight', 'minCropBoxWidth', 'modal', 'movable', 'move', 'moveTo', 'outputData', 'preview', 'replace', 'reset', 'responsive', 'restore', 'rotatable', 'rotate', 'rotateTo', 'scalable', 'scale', 'scaleX', 'scaleY', 'src', 'style', 'toggleDragModeOnDblclick', 'viewMode', 'wheelZoomRatio', 'zoom', 'zoomOnTouch', 'zoomOnWheel', 'zoomTo', 'zoomable']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyImageCropper, self).__init__(**args)
