import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyGlobeBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_three" */ '../../fragments/animations/FefferyGlobeBackground.react'));

const FefferyGlobeBackground = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyGlobeBackground {...props} />
        </Suspense>
    );
}


// 定义参数或属性
FefferyGlobeBackground.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 设置内嵌元素内容
     */
    children: PropTypes.node,

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
     * 设置是否开启鼠标控制，默认为true
     */
    mouseControls: PropTypes.bool,

    /**
     * 设置是否开启触摸控制，默认为true
     */
    touchControls: PropTypes.bool,

    /**
     * 设置是否开启陀螺仪控制，默认为false
     */
    gyroControls: PropTypes.bool,

    /**
     * 设置最小高度，默认为200.00
     */
    minHeight: PropTypes.number,

    /**
     * 设置最小宽度，默认为200.00
     */
    minWidth: PropTypes.number,

    /**
     * 设置比例，默认为1.00
     */
    scale: PropTypes.number,

    /**
     * 设置移动端比例，默认为1.00
     */
    scaleMobile: PropTypes.number,

    /**
     * 设置背景颜色，默认为'#23153c'
     */
    backgroundColor: PropTypes.string,

    /**
     * 设置globe颜色，默认为'#ff3f81'
     */
    color: PropTypes.string,

    /**
     * 设置globe颜色2，默认为'#ffffff'
     */
    color2: PropTypes.string,

    /**
     * 设置globe大小，范围0.5到2，默认为1
     */
    size: PropTypes.number,

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
FefferyGlobeBackground.defaultProps = {
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.00,
    scaleMobile: 1.00,
    backgroundColor: '#23153c',
    color: '#ff3f81',
    color2: '#ffffff',
    size: 1
}

export default FefferyGlobeBackground;

export const propTypes = FefferyGlobeBackground.propTypes;
export const defaultProps = FefferyGlobeBackground.defaultProps;