import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyCellsBackground = React.lazy(() => import(/* webpackChunkName: "feffery_cells_background" */ '../../fragments/animations/FefferyCellsBackground.react'));

const FefferyCellsBackground = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyCellsBackground {...props} />
        </Suspense>
    );
}


// 定义参数或属性
FefferyCellsBackground.propTypes = {
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
     * 设置cells颜色1，默认为'#109090'
     */
    color1: PropTypes.string,

    /**
     * 设置cells颜色2，默认为'#f2e735'
     */
    color2: PropTypes.string,

    /**
     * 设置cells大小，范围0.2到5，默认为1.5
     */
    size: PropTypes.number,

    /**
     * 设置cells动画速度，范围0到5，默认为1
     */
    speed: PropTypes.number,

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
FefferyCellsBackground.defaultProps = {
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.00,
    color1: '#109090',
    color2: '#f2e735',
    size: 1.5,
    speed: 1
}

export default FefferyCellsBackground;

export const propTypes = FefferyCellsBackground.propTypes;
export const defaultProps = FefferyCellsBackground.defaultProps;