import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyTrunkBackground = React.lazy(() => import(/* webpackChunkName: "feffery_animated_3d_background_p5" */ '../../fragments/animations/FefferyTrunkBackground.react'));

/**
 * 3D-Trunk背景组件FefferyTrunkBackground
 */
const FefferyTrunkBackground = ({
    mouseControls = true,
    touchControls = true,
    gyroControls = false,
    minHeight = 200.00,
    minWidth = 200.00,
    scale = 1.00,
    scaleMobile = 1.00,
    backgroundColor = '#222426',
    color = '#98465f',
    spacing = 0,
    chaos = 1,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyTrunkBackground {
                ...{
                    mouseControls,
                    touchControls,
                    gyroControls,
                    minHeight,
                    minWidth,
                    scale,
                    scaleMobile,
                    backgroundColor,
                    color,
                    spacing,
                    chaos,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyTrunkBackground.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，设置内嵌元素内容
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名，支持[动态css](/advanced-classname)
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 设置是否开启鼠标控制
     * 默认为`true`
     */
    mouseControls: PropTypes.bool,

    /**
     * 设置是否开启触摸控制
     * 默认为`true`
     */
    touchControls: PropTypes.bool,

    /**
     * 设置是否开启陀螺仪控制
     * 默认为`false`
     */
    gyroControls: PropTypes.bool,

    /**
     * 设置最小高度
     * 默认为`200.00`
     */
    minHeight: PropTypes.number,

    /**
     * 设置最小宽度
     * 默认为`200.00`
     */
    minWidth: PropTypes.number,

    /**
     * 设置比例
     * 默认为`1.00`
     */
    scale: PropTypes.number,

    /**
     * 设置移动端比例
     * 默认为`1.00`
     */
    scaleMobile: PropTypes.number,

    /**
     * 设置背景颜色
     * 默认为`'#222426'`
     */
    backgroundColor: PropTypes.string,

    /**
     * 设置`trunk`颜色
     * 默认为`'#98465f'`
     */
    color: PropTypes.string,

    /**
     * 设置trunk间距，范围`0`到`10`
     * 默认为`0`
     */
    spacing: PropTypes.number,

    /**
     * 设置`trunk`混乱程度，范围`0`到`10`
     * 默认为`1`
     */
    chaos: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyTrunkBackground;

export const propTypes = FefferyTrunkBackground.propTypes;
export const defaultProps = FefferyTrunkBackground.defaultProps;