import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyResizable = React.lazy(() => import(/* webpackChunkName: "feffery_resizable" */ '../../fragments/resizable/FefferyResizable.react'));

/**
 * 尺寸调整组件FefferyResizable
 */
const FefferyResizable = ({
    direction = ['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft'],
    minWidth = 10,
    minHeight = 10,
    grid = [1, 1],
    bounds = 'window',
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyResizable {
                ...{
                    direction,
                    minWidth,
                    minHeight,
                    grid,
                    bounds,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyResizable.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，设置内部嵌套的子元素
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
     * 设置尺寸调整组件初始化时的宽度和高度，可传入如`300`、`'300px'`、`'50%'`、`'50vh'`等形式
     */
    defaultSize: PropTypes.exact({
        /**
         * 设置宽度
         */
        width: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ]),
        /**
         * 设置高度
         */
        height: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ])
    }),

    /**
     * 监听或设置尺寸调整组件的宽度和高度，可传入如`300`、`'300px'`、`'50%'`、`'50vh'`等形式
     */
    size: PropTypes.exact({
        /**
         * 设置宽度
         */
        width: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ]),
        /**
         * 设置高度
         */
        height: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ])
    }),

    /**
     * 设置尺寸调整组件的最小宽度
     * 默认值：`10`
     */
    minWidth: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 设置尺寸调整组件的最小高度
     * 默认值：`10`
     */
    minHeight: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 设置尺寸调整组件的最大宽度
     */
    maxWidth: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 设置尺寸调整组件的最大高度
     */
    maxHeight: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 设置允许进行尺寸调整的方向，多选，可选项有`'top'`、`'right'`、`'bottom'`、`'left'`、`'topRight'`、`'bottomRight'`、`'bottomLeft'`、`'topLeft'`
     * 默认值：`['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft']`
     */
    direction: PropTypes.arrayOf(
        PropTypes.oneOf(['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft'])
    ),

    /**
     * 设置尺寸调整在水平和竖直方向上的最小调整像素步长
     * 默认值：`[1, 1]`
     */
    grid: PropTypes.arrayOf(PropTypes.number),

    /**
     * 设置尺寸调整组件的外边界类型，可选的有`'window'`、`'parent'`
     * 默认值：`'window'`
     */
    bounds: PropTypes.oneOf(['window', 'parent']),

    /**
     * 用于指定边界元素的`css`选择器，优先级高于`bounds`
     */
    boundsSelector: PropTypes.string,

    /**
     * 用于分别设置不同方向上拖拽控件部分的`css`样式
     */
    handleStyles: PropTypes.exact({
        top: PropTypes.object,
        right: PropTypes.object,
        bottom: PropTypes.object,
        left: PropTypes.object,
        topRight: PropTypes.object,
        bottomRight: PropTypes.object,
        bottomLeft: PropTypes.object,
        topLeft: PropTypes.object
    }),

    /**
     * 用于分别设置不同方向上拖拽控件部分的`css`类名
     */
    handleClassNames: PropTypes.exact({
        top: PropTypes.string,
        right: PropTypes.string,
        bottom: PropTypes.string,
        left: PropTypes.string,
        topRight: PropTypes.string,
        bottomRight: PropTypes.string,
        bottomLeft: PropTypes.string,
        topLeft: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyResizable;

export const propTypes = FefferyResizable.propTypes;
export const defaultProps = FefferyResizable.defaultProps;