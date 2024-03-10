import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyAnimatedImage = React.lazy(() => import(/* webpackChunkName: "feffery_animated_image" */ '../fragments/FefferyAnimatedImage.react'));

const FefferyAnimatedImage = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyAnimatedImage {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyAnimatedImage.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 强制刷新用
     */
    key: PropTypes.string,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * 自定义css字典
     */
    style: PropTypes.object,

    /**
     * 必填，定义动图资源地址
     */
    src: PropTypes.string.isRequired,

    /**
     * 动图alt信息
     */
    alt: PropTypes.string,

    /**
     * 初始化是否自动播放动图
     * 默认：false
     */
    play: PropTypes.bool,

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
    setProps: PropTypes.func
};

// 设置默认参数
FefferyAnimatedImage.defaultProps = {
    play: false
}

export default FefferyAnimatedImage;

export const propTypes = FefferyAnimatedImage.propTypes;
export const defaultProps = FefferyAnimatedImage.defaultProps;