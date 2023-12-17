import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyCropper = React.lazy(() => import(/* webpackChunkName: "feffery_cropper" */ '../../fragments/images/FefferyCropper.react'));

const FefferyCropper = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyCropper {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyCropper.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * css类名
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 自定义css字典
     */
    style: PropTypes.object,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 裁剪后的图片数据，base64格式
     */
    croppedImageData: PropTypes.string,

    /**
     * 要裁剪的图片的地址
     */
    src: PropTypes.string,

    /**
     * 图片占位名称，默认为'picture'
     */
    alt: PropTypes.string,
    
    /**
     * 图片跨域属性
     */
    crossOrigin: PropTypes.string,

    /**
     * 设置裁剪框的视图模式。
     * 如果将viewMode设置为0，裁剪框可以超出画布的范围，而设置为1、2或3的值将限制裁剪框的大小与画布一致。
     * viewMode为2或3还会额外限制画布适应容器的大小，当画布和容器的比例相同时，2和3没有区别。
     * 0：无限制。
     * 1：限制裁剪框不超过画布的大小。
     * 2：限制最小画布尺寸适应容器。如果画布和容器的比例不同，最小画布将在一个维度上被额外空间包围。
     * 3：限制最小画布尺寸填满容器。如果画布和容器的比例不同，容器将无法在一个维度上容纳整个画布。
     * 默认为0
     */
    viewMode: PropTypes.oneOf([0, 1, 2, 3]),

    /**
     * 设置裁剪器的拖动模式。
     * 'crop'：创建一个新的裁剪框。
     * 'move'：移动画布。
     * 'none'：无操作。
     * 默认为'crop'
     */
    dragMode: PropTypes.oneOf(['crop', 'move', 'none']),

    /**
     * 设置裁剪框的初始宽高比，默认与画布宽高比相同，仅在aspectRatio未设置时有效
     */
    initialAspectRatio: PropTypes.number,

    /**
     * 设置裁剪框的固定宽高比。 默认情况下，裁剪框具有自由比例
     */
    aspectRatio: PropTypes.number,

    /**
     * 设置初始化时要传给setData方法的裁剪的数据，仅当autoCrop选项设置为true时才有效
     */
    data: PropTypes.object,

    /**
     * 设置预览的容器（选择器）。
     * 注意：最大宽度是预览容器的初始宽度。
     * 最大高度是预览容器的初始高度。
     * 如果您设置了宽高比选项，请务必为预览容器设置相同的宽高比。
     * 如果预览无法正确显示，请将预览容器设置为overflow:hidden样式。
     */
    preview: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string)
    ]),

    /**
     * 调整窗口大小时s是否重新渲染裁剪器，默认为true
     */
    responsive: PropTypes.bool,

    /**
     * 调整窗口大小后是否恢复裁剪区域，默认为true
     */
    restore: PropTypes.bool,

    /**
     * 检查当前图片是否为跨域图片。
     * 如果是，则会在克隆的图片元素中添加一个crossOrigin属性，并在src属性中添加一个时间戳参数，以重新加载源图片，以避免浏览器缓存错误。
     * 向图片元素添加 crossOrigin 属性将停止向图片 URL 添加时间戳并停止重新加载图片。 但是读取图片数据以进行方向检查的请求（XMLHttpRequest）将需要时间戳来破坏缓存以避免浏览器缓存错误。 您可以将checkOrientation选项设置为false以取消此请求。
     * 如果图片的crossOrigin属性值为'use-credentials'，那么当通过XMLHttpRequest读取图片数据时，withCredentials属性将设置为true。
     * 默认为true
     */
    checkCrossOrigin: PropTypes.bool,

    /**
     * 检查当前图片的Exif方向信息。请注意，只有JPEG图片可能包含Exif方向信息。
     * 具体来说，读取旋转或翻转图片的方向值，然后用1（默认值）覆盖方向值，以避免iOS设备上的某些问题。
     * 需要同时将可旋转和可缩放选项设置为 true。
     * 注意：不要总是相信这一点，因为某些 JPG 图片可能具有不正确（非标准）的方向值，需要类型化数组支持（IE 10+）。
     * 默认为true
     */
    checkOrientation: PropTypes.bool,

    /**
     * 是否在图片上方和裁剪框下方显示黑色模态，默认为true
     */
    modal: PropTypes.bool,

    /**
     * 是否显示裁剪框上方的虚线，默认为true
     */
    guides: PropTypes.bool,

    /**
     * 是否在裁剪框上方显示中心指示器，默认为true
     */
    center: PropTypes.bool,

    /**
     * 是否在裁剪框上方显示白色模态（突出显示裁剪框），默认为true
     */
    highlight: PropTypes.bool,

    /**
     * 是否显示容器的网格背景，默认为true
     */
    background: PropTypes.bool,

    /**
     * 是否在初始化时自动裁剪图片，默认为true
     */
    autoCrop: PropTypes.bool,

    /**
     * 设置自动裁剪区域大小，为0到1之间的值，默认为0.8
     */
    autoCropArea: PropTypes.number,

    /**
     * 是否可以移动图片，默认为true
     */
    movable: PropTypes.bool,

    /**
     * 是否可以旋转图片，默认为true
     */
    rotatable: PropTypes.bool,

    /**
     * 是否可以缩放图片（居中缩放），默认为true
     */
    scalable: PropTypes.bool,

    /**
     * 是否可以缩放图片（相对于左上角），默认为true
     */
    zoomable: PropTypes.bool,

    /**
     * 是否可以通过拖动触摸来缩放图片，默认为true
     */
    zoomOnTouch: PropTypes.bool,

    /**
     * 是否可以通过鼠标滚轮缩放图片，默认为true
     */
    zoomOnWheel: PropTypes.bool,

    /**
     * 设置通过鼠标滚轮缩放图片时的缩放比例，默认为0.1
     */
    wheelZoomRatio: PropTypes.number,

    /**
     * 是否可以通过拖动来移动裁剪框，默认为true
     */
    cropBoxMovable: PropTypes.bool,

    /**
     * 是否可以通过拖动来调整裁剪框的大小，默认为true
     */
    cropBoxResizable: PropTypes.bool,

    /**
     * 单击裁剪器两次时，是否可以在'crop'和'move'之间切换拖动模式，需要支持dbclick事件，需要默认为true
     */
    toggleDragModeOnDblclick: PropTypes.bool,

    /**
     * 设置容器的最小宽度，默认为200
     */
    minContainerWidth: PropTypes.number,

    /**
     * 设置容器的最小高度，默认为100
     */
    minContainerHeight: PropTypes.number,

    /**
     * 设置画布的最小宽度，默认为0
     */
    minCanvasWidth: PropTypes.number,

    /**
     * 设置画布的最小高度，默认为0
     */
    minCanvasHeight: PropTypes.number,

    /**
     * 设置裁剪框的最小宽度（这个尺寸是相对于页面的，而不是图片的），默认为0
     */
    minCropBoxWidth: PropTypes.number,

    /**
     * 设置裁剪框的最小高度（这个尺寸是相对于页面的，而不是图片的），默认为0
     */
    minCropBoxHeight: PropTypes.number,

    /**
     * 将图片和裁剪框重置为初始状态，每次设置为true后执行完相应操作后会自动置为false
     */
    reset: PropTypes.bool,

    /**
     * 清除裁剪框，每次设置为true后执行完相应操作后会自动置为false
     */
    clear: PropTypes.bool,

    /**
     * 替换图片的src并重新构建裁剪器，每次isReplace设置为true后执行完相应操作后会自动置为false
     */
    replace: PropTypes.exact({
        /**
         * 是否启用
         */
        isReplace: PropTypes.bool,
        /**
         * 新的图片url
         */
        url: PropTypes.string,
        /**
         * 如果新图片的大小与旧图片相同，则它不会重建裁剪器，而只会更新所有相关图片的url
         */
        hasSameSize: PropTypes.bool
    }),

    /**
     * 启用裁剪器，每次设置为true后执行完相应操作后会自动置为false
     */
    enable: PropTypes.bool,

    /**
     * 禁用裁剪器，每次设置为true后执行完相应操作后会自动置为false
     */
    disable: PropTypes.bool,

    /**
     * 销毁裁剪器并从图片中删除实例，每次设置为true后执行完相应操作后会自动置为false
     */
    destroy: PropTypes.bool,

    /**
     * 使用相对偏移量移动画布，每次isMove设置为true后执行完相应操作后会自动置为false
     */
    move: PropTypes.exact({
        /**
         * 是否启用
         */
        isMove: PropTypes.bool,
        /**
         * 在水平方向上移动大小 （px）
         */
        offsetX: PropTypes.number,
        /**
         * 在垂直方向上移动大小 （px），如果不存在，则其默认值为offsetX
         */
        offsetY: PropTypes.number
    }),

    /**
     * 将画布移动到绝对点，每次isMoveTo设置为true后执行完相应操作后会自动置为false
     */
    moveTo: PropTypes.exact({
        /**
         * 是否启用
         */
        isMoveTo: PropTypes.bool,
        /**
         * 画布left的值
         */
        x: PropTypes.number,
        /**
         * 画布top的值，如果不存在，则其默认值为x
         */
        y: PropTypes.number
    }),

    /**
     * 使用相对比例缩放画布，每次isZoom设置为true后执行完相应操作后会自动置为false
     */
    zoom: PropTypes.exact({
        /**
         * 是否启用
         */
        isZoom: PropTypes.bool,
        /**
         * 放大：需要一个正数（比率 > 0）；
         * 缩小：需要负数（比率 < 0）
         */
        ratio: PropTypes.number
    }),

    /**
     * 将画布缩放到绝对比例，每次isZoomTo设置为true后执行完相应操作后会自动置为false
     */
    zoomTo: PropTypes.exact({
        /**
         * 是否启用
         */
        isZoomTo: PropTypes.bool,
        /**
         * 需要一个正数（比率 > 0）
         */
        ratio: PropTypes.number,
        /**
         * 用于缩放的中心点的坐标，基于裁剪器容器的左上角
         */
        pivot: PropTypes.exact({
            x: PropTypes.number,
            y: PropTypes.number
        })
    }),

    /**
     * 将图片旋转到相对角度，每次isRotate设置为true后执行完相应操作后会自动置为false
     */
    rotate: PropTypes.exact({
        /**
         * 是否启用
         */
        isRotate: PropTypes.bool,
        /**
         * 向右旋转：需要正数（度数 > 0）；
         * 向左旋转：需要负数（度数 < 0）
         */
        degree: PropTypes.number
    }),

    /**
     * 将图片旋转到绝对角度，每次isRotateTo设置为true后执行完相应操作后会自动置为false
     */
    rotateTo: PropTypes.exact({
        /**
         * 是否启用
         */
        isRotateTo: PropTypes.bool,
        /**
         * 绝对角度的度数
         */
        degree: PropTypes.number
    }),

    /**
     * 缩放图片，每次isScale设置为true后执行完相应操作后会自动置为false
     */
    scale: PropTypes.exact({
        /**
         * 是否启用
         */
        isScale: PropTypes.bool,
        /**
         * 要应用于图片横坐标的比例因子，当等于1时，图片保持不变
         */
        scaleX: PropTypes.number,
        /**
         * 要应用于图片纵坐标的比例因子，如果不存在，则其默认值为scaleX
         */
        scaleY: PropTypes.number
    }),

    /**
     * 缩放图片的横坐标，每次isScaleX设置为true后执行完相应操作后会自动置为false
     */
    scaleX: PropTypes.exact({
        /**
         * 是否启用
         */
        isScaleX: PropTypes.bool,
        /**
         * 要应用于图片横坐标的比例因子，当等于1时，图片保持不变
         */
        scaleX: PropTypes.number
    }),

    /**
     * 缩放图片的纵坐标，每次isScaleY设置为true后执行完相应操作后会自动置为false
     */
    scaleY: PropTypes.exact({
        /**
         * 是否启用
         */
        isScaleY: PropTypes.bool,
        /**
         * 要应用于图片纵坐标的比例因子，当等于1时，图片保持不变
         */
        scaleY: PropTypes.number
    }),

    /**
     * 输出的最终裁剪的区域位置和大小数据（基于原始图像的自然大小）
     */
    outputData: PropTypes.exact({
        /**
         * 裁剪区域的左侧偏移量
         */
        x: PropTypes.number,
        /**
         * 裁剪区域的顶部偏移量
         */
        y: PropTypes.number,
        /**
         * 裁剪区域的宽度
         */
        width: PropTypes.number,
        /**
         * 裁剪区域的高度
         */
        height: PropTypes.number,
        /**
         * 图片的旋转角度
         */
        rotate: PropTypes.number,
        /**
         * 缩放后应用于图片横坐标的缩放因子
         */
        scaleX: PropTypes.number,
        /**
         * 缩放后应用于图片纵坐标的缩放因子
         */
        scaleY: PropTypes.number
    }),

    /**
     * 输出的容器大小数据
     */
    containerData: PropTypes.exact({
        /**
         * 容器的当前宽度
         */
        width: PropTypes.number,
        /**
         * 容器的当前高度
         */
        height: PropTypes.number
    }),

    /**
     * 输出的图片数据
     */
    imageData: PropTypes.exact({
        /**
         * 图片的左侧偏移量
         */
        left: PropTypes.number,
        /**
         * 图片的顶部偏移量
         */
        top: PropTypes.number,
        /**
         * 图片的宽度
         */
        width: PropTypes.number,
        /**
         * 图片的高度
         */
        height: PropTypes.number,
        /**
         * 图片的原始宽度
         */
        naturalWidth: PropTypes.number,
        /**
         * 图片的原始高度
         */
        naturalHeight: PropTypes.number,
        /**
         * 图片的纵横比
         */
        aspectRatio: PropTypes.number,
        /**
         * 图片的旋转角度
         */
        rotate: PropTypes.number,
        /**
         * 缩放后应用于图片横坐标的缩放因子
         */
        scaleX: PropTypes.number,
        /**
         * 缩放后应用于图片纵坐标的缩放因子
         */
        scaleY: PropTypes.number
    }),

    /**
     * 输出的画布数据
     */
    canvasData: PropTypes.exact({
        /**
         * 画布的左侧偏移量
         */
        left: PropTypes.number,
        /**
         * 画布的顶部偏移量
         */
        top: PropTypes.number,
        /**
         * 画布的宽度
         */
        width: PropTypes.number,
        /**
         * 画布的高度
         */
        height: PropTypes.number,
        /**
         * 画布的原始宽度（只读）
         */
        naturalWidth: PropTypes.number,
        /**
         * 画布的原始高度（只读）
         */
        naturalHeight: PropTypes.number
    }),

    /**
     * 输出的裁剪框数据
     */
    cropBoxData: PropTypes.exact({
        /**
         * 裁剪框的左侧偏移量
         */
        left: PropTypes.number,
        /**
         * 裁剪框的顶部偏移量
         */
        top: PropTypes.number,
        /**
         * 裁剪框的宽度
         */
        width: PropTypes.number,
        /**
         * 裁剪框的高度
         */
        height: PropTypes.number
    }),

    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

// 设置默认参数
FefferyCropper.defaultProps = {
    alt: 'picture',
    viewMode: 0,
    dragMode: 'crop',
    preview: '',
    responsive: true,
    restore: true,
    checkCrossOrigin: true,
    checkOrientation: true,
    modal: true,
    guides: true,
    center: true,
    highlight: true,
    background: true,
    autoCrop: true,
    autoCropArea: 0.8,
    movable: true,
    rotatable: true,
    scalable: true,
    zoomable: true,
    zoomOnTouch: true,
    zoomOnWheel: true,
    wheelZoomRatio: 0.1,
    cropBoxMovable: true,
    cropBoxResizable: true,
    toggleDragModeOnDblclick: true,
    minContainerWidth: 200,
    minContainerHeight: 100,
    minCanvasWidth: 0,
    minCanvasHeight: 0,
    minCropBoxWidth: 0,
    minCropBoxHeight: 0,
    reset: false,
    clear: false,
    replace: {
        isReplace: false,
        hasSameSize: false
    },
    enable: false,
    disable: false,
    destroy: false,
    move: {
        isMove: false
    },
    moveTo: {
        isMoveTo: false
    },
    zoom: {
        isZoom: false
    },
    zoomTo: {
        isZoomTo: false
    },
    rotate: {
        isRotate: false
    },
    rotateTo: {
        isRotateTo: false
    },
    scale: {
        isScale: false
    },
    scaleX: {
        isScaleX: false
    },
    scaleY: {
        isScaleY: false
    }
}

export default FefferyCropper;

export const propTypes = FefferyCropper.propTypes;
export const defaultProps = FefferyCropper.defaultProps;