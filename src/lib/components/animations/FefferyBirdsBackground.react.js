import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyBirdsBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_three" */ '../../fragments/animations/FefferyBirdsBackground.react'));

const FefferyBirdsBackground = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyBirdsBackground {...props} />
        </Suspense>
    );
}


// 定义参数或属性
FefferyBirdsBackground.propTypes = {
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
     * 设置背景颜色，默认为'#000000'
     */
    backgroundColor: PropTypes.string,

    /**
     * 设置背景颜色透明度，范围0到1，默认为1
     */
    backgroundAlpha: PropTypes.number,

    /**
     * 设置birds颜色1，默认为'#ff0000'
     */
    color1: PropTypes.string,

    /**
     * 设置birds颜色2，默认为'#13becf'
     */
    color2: PropTypes.string,

    /**
     * 设置颜色模式，可选的有'lerp', 'variance', 'lerpGradient', 'varianceGradient'
     * 默认为'varianceGradient'
     */
    colorMode: PropTypes.oneOf(['lerp', 'variance', 'lerpGradient', 'varianceGradient']),

    /**
     * 设置背景质量，范围1到5，默认为5
     */
    quantity: PropTypes.number,

    /**
     * 设置birds大小，范围1到4，默认为1
     */
    birdSize: PropTypes.number,

    /**
     * 设置birds翼展，范围10到40，默认为30
     */
    wingSpan: PropTypes.number,

    /**
     * 设置birds速度限制，范围1到10，默认为5
     */
    speedLimit: PropTypes.number,

    /**
     * 设置birds分离大小，范围1到100，默认为20
     */
    separation: PropTypes.number,

    /**
     * 设置birds对齐大小，范围1到100，默认为20
     */
    alignment: PropTypes.number,

    /**
     * 设置birds内聚大小，范围1到100，默认为20
     */
    cohesion: PropTypes.number,

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
FefferyBirdsBackground.defaultProps = {
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.00,
    scaleMobile: 1.00,
    backgroundColor: '#000000',
    backgroundAlpha: 1,
    color1: '#ff0000',
    color2: '#13becf',
    colorMode: 'varianceGradient',
    quantity: 5,
    birdSize: 1,
    wingSpan: 30,
    speedLimit: 5,
    separation: 20,
    alignment: 20,
    cohesion: 20
}

export default FefferyBirdsBackground;

export const propTypes = FefferyBirdsBackground.propTypes;
export const defaultProps = FefferyBirdsBackground.defaultProps;