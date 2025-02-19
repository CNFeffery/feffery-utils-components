import { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyPhotoSphereViewer = React.lazy(() => import(/* webpackChunkName: "feffery_photo_sphere_viewer" */ '../../fragments/images/FefferyPhotoSphereViewer.react'));

/**
 * 全景图片查看器组件FefferyPhotoSphereViewer
 */
const FefferyPhotoSphereViewer = ({
    littlePlanet = false,
    navbar = ['caption'],
    mousewheel = true,
    mousemove = true,
    moveSpeed = 1,
    zoomSpeed = 1,
    fisheye = false,
    hideNavbarButton = false,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyPhotoSphereViewer {
                ...{
                    littlePlanet,
                    navbar,
                    mousewheel,
                    mousemove,
                    moveSpeed,
                    zoomSpeed,
                    fisheye,
                    hideNavbarButton,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyPhotoSphereViewer.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 全景图片资源地址
     */
    src: PropTypes.string,

    /**
     * 设置查看器宽度，同`css`中的`width`属性
     */
    width: PropTypes.string,

    /**
     * 设置查看器高度，同`css`中的`height`属性
     */
    height: PropTypes.string,

    /**
     * 是否开启小星球模式
     * 默认值：`false`
     */
    littlePlanet: PropTypes.bool,

    /**
     * 设置查看器所在容器`css`类名
     */
    containerClass: PropTypes.string,

    /**
     * 配置导航栏中需要显示的功能项及顺序，设置为`false`时将隐藏导航栏，可选项有`'zoom'`、`'move'`、`'download'`、`'caption'`、`'fullscreen'`、`'autorotate'`
     * 默认值：`['caption']`
     */
    navbar: PropTypes.oneOfType(
        [
            PropTypes.arrayOf(
                PropTypes.oneOf(['zoom', 'move', 'download', 'caption', 'fullscreen', 'autorotate'])
            ),
            PropTypes.bool
        ]
    ),

    /**
     * 导航栏标题内容，支持`HTML`字符串，仅当`navbar`中包含`'caption'`时有效
     */
    caption: PropTypes.string,

    /**
     * 手动设置下载目标文件地址
     */
    downloadUrl: PropTypes.string,

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
     * 默认值：`true`
     */
    mousewheel: PropTypes.bool,

    /**
     * 是否允许鼠标拖拽平移
     * 默认值：`true`
     */
    mousemove: PropTypes.bool,

    /**
     * 设置鼠标平移速度
     * 默认值：`1`
     */
    moveSpeed: PropTypes.number,

    /**
     * 设置鼠标滚轮缩放速度
     * 默认值：`1`
     */
    zoomSpeed: PropTypes.number,

    /**
     * 是否开启鱼眼模式
     * 默认值：`false`
     */
    fisheye: PropTypes.bool,

    /**
     * 为相关功能控件或场景设置鼠标悬停提示信息文案
     */
    lang: PropTypes.exact({
        /**
         * 小星球模式
         */
        littlePlanetButton: PropTypes.string,
        /**
         * 缩小操作
         */
        zoomOut: PropTypes.string,
        /**
         * 放大操作
         */
        zoomIn: PropTypes.string,
        /**
         * 左移操作
         */
        moveLeft: PropTypes.string,
        /**
         * 右移操作
         */
        moveRight: PropTypes.string,
        /**
         * 上移操作
         */
        moveUp: PropTypes.string,
        /**
         * 下移操作
         */
        moveDown: PropTypes.string,
        /**
         * 下载操作
         */
        download: PropTypes.string,
        /**
         * 全屏操作
         */
        fullscreen: PropTypes.string,
        /**
         * 资源加载失败
         */
        loadError: PropTypes.string,
        /**
         * 自动旋转调节
         */
        autorotate: PropTypes.string
    }),

    /**
     * 是否渲染底部导航栏隐藏按钮
     * 默认值：`false`
     */
    hideNavbarButton: PropTypes.bool,

    /**
     * 用于配置额外插件功能
     */
    plugins: PropTypes.arrayOf(
        PropTypes.shape({
            /**
             * 必填，插件类型，可选项有`'Autorotate'`
             */
            type: PropTypes.oneOf(['Autorotate']).isRequired,
            /**
             * `Autorotate`模式下，从用户无操作到恢复自动旋转的延时，单位：毫秒
             * 默认值：`2000`
             */
            autostartDelay: PropTypes.number,
            /**
             * `Autorotate`模式下，是否在用户无操作一段时间后恢复自动旋转
             * 默认值：`true`
             */
            autostartOnIdle: PropTypes.bool,
            /**
             * `Autorotate`模式下，自动旋转速度
             * 默认值：`2rpm`
             */
            autorotateSpeed: PropTypes.string
        })
    ),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyPhotoSphereViewer;

export const propTypes = FefferyPhotoSphereViewer.propTypes;
export const defaultProps = FefferyPhotoSphereViewer.defaultProps;