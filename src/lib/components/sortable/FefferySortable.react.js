import React, { Suspense } from "react";
import PropTypes from 'prop-types';

const LazyFefferySortable = React.lazy(() => import(/* webpackChunkName: "feffery_sortable" */ '../../fragments/sortable/FefferySortable.react'));

const FefferySortable = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferySortable {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferySortable.propTypes = {
    /**
     * 组件id
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

    /**
     * 强制刷新用
     */
    key: PropTypes.string,

    /**
     * 必填参数，用于定义子项源数组，数组顺序不会受拖拽排序结果影响
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
     * 限制横向拖拽最大像素偏移距离，默认无限制
     */
    maxTranslateX: PropTypes.number,

    /**
     * 限制纵向拖拽最大像素偏移距离，默认无限制
     */
    maxTranslateY: PropTypes.number,

    /**
     * 监听或设置当前各子项呈现的顺序
     */
    currentOrder: PropTypes.arrayOf(
        PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ])
    ),

    // 子项点选相关功能
    /**
     * 设置或监听当前处于选中状态的子项key值
     */
    value: PropTypes.oneOfType([
        /**
         * 单选模式
         */
        PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
        /**
         * 多选模式
         */
        PropTypes.arrayOf(
            PropTypes.oneOfType([PropTypes.number, PropTypes.string])
        )
    ]),

    /**
     * 是否允许多选
     * 默认：false
     */
    multiple: PropTypes.bool,

    /**
     * 是否允许无选中项
     * 默认：true
     */
    allowNoValue: PropTypes.bool,

    /**
     * 针对已选中项设置额外的css样式
     */
    selectedStyle: PropTypes.object,

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
FefferySortable.defaultProps = {
    direction: 'vertical',
    itemDraggingScale: 1,
    handlePosition: 'end',
    handleType: 'holder',
    multiple: false,
    allowNoValue: true
}

export default React.memo(FefferySortable);

export const propTypes = FefferySortable.propTypes;
export const defaultProps = FefferySortable.defaultProps;