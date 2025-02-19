import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyRND = React.lazy(() => import(/* webpackChunkName: "feffery_rnd" */ '../../fragments/draggable/FefferyRND.react'));

/**
 * 尺寸可调可拖拽组件FefferyRND
 */
const FefferyRND = ({
    direction = ['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft'],
    selected = false,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyRND {
                ...{
                    direction,
                    selected,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyRND.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，内嵌元素
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 设置默认位置及尺寸状态
     */
    defaultState: PropTypes.exact({
        /**
         * 水平方向像素位置
         */
        x: PropTypes.number,
        /**
         * 竖直方向像素位置
         */
        y: PropTypes.number,
        /**
         * 宽度值，数值型表示像素宽度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等
         */
        width: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ]),
        /**
         * 高度值，数值型表示像素高度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等
         */
        height: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ])
    }),

    /**
     * 设置或监听当前组件尺寸状态
     */
    size: PropTypes.exact({
        /**
         * 宽度值，数值型表示像素宽度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等
         */
        width: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ]),
        /**
         * 高度值，数值型表示像素高度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等
         */
        height: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ])
    }),

    /**
     * 设置或监听当前组件位置状态
     */
    position: PropTypes.exact({
        /**
         * 水平方向像素位置
         */
        x: PropTypes.number,
        /**
         * 竖直方向像素位置
         */
        y: PropTypes.number
    }),

    /**
     * 限制可调宽度下限，数值型表示像素宽度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等
     */
    minWidth: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 限制可调高度下限，数值型表示像素宽度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等
     */
    minHeight: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 限制可调宽度上限，数值型表示像素宽度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等
     */
    maxWidth: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 限制可调高度上限，数值型表示像素宽度，字符型与`css`相关属性值格式兼容，如'300px'、'50%'等
     */
    maxHeight: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 针对尺寸调整行为，设置水平和竖直方向上调整的像素步长，格式：`[水平像素步长, 竖直像素步长]`
     * 默认值：`[1, 1]`
     */
    resizeGrid: PropTypes.arrayOf(PropTypes.number),

    /**
     * 针对位置拖拽行为，设置水平和竖直方向上拖拽的像素步长，格式：`[水平像素步长, 竖直像素步长]`
     * 默认值：`[1, 1]`
     */
    dragGrid: PropTypes.arrayOf(PropTypes.number),

    /**
     * 配置高宽比锁定，传入`true`时，将锁定初始尺寸对应高宽比，传入数值型时，用于指定具体的高宽比
     * 默认值：`false`
     */
    lockAspectRatio: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.number
    ]),

    /**
     * 在`lockAspectRatio`基础上，设置额外像素宽度
     * 默认值：`0`
     */
    lockAspectRatioExtraWidth: PropTypes.number,

    /**
     * 在`lockAspectRatio`基础上，设置额外像素高度
     * 默认值：`0`
     */
    lockAspectRatioExtraHeight: PropTypes.number,

    /**
     * 允许进行尺寸调整的方向，可多选，可选项有`'top'`、`'right'`、`'bottom'`、`'left'`、`'topRight'`、`'bottomRight'`、`'bottomLeft'`、`'topLeft'`
     * 默认值：`['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft']`
     */
    direction: PropTypes.arrayOf(
        PropTypes.oneOf(['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft'])
    ),

    /**
     * 是否禁用拖拽功能
     */
    disableDragging: PropTypes.bool,

    /**
     * 允许进行拖拽的方向，可选项有`'x'`、`'y'`、`'both'`、`'none'`
     */
    dragAxis: PropTypes.oneOf(['x', 'y', 'both', 'none']),

    /**
     * 设置当前组件尺寸调整及拖拽的外边界类型，可选项有`'window'`、`'parent'`
     * 默认值：`'window'`
     */
    bounds: PropTypes.oneOf(['window', 'parent']),

    /**
     * 设置或监听当前组件是否处于选择状态
     * 默认值：`false`
     */
    selected: PropTypes.bool,

    /**
     * 设置当前组件在选中状态下的`css`样式
     */
    selectedStyle: PropTypes.object,

    /**
     * 配置当前组件在选中状态下的`css`类名
     */
    selectedClassName: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyRND;

export const propTypes = FefferyRND.propTypes;
export const defaultProps = FefferyRND.defaultProps;