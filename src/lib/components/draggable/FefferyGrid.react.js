import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyGrid = React.lazy(() => import(/* webpackChunkName: "feffery_grid" */ '../../fragments/draggable/FefferyGrid.react'));

/**
 * 可拖拽网格组件FefferyGrid
 */
const FefferyGrid = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyGrid {...props} />
        </Suspense>
    );
}

FefferyGrid.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 传入内部的各`FefferyGridItem`组件
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
     * 组件型，占位元素，用于在`children`为空时呈现相关提示信息
     */
    placeholder: PropTypes.node,

    /**
     * 网格容器固定像素高度
     */
    height: PropTypes.number,

    /**
     * 当前网格容器是否受内部元素影响调整高度
     * 默认值：`true`
     */
    autoSize: PropTypes.bool,

    /**
     * 网格项自动调整约束方向，可选项有`'vertical'`、`'horizontal'`
     * 默认值：`'vertical'`
     */
    compactType: PropTypes.oneOf(['vertical', 'horizontal']),

    /**
     * 网格容器内子元素之间的像素间距，格式：`[水平间距, 竖直间距]`，也可以传入以断点为键的字典从而实现响应式
     * 默认值：`[10, 10]`
     */
    margin: PropTypes.oneOfType([
        PropTypes.arrayOf(PropTypes.number),
        // 响应式
        PropTypes.objectOf(
            PropTypes.arrayOf(PropTypes.number)
        )
    ]),

    /**
     * 用于设置当前网格容器内部像素padding，格式：[x, y]，支持响应式
     */
    containerPadding: PropTypes.oneOfType([
        PropTypes.arrayOf(PropTypes.number),
        PropTypes.objectOf(
            PropTypes.arrayOf(PropTypes.number)
        )
    ]),

    /**
     * 网格中每行像素高度
     * 默认值：`150`
     */
    rowHeight: PropTypes.number,

    /**
     * 内部网格项是否可拖拽
     * 默认值：`true`
     */
    isDraggable: PropTypes.bool,

    /**
     * 内部网格项尺寸是否可调整
     * 默认值：`true`
     */
    isResizable: PropTypes.bool,

    /**
     * 是否允许内部网格项拖拽出界
     * 默认值：`false`
     */
    isBounded: PropTypes.bool,

    /**
     * 是否允许内部网格项重叠
     * 默认值：`false`
     */
    allowOverlap: PropTypes.bool,

    /**
     * 自定义断点键及对应断点像素宽度值
     * 默认值：`{lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0}`
     */
    breakpoints: PropTypes.objectOf(PropTypes.number),

    /**
     * 与`breakpoints`对应，设置不同断点下网格系统的列数
     * 默认值：`12`
     */
    cols: PropTypes.oneOfType([
        PropTypes.objectOf(PropTypes.number),
        PropTypes.number
    ]),

    /**
     * 配置各网格项
     */
    layouts: PropTypes.oneOfType([
        PropTypes.objectOf(
            PropTypes.arrayOf(
                PropTypes.shape({
                    /**
                     * 对应当前网格项的`key`值
                     */
                    i: PropTypes.string,
                    /**
                     * 对应当前网格项的锚点`x`单位坐标
                     */
                    x: PropTypes.number,
                    /**
                     * 对应当前网格项的锚点`y`单位坐标
                     */
                    y: PropTypes.number,
                    /**
                     * 对应当前网格项的网格单位宽度
                     */
                    w: PropTypes.number,
                    /**
                     * 对应当前网格项的网格单位高度
                     */
                    h: PropTypes.number,
                    /**
                     * 对应当前网格项的最小网格单位宽度
                     * 默认值：`0`
                     */
                    minW: PropTypes.number,
                    /**
                     * 对应当前网格项的最大网格单位宽度，默认无限制
                     */
                    maxW: PropTypes.number,
                    /**
                     * 对应当前网格项的最小网格单位高度
                     * 默认值：`0`
                     */
                    minH: PropTypes.number,
                    /**
                     * 对应当前网格项的最大网格单位高度，默认无限制
                     */
                    maxH: PropTypes.number,
                    /**
                     * 设置当前网格项是否静态
                     * 默认值：`false`
                     */
                    static: PropTypes.bool,
                    /**
                     * 设置当前网格项是否允许被拖拽
                     * 默认值：`true`
                     */
                    isDraggable: PropTypes.bool,
                    /**
                     * 设置当前网格项是否允许被调整尺寸
                     * 默认值：`true`
                     */
                    isResizable: PropTypes.bool,
                    /**
                     * 设置是否为当前网格项施加边界约束
                     * 默认值：`false`
                     */
                    isBounded: PropTypes.bool
                })
            )
        ),
        PropTypes.arrayOf(
            PropTypes.shape({
                /**
                 * 对应当前网格项的`key`值
                 */
                i: PropTypes.string,
                /**
                 * 对应当前网格项的锚点`x`单位坐标
                 */
                x: PropTypes.number,
                /**
                 * 对应当前网格项的锚点`y`单位坐标
                 */
                y: PropTypes.number,
                /**
                 * 对应当前网格项的网格单位宽度
                 */
                w: PropTypes.number,
                /**
                 * 对应当前网格项的网格单位高度
                 */
                h: PropTypes.number,
                /**
                 * 对应当前网格项的最小网格单位宽度
                 * 默认值：`0`
                 */
                minW: PropTypes.number,
                /**
                 * 对应当前网格项的最大网格单位宽度，默认无限制
                 */
                maxW: PropTypes.number,
                /**
                 * 对应当前网格项的最小网格单位高度
                 * 默认值：`0`
                 */
                minH: PropTypes.number,
                /**
                 * 对应当前网格项的最大网格单位高度，默认无限制
                 */
                maxH: PropTypes.number,
                /**
                 * 设置当前网格项是否静态
                 * 默认值：`false`
                 */
                static: PropTypes.bool,
                /**
                 * 设置当前网格项是否允许被拖拽
                 * 默认值：`true`
                 */
                isDraggable: PropTypes.bool,
                /**
                 * 设置当前网格项是否允许被调整尺寸
                 * 默认值：`true`
                 */
                isResizable: PropTypes.bool,
                /**
                 * 设置是否为当前网格项施加边界约束
                 * 默认值：`false`
                 */
                isBounded: PropTypes.bool
            })
        ),
        PropTypes.any
    ]),

    /**
     * 拖拽预览占位对应`css`的`background`属性
     * 默认值：`'#3b3a39'`
     */
    placeholderBackground: PropTypes.string,

    /**
     * 拖拽预览占位对应`css`的`opacity`属性
     * 默认值：`0.2`
     */
    placeholderOpacity: PropTypes.number,

    /**
     * 拖拽预览占位对应`css`的`border`属性
     * 默认值：`'none'`
     */
    placeholderBorder: PropTypes.string,

    /**
     * 拖拽预览占位对应`css`的`border-radius`属性
     * 默认值：`'0px'`
     */
    placeholderBorderRadius: PropTypes.string,

    /**
     * 是否开启调试模式，开启后，每次布局参数更新，都会在浏览器开发者工具控制台打印相关参数
     * 默认值：`false`
     */
    debug: PropTypes.bool,

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
    setProps: PropTypes.func
};

FefferyGrid.defaultProps = {
    autoSize: true,
    cols: 12,
    compactType: 'vertical',
    margin: [10, 10],
    rowHeight: 150,
    isDraggable: true,
    isResizable: true,
    isBounded: false,
    allowOverlap: false,
    placeholderBackground: '#3b3a39',
    placeholderOpacity: 0.2,
    placeholderBorder: 'none',
    placeholderBorderRadius: '0px',
    breakpoints: { lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0 },
    compactType: 'vertical',
    debug: false
}

export default FefferyGrid;

export const propTypes = FefferyGrid.propTypes;
export const defaultProps = FefferyGrid.defaultProps;