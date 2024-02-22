import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyResizable = React.lazy(() => import(/* webpackChunkName: "feffery_resizable" */ '../../fragments/resizable/FefferyResizable.react'));

const FefferyResizable = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyResizable {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyResizable.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    key: PropTypes.string,

    /**
     * 设置内部嵌套的子元素
     */
    children: PropTypes.node,

    /**
     * 设置css类名
     */
    className: PropTypes.string,

    /**
     * 设置css样式
     */
    style: PropTypes.object,

    /**
     * 设置尺寸调整组件初始化时的宽度、高度，可传入如300、'300px'、'50%'、'50vh'等形式
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
     * 监听或设置尺寸调整组件的宽度、高度，可传入如300、'300px'、'50%'、'50vh'等形式
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
     * 设置尺寸调整组件的最小宽度，默认为10
     */
    minWidth: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    /**
     * 设置尺寸调整组件的最小高度，默认为10
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
     * 设置允许进行尺寸调整的方向，多选，可选项有'top'、'right'、'bottom'、'left'、'topRight'、'bottomRight'、'bottomLeft'、'topLeft'
     * 默认为['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft']
     */
    direction: PropTypes.arrayOf(
        PropTypes.oneOf(['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft'])
    ),

    /**
     * 设置尺寸调整在水平和竖直方向上的最小调整像素步长，默认为[1, 1]
     */
    grid: PropTypes.arrayOf(PropTypes.number),

    /**
     * 设置尺寸调整组件的外边界类型，可选的有'window'、'parent'
     * 默认为'window'
     */
    bounds: PropTypes.oneOf(['window', 'parent']),

    /**
     * 用于指定边界元素的css选择器，优先级高于bounds
     */
    boundsSelector: PropTypes.string,

    /**
     * 用于分别设置不同方向上拖拽控件部分的css样式
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
     * 用于分别设置不同方向上拖拽控件部分的css类名
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
FefferyResizable.defaultProps = {
    direction: ['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft'],
    minWidth: 10,
    minHeight: 10,
    grid: [1, 1],
    bounds: 'window'
}

export default FefferyResizable;

export const propTypes = FefferyResizable.propTypes;
export const defaultProps = FefferyResizable.defaultProps;