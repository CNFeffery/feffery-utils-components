import React, { Suspense } from "react";
import PropTypes from 'prop-types';

const LazyFefferySortableList = React.lazy(() => import(/* webpackChunkName: "feffery_sortable_list" */ '../../fragments/sortable/FefferySortableList.react'));

const FefferySortableList = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferySortableList {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferySortableList.propTypes = {
    /**
     * 部件id
     */
    id: PropTypes.string,

    /**
     * 组件css样式
     */
    style: PropTypes.object,

    /**
     * 拖拽手柄css样式
     */
    handleStyle: PropTypes.object,

    /**
     * 拖拽手柄css类
     */
    handleClassName: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 组件css类
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    key: PropTypes.string,

    /**
     * 必填参数，用于定义当前排序列表组件的各子元素
     */
    items: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 对应当前子元素的唯一标识
             */
            key: PropTypes.oneOfType([PropTypes.number, PropTypes.string]).isRequired,

            /**
             * 当前子元素内容
             */
            content: PropTypes.node,

            /**
             * 当前子元素容器css样式
             */
            style: PropTypes.object,

            /**
             * 当前子元素容器css类
             */
            className: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.object
            ]),

            /**
             * 当前子元素处于拖拽中状态下的css样式
             */
            draggingStyle: PropTypes.object,

            /**
             * 当前子元素处于拖拽中状态下的css类
             */
            draggingClassName: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.object
            ])
        })
    ).isRequired,

    /**
     * 设置排序列表的方向，可选的有'vertical'和'horizontal'
     * 默认：'vertical'
     */
    direction: PropTypes.oneOf(['vertical', 'horizontal']),

    /**
     * 设置子项处于拖拽中状态下的缩放比例，默认为1即不缩放
     */
    itemDraggingScale: PropTypes.number,

    /**
     * 设置拖拽手柄位置，默认为'end'
     */
    handlePosition: PropTypes.oneOf(['start', 'end']),

    /**
     * 设置内置的推拽手柄图标类型，默认为'holder'
     */
    handleType: PropTypes.oneOf(['holder', 'menu', 'drag']),

    /**
     * 监听当前items顺序对应的子项id数组
     */
    currentOrder: PropTypes.arrayOf(
        PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ])
    ),

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
FefferySortableList.defaultProps = {
    direction: 'vertical',
    itemDraggingScale: 1,
    handlePosition: 'end',
    handleType: 'holder'
}

export default React.memo(FefferySortableList);

export const propTypes = FefferySortableList.propTypes;
export const defaultProps = FefferySortableList.defaultProps;