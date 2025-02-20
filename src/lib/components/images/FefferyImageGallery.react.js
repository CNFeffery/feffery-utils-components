// react核心
import PropTypes from 'prop-types';
// 组件核心
import ImageGallery from "react-image-gallery";
// 辅助库
import { useLoading } from '../utils';
// 样式
import "react-image-gallery/styles/css/image-gallery.css";

/**
 * 相册组件FefferyImageGallery
 */
const FefferyImageGallery = ({
    id,
    style,
    className,
    images,
    infinite = true,
    lazyLoad = false,
    showNav = true,
    showThumbnails = true,
    thumbnailPosition = 'bottom',
    showFullscreenButton = true,
    useBrowserFullscreen = true,
    showPlayButton = true,
    showBullets = false,
    showIndex = false,
    autoPlay = false,
    slideDuration = 450,
    slideInterval = 3000,
    startIndex = 0,
    isFullscreen = false,
    setProps
}) => {

    return (
        <div style={style}
            className={className}>
            <ImageGallery
                id={id}
                items={images}
                infinite={infinite}
                lazyLoad={lazyLoad}
                showNav={showNav}
                showThumbnails={showThumbnails}
                thumbnailPosition={thumbnailPosition}
                showFullscreenButton={showFullscreenButton}
                useBrowserFullscreen={useBrowserFullscreen}
                showPlayButton={showPlayButton}
                showBullets={showBullets}
                showIndex={showIndex}
                autoPlay={autoPlay}
                slideDuration={slideDuration}
                slideInterval={slideInterval}
                startIndex={startIndex}
                isFullscreen={isFullscreen}
                onScreenChange={(e) => setProps({ isFullscreen: e })}
                data-dash-is-loading={useLoading()}
            />
        </div>
    );
}

FefferyImageGallery.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 必填，用于定义相册内部各图片相关信息数组
     */
    images: PropTypes.array,

    /**
     * 是否启用无限轮播
     * 默认值：`true`
     */
    infinite: PropTypes.bool,

    /**
     * 是否为图片启用懒加载功能
     * 默认值：`false`
     */
    lazyLoad: PropTypes.bool,

    /**
     * 是否展示导航按钮
     * 默认值：`true`
     */
    showNav: PropTypes.bool,

    /**
     * 是否展示缩略图列表
     * 默认值：`true`
     */
    showThumbnails: PropTypes.bool,

    /**
     * 设置缩略图方位，可选项有`'top'`、`'right'`、`'bottom'`、`'left'`
     * 默认值：`'bottom'`
     */
    thumbnailPosition: PropTypes.oneOf(['top', 'right', 'bottom', 'left']),

    /**
     * 是否展示全屏功能按钮
     * 默认值：`true`
     */
    showFullscreenButton: PropTypes.bool,

    /**
     * 是否使用原生全屏化功能
     * 默认值：`true`
     */
    useBrowserFullscreen: PropTypes.bool,

    /**
     * 是否展示播放功能按钮
     * 默认值：`true`
     */
    showPlayButton: PropTypes.bool,

    /**
     * 是否展示快捷跳转指示器
     * 默认值：`false`
     */
    showBullets: PropTypes.bool,

    /**
     * 是否展示图片序号信息
     * 默认值：`false`
     */
    showIndex: PropTypes.bool,

    /**
     * 是否启用自动播放
     * 默认值：`false`
     */
    autoPlay: PropTypes.bool,

    /**
     * 设置图片轮播动画的持续时长，单位：毫秒
     * 默认值：`450`
     */
    slideDuration: PropTypes.number,

    /**
     * 设置图片轮播动画的间隔时长，单位：毫秒
     * 默认值：`3000`
     */
    slideInterval: PropTypes.number,

    /**
     * 设置初始化图片下标，从0开始
     * 默认值：`0`
     */
    startIndex: PropTypes.number,

    /**
     * 监听当前相册是否处于全屏化状态
     * 默认值：`false`
     */
    isFullscreen: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyImageGallery;