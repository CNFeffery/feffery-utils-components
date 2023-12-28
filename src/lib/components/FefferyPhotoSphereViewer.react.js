import { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyPhotoSphereViewer = React.lazy(() => import(/* webpackChunkName: "feffery_photo_sphere_viewer" */ '../fragments/FefferyPhotoSphereViewer.react'));

const FefferyPhotoSphereViewer = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyPhotoSphereViewer {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyPhotoSphereViewer.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 设置全景图片资源地址
     */
    src: PropTypes.string,

    /**
     * 设置查看器宽度，同css中的width属性
     */
    width: PropTypes.string,

    /**
     * 设置查看器高度，同css中的height属性
     */
    height: PropTypes.string,

    /**
     * 是否开启小星球模式
     * 默认：false
     */
    littlePlanet: PropTypes.bool,

    /**
     * 设置查看器所在容器css类名
     */
    containerClass: PropTypes.string,

    /**
     * 配置导航栏中需要显示的功能项及顺序
     * 可选的有'zoom'、'move'、'download'、'caption'、'fullscreen'
     * 默认：['caption']
     */
    navbar: PropTypes.arrayOf(
        PropTypes.oneOf(['zoom', 'move', 'download', 'caption', 'fullscreen'])
    ),

    /**
     * 导航栏标题内容，支持HTML字符串，仅当navbar中包含'caption'时有效
     */
    caption: PropTypes.string,

    /**
     * 自定义载入阶段过场图片地址
     */
    loadingImg: PropTypes.string,

    /**
     * 自定义载入阶段文字提示内容
     */
    loadingTxt: PropTypes.string,

    /**
     * 是否允许鼠标滚轮缩放
     * 默认：true
     */
    mousewheel: PropTypes.bool,

    /**
     * 是否允许鼠标拖拽平移
     * 默认：true
     */
    mousemove: PropTypes.bool,

    /**
     * 设置鼠标平移速度
     * 默认：1
     */
    moveSpeed: PropTypes.number,

    /**
     * 设置鼠标滚轮缩放速度
     * 默认：1
     */
    zoomSpeed: PropTypes.number,

    /**
     * 是否开启鱼眼模式
     * 默认：false
     */
    fisheye: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

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
    })
};

// 设置默认参数
FefferyPhotoSphereViewer.defaultProps = {
    littlePlanet: false,
    navbar: ['caption'],
    mousewheel: true,
    mousemove: true,
    moveSpeed: 1,
    zoomSpeed: 1,
    fisheye: false
}

export default FefferyPhotoSphereViewer;

export const propTypes = FefferyPhotoSphereViewer.propTypes;
export const defaultProps = FefferyPhotoSphereViewer.defaultProps;