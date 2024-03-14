import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyRND = React.lazy(() => import(/* webpackChunkName: "feffery_rnd" */ '../../fragments/draggable/FefferyRND.react'));

const FefferyRND = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyRND {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyRND.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 强制刷新用
     */
    key: PropTypes.string,

    /**
     * css样式
     */
    style: PropTypes.object,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * 内部元素
     */
    children: PropTypes.node,

    /**
     * 设置默认位置及尺寸信息
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
         * 宽度值，数值型表示像素宽度，字符型与css相关属性值格式兼容，如'300px'、'50%'等
         */
        width: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ]),
        /**
         * 高度值，数值型表示像素高度，字符型与css相关属性值格式兼容，如'300px'、'50%'等
         */
        height: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ])
    }),

    /**
     * 设置或监听当前组件尺寸信息
     */
    size: PropTypes.exact({
        /**
         * 宽度值，数值型表示像素宽度，字符型与css相关属性值格式兼容，如'300px'、'50%'等
         */
        width: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ]),
        /**
         * 高度值，数值型表示像素高度，字符型与css相关属性值格式兼容，如'300px'、'50%'等
         */
        height: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ])
    }),

    /**
     * 设置或监听当前组件位置信息
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
     * 限制可调宽度下限，数值型表示像素宽度，字符型与css相关属性值格式兼容，如'300px'、'50%'等
     */
    minWidth: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 限制可调高度下限，数值型表示像素宽度，字符型与css相关属性值格式兼容，如'300px'、'50%'等
     */
    minHeight: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 限制可调宽度上限，数值型表示像素宽度，字符型与css相关属性值格式兼容，如'300px'、'50%'等
     */
    maxWidth: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 限制可调高度上限，数值型表示像素宽度，字符型与css相关属性值格式兼容，如'300px'、'50%'等
     */
    maxHeight: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 针对尺寸调整行为，设置水平和竖直方向上调整的像素步长，格式为：[水平像素步长, 竖直像素步长]
     * 默认：[1, 1]
     */
    resizeGrid: PropTypes.arrayOf(PropTypes.number),

    /**
     * 针对位置拖拽行为，设置水平和竖直方向上拖拽的像素步长，格式为：[水平像素步长, 竖直像素步长]
     * 默认：[1, 1]
     */
    dragGrid: PropTypes.arrayOf(PropTypes.number),

    /**
     * 配置高宽比锁定
     * 传入true时，将锁定初始尺寸对应高宽比
     * 传入数值型时，用于指定具体的高宽比
     * 默认：false
     */
    lockAspectRatio: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.number
    ]),

    /**
     * 在lockAspectRatio基础上，设置额外像素宽度
     * 默认：0
     */
    lockAspectRatioExtraWidth: PropTypes.number,

    /**
     * 在lockAspectRatio基础上，设置额外像素高度
     * 默认：0
     */
    lockAspectRatioExtraHeight: PropTypes.number,

    /**
     * 设置允许进行尺寸调整的方向，多选，可选项有'top'、'right'、'bottom'、'left'、'topRight'、'bottomRight'、'bottomLeft'、'topLeft'
     * 默认为['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft']
     */
    direction: PropTypes.arrayOf(
        PropTypes.oneOf(['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft'])
    ),

    /**
     * 是否禁用拖拽功能
     */
    disableDragging: PropTypes.bool,

    /**
     * 允许进行拖拽的方向，可选的有'x'、'y'、'both'、'none'
     */
    dragAxis: PropTypes.oneOf(['x', 'y', 'both', 'none']),

    /**
     * 设置当前组件尺寸调整及拖拽的外边界类型，可选的有'window'、'parent'
     * 默认为'window'
     */
    bounds: PropTypes.oneOf(['window', 'parent']),

    /**
     * 设置或监听当前组件是否处于选择状态
     * 默认：false
     */
    selected: PropTypes.bool,

    /**
     * 设置当前组件在选中状态下的css样式
     */
    selectedStyle: PropTypes.object,

    /**
     * 配置当前组件在选中状态下的css类名
     */
    selectedClassName: PropTypes.string,

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
FefferyRND.defaultProps = {
    direction: ['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft'],
    selected: false
}

export default FefferyRND;

export const propTypes = FefferyRND.propTypes;
export const defaultProps = FefferyRND.defaultProps;