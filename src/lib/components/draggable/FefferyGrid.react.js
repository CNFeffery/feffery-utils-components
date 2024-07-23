import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyGrid = React.lazy(() => import(/* webpackChunkName: "feffery_grid" */ '../../fragments/draggable/FefferyGrid.react'));

const FefferyGrid = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyGrid {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyGrid.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 传入内部的各个FefferyGridItem元素
     */
    children: PropTypes.node,

    /**
     * 占位元素，用于在children为空时呈现相关提示信息
     */
    placeholder: PropTypes.node,

    /**
     * 强制刷新用
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
     * 设置网格容器固定像素高度
     */
    height: PropTypes.number,

    /**
     * 设置当前网格容器是否自使用内部元素而调整高度，默认为true
     */
    autoSize: PropTypes.bool,

    /**
     * 设置网格项的自动调整约束方向，默认无约束
     */
    compactType: PropTypes.oneOf(['vertical', 'horizontal']),

    /**
     * 用于设置当前网格容器内子元素之间的像素margin，格式：[x, y]
     * 也可以传入以断点为键的字典从而实现响应式
     */
    margin: PropTypes.oneOfType([
        PropTypes.arrayOf(PropTypes.number),
        // 响应式
        PropTypes.objectOf(
            PropTypes.arrayOf(PropTypes.number)
        )
    ]),

    /**
     * 用于设置当前网格容器内部像素padding，格式：[x, y]
     * 也可以传入以断点为键的字典从而实现响应式
     */
    containerPadding: PropTypes.oneOfType([
        PropTypes.arrayOf(PropTypes.number),
        // 响应式
        PropTypes.objectOf(
            PropTypes.arrayOf(PropTypes.number)
        )
    ]),

    /**
     * 用于设置网格中每行的像素高度，默认为150
     */
    rowHeight: PropTypes.number,

    /**
     * 设置是否开启当前网格内部的拖拽行为，默认为true
     */
    isDraggable: PropTypes.bool,

    /**
     * 设置是否开启当前网格内部的尺寸调整行为，默认为true
     */
    isResizable: PropTypes.bool,

    /**
     * 设置是否限制当前网格内部的拖拽行为仅限于内部，默认为false
     */
    isBounded: PropTypes.bool,

    /**
     * 设置是否允许相互压盖，默认为false
     */
    allowOverlap: PropTypes.bool,

    /**
     * 用于自定义断点及其对应的像素值映射对象
     * 默认为{lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0}
     */
    breakpoints: PropTypes.objectOf(PropTypes.number),

    /**
     * 与breakpoints对应，用于设置不同断点下网格系统的列数
     * 默认为{lg: 12, md: 10, sm: 6, xs: 4, xxs: 2}
     */
    cols: PropTypes.oneOfType([
        PropTypes.objectOf(PropTypes.number),
        /**
         * 通用模式
         */
        PropTypes.number
    ]),

    /**
     * 用于定义不同断点下的各个网格项布局相关参数
     */
    layouts: PropTypes.oneOfType([
        PropTypes.objectOf(
            PropTypes.arrayOf(
                PropTypes.exact({
                    /**
                     * 对应当前网格项的key值
                     */
                    i: PropTypes.string,
                    /**
                     * 对应当前网格项的锚点x单位坐标
                     */
                    x: PropTypes.number,
                    /**
                     * 对应当前网格项的锚点y单位坐标
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
                     * 对应当前网格项的最小网格单位宽度，默认为0
                     */
                    minW: PropTypes.number,
                    /**
                     * 对应当前网格项的最大网格单位宽度，默认无限制
                     */
                    maxW: PropTypes.number,
                    /**
                     * 对应当前网格项的最小网格单位高度，默认为0
                     */
                    minH: PropTypes.number,
                    /**
                     * 对应当前网格项的最大网格单位高度，默认无限制
                     */
                    maxH: PropTypes.number,
                    /**
                     * 设置当前网格项是否静态，默认为false
                     */
                    static: PropTypes.bool,
                    /**
                     * 设置当前网格项是否允许被拖拽，默认为true
                     */
                    isDraggable: PropTypes.bool,
                    /**
                     * 设置当前网格项是否允许被调整尺寸，默认为true
                     */
                    isResizable: PropTypes.bool,
                    /**
                     * 设置是否为当前网格项施加边界约束，默认为false
                     */
                    isBounded: PropTypes.bool,
                    moved: PropTypes.any
                })
            )
        ),
        // 通用模式
        PropTypes.arrayOf(
            PropTypes.exact({
                /**
                 * 对应当前网格项的key值
                 */
                i: PropTypes.string,
                /**
                 * 对应当前网格项的锚点x单位坐标
                 */
                x: PropTypes.number,
                /**
                 * 对应当前网格项的锚点y单位坐标
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
                 * 对应当前网格项的最小网格单位宽度，默认为0
                 */
                minW: PropTypes.number,
                /**
                 * 对应当前网格项的最大网格单位宽度，默认无限制
                 */
                maxW: PropTypes.number,
                /**
                 * 对应当前网格项的最小网格单位高度，默认为0
                 */
                minH: PropTypes.number,
                /**
                 * 对应当前网格项的最大网格单位高度，默认无限制
                 */
                maxH: PropTypes.number,
                /**
                 * 设置当前网格项是否静态，默认为false
                 */
                static: PropTypes.bool,
                /**
                 * 设置当前网格项是否允许被拖拽，默认为true
                 */
                isDraggable: PropTypes.bool,
                /**
                 * 设置当前网格项是否允许被调整尺寸，默认为true
                 */
                isResizable: PropTypes.bool,
                /**
                 * 设置是否为当前网格项施加边界约束，默认为false
                 */
                isBounded: PropTypes.bool,
                moved: PropTypes.any
            })
        ),
        PropTypes.any
    ]),

    /**
     * 自定义样式相关快捷样式参数
     * 自定义拖拽预览占位的background属性，默认为'#3b3a39'
     */
    placeholderBackground: PropTypes.string,

    /**
     * 自定义拖拽预览占位的opacity属性，默认为0.2
     */
    placeholderOpacity: PropTypes.number,

    /**
     * 自定义拖拽预览占位的border属性，默认为'none'
     */
    placeholderBorder: PropTypes.string,

    /**
     * 自定义拖拽预览占位的border-radius属性，默认为'0px'
     */
    placeholderBorderRadius: PropTypes.string,

    /**
     * 设置是否开启debug模式，开启后，每次布局参数更新，都会在浏览器开发者工具控制台进行打印
     * 默认：false
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

// 设置默认参数
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