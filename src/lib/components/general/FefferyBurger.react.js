import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyBurger = React.lazy(() => import(/* webpackChunkName: "feffery_burger" */ '../../fragments/general/FefferyBurger.react'));

/**
 * 动态菜单图标组件FefferyBurger
 */
const FefferyBurger = ({
    id,
    className,
    style,
    type = 'default',
    toggled,
    size = 32,
    direction = 'left',
    duration = 0.3,
    distance = 'md',
    color,
    rounded = false,
    setProps,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyBurger {
                ...{
                    id,
                    className,
                    style,
                    type,
                    toggled,
                    size,
                    direction,
                    duration,
                    distance,
                    color,
                    rounded,
                    setProps,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyBurger.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 图标类型，可选项有`'default'`、`'squash'`、`'cross'`、`'twirl'`、`'fade'`、`'slant'`、`'spiral'` 、`'divide'`、`'turn'`、`'pivot'`、`'sling'`、`'squeeze'`、`'spin'`、`'rotate'`
     * 默认值：`'default'`
     */
    type: PropTypes.oneOf(['default', 'squash', 'cross', 'twirl', 'fade', 'slant', 'spiral', 'divide', 'turn', 'pivot', 'sling', 'squeeze', 'spin', 'rotate']),

    /**
     * 设置或监听图标状态
     */
    toggled: PropTypes.bool,

    /**
     * 图标像素尺寸
     * 默认值：`32`
     */
    size: PropTypes.number,

    /**
     * 部分类型图标可用，控制动画方向，可选项有`'left'`、`'right'`
     * 默认值：`'left'`
     */
    direction: PropTypes.oneOf(['left', 'right']),

    /**
     * 动画过程时长，单位：秒，设置为`0`时将关闭动画
     * 默认值：`0.3`
     */
    duration: PropTypes.number,

    /**
     * 图标水平线之间的间距大小规格，可选项有`'sm'`、`'md'`、`'lg'`
     * 默认值：`'md'`
     */
    distance: PropTypes.oneOf(['sm', 'md', 'lg']),

    /**
     * 图标颜色
     */
    color: PropTypes.string,

    /**
     * 是否渲染为圆角矩形
     * 默认值：`false`
     */
    rounded: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyBurger;

export const propTypes = FefferyBurger.propTypes;
export const defaultProps = FefferyBurger.defaultProps;