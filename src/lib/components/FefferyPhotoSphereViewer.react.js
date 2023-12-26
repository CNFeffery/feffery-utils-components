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
    littlePlanet: false
}

export default FefferyPhotoSphereViewer;

export const propTypes = FefferyPhotoSphereViewer.propTypes;
export const defaultProps = FefferyPhotoSphereViewer.defaultProps;