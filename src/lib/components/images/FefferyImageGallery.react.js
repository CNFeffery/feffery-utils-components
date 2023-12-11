import PropTypes from 'prop-types';
import ImageGallery from "react-image-gallery";
import "react-image-gallery/styles/css/image-gallery.css";

// 定义相册组件FefferyImageGallery
const FefferyImageGallery = (props) => {
    // 取得必要属性或参数
    const {
        id,
        style,
        className,
        images,
        infinite,
        lazyLoad,
        showNav,
        showThumbnails,
        thumbnailPosition,
        showFullscreenButton,
        useBrowserFullscreen,
        showPlayButton,
        showBullets,
        showIndex,
        slideDuration,
        slideInterval,
        startIndex,
        setProps,
        loading_state
    } = props;

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
                slideDuration={slideDuration}
                slideInterval={slideInterval}
                startIndex={startIndex}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }
            />
        </div>
    );
}

// 定义参数或属性
FefferyImageGallery.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * css样式
     */
    style: PropTypes.object,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * 必填，用于定义相册内部各图片相关信息数组
     */
    images: PropTypes.array,

    /**
     * 是否启用无限轮播
     * 默认：true
     */
    infinite: PropTypes.bool,

    /**
     * 是否为图片启用懒加载功能
     * 默认：false
     */
    lazyLoad: PropTypes.bool,

    /**
     * 是否展示导航按钮
     * 默认：true
     */
    showNav: PropTypes.bool,

    /**
     * 是否展示缩略图列表
     * 默认：true
     */
    showThumbnails: PropTypes.bool,

    /**
     * 设置缩略图方位，可选的有'top'、'right'、'bottom'、'left'
     * 默认：'bottom'
     */
    thumbnailPosition: PropTypes.oneOf(['top', 'right', 'bottom', 'left']),

    /**
     * 是否展示全屏功能按钮
     * 默认：true
     */
    showFullscreenButton: PropTypes.bool,

    /**
     * 是否使用原生全屏化功能
     * 默认：true
     */
    useBrowserFullscreen: PropTypes.bool,

    /**
     * 是否展示播放功能按钮
     * 默认：true
     */
    showPlayButton: PropTypes.bool,

    /**
     * 是否展示快捷跳转指示器
     * 默认：false
     */
    showBullets: PropTypes.bool,

    /**
     * 是否展示图片序号信息
     * 默认：false
     */
    showIndex: PropTypes.bool,

    /**
     * 是否启用自动播放
     * 默认：false
     */
    autoPlay: PropTypes.bool,

    /**
     * 设置图片轮播动画的持续时长，单位：毫秒
     * 默认：450
     */
    slideDuration: PropTypes.number,

    /**
     * 设置图片轮播动画的间隔时长，单位：毫秒
     * 默认：3000
     */
    slideInterval: PropTypes.number,

    /**
     * 设置初始化图片下标，从0开始
     * 默认：0
     */
    startIndex: PropTypes.number,

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
FefferyImageGallery.defaultProps = {
    infinite: true,
    lazyLoad: false,
    showNav: true,
    showThumbnails: true,
    thumbnailPosition: 'bottom',
    showFullscreenButton: true,
    useBrowserFullscreen: true,
    showPlayButton: true,
    showBullets: false,
    showIndex: false,
    autoPlay: false,
    slideDuration: 450,
    slideInterval: 3000,
    startIndex: 0
}

export default FefferyImageGallery;