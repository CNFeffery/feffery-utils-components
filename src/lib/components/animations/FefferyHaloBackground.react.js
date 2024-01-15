import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyHaloBackground = React.lazy(() => import(/* webpackChunkName: "feffery_halo_background" */ '../../fragments/animations/FefferyHaloBackground.react'));

const FefferyHaloBackground = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyHaloBackground {...props} />
        </Suspense>
    );
}


// 定义参数或属性
FefferyHaloBackground.propTypes = {
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
     * 设置背景颜色，默认为'#131a43'
     */
    backgroundColor: PropTypes.string,

    /**
     * 设置基本颜色，默认为'#112966'
     */
    baseColor: PropTypes.string,

    /**
     * 设置动画大小，范围0.1到3，默认为1
     */
    size: PropTypes.number,

    /**
     * 设置动画振幅因子，范围0到3，默认为1
     */
    amplitudeFactor: PropTypes.number,

    /**
     * 设置x轴偏移量，范围为-0.5到0.5，默认为0
     */
    xOffset: PropTypes.number,

    /**
     * 设置y轴偏移量，范围为-0.5到0.5，默认为0
     */
    yOffset: PropTypes.number,

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
FefferyHaloBackground.defaultProps = {
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    backgroundColor: '#131a43',
    baseColor: '#112966',
    size: 1,
    amplitudeFactor: 1,
    xOffset: 0,
    yOffset: 0
}

export default FefferyHaloBackground;

export const propTypes = FefferyHaloBackground.propTypes;
export const defaultProps = FefferyHaloBackground.defaultProps;