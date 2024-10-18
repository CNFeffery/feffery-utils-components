import React, { Suspense } from "react";
import PropTypes from 'prop-types';

const LazyFefferySortable = React.lazy(() => import(/* webpackChunkName: "feffery_sortable" */ '../../fragments/draggable/FefferySortable.react'));

/**
 * 排序列表组件FefferySortable
 */
const FefferySortable = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferySortable {...props} />
        </Suspense>
    );
}

FefferySortable.propTypes = {
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
     * 拖拽手柄css样式
     */
    handleStyle: PropTypes.object,

    /**
     * 拖拽手柄css类名
     */
    handleClassName: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 当前组件css类名
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 必填，定义子项源数组，数组顺序不会受拖拽排序结果影响
     */
    items: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 对应当前子元素唯一标识
             */
            key: PropTypes.oneOfType([PropTypes.number, PropTypes.string]).isRequired,

            /**
             * 当前子元素内容
             */
            content: PropTypes.node,

            /**
             * 当前子元素容器`css`样式
             */
            style: PropTypes.object,

            /**
             * 当前子元素容器`css`类名
             */
            className: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.object
            ]),

            /**
             * 当前子元素处于拖拽中状态下的`css`样式
             */
            draggingStyle: PropTypes.object,

            /**
             * 当前子元素处于拖拽中状态下的`css`类名
             */
            draggingClassName: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.object
            ])
        })
    ).isRequired,

    /**
     * 排序列表方向，可选项有`'vertical'`、`'horizontal'`
     * 默认值：`'vertical'`
     */
    direction: PropTypes.oneOf(['vertical', 'horizontal']),

    /**
     * 设置子项处于拖拽中状态下的缩放比例
     * 默认值：`1`
     */
    itemDraggingScale: PropTypes.number,

    /**
     * 设置拖拽手柄位置，可选项有`'start'`、`'end'`
     * 默认值：`'end'`
     */
    handlePosition: PropTypes.oneOf(['start', 'end']),

    /**
     * 设置内置的推拽手柄图标类型，可选项有`'holder'`、`'menu'`、`'drag'`
     * 默认值：`'holder'`
     */
    handleType: PropTypes.oneOf(['holder', 'menu', 'drag']),

    /**
     * 限制横向拖拽最大像素偏移距离
     */
    maxTranslateX: PropTypes.number,

    /**
     * 限制纵向拖拽最大像素偏移距离
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

    /**
     * 设置或监听当前处于选中状态的子项`key`值
     */
    value: PropTypes.oneOfType([
        PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
        PropTypes.arrayOf(
            PropTypes.oneOfType([PropTypes.number, PropTypes.string])
        )
    ]),

    /**
     * 是否允许多选
     * 默认值：`false`
     */
    multiple: PropTypes.bool,

    /**
     * 是否允许无选中项
     * 默认值：`true`
     */
    allowNoValue: PropTypes.bool,

    /**
     * 针对已选中项设置额外的`css`样式
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