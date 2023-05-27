import { Resizable } from 're-resizable';
import PropTypes from 'prop-types';
import { clone } from 'lodash';

// 定义尺寸调整组件FefferyResizable
const FefferyResizable = (props) => {
    // 取得必要属性或参数
    const {
        id,
        key,
        children,
        className,
        style,
        defaultSize,
        minWidth,
        minHeight,
        maxWidth,
        maxHeight,
        direction,
        grid,
        bounds,
        handleStyles,
        handleClassNames,
        setProps,
        loading_state
    } = props;

    // 初始化enable
    const defaultEnable = {
        top: false,
        right: false,
        bottom: false,
        left: false,
        topRight: false,
        bottomRight: false,
        bottomLeft: false,
        topLeft: false
    }

    const enable = clone(defaultEnable);

    // 根据direction更新enable
    for (let d of direction) {
        enable[d] = true
    }

    return (
        <Resizable
            id={id}
            key={key}
            children={children}
            className={className}
            style={style}
            defaultSize={defaultSize}
            minWidth={minWidth}
            minHeight={minHeight}
            maxWidth={maxWidth}
            maxHeight={maxHeight}
            grid={grid}
            bounds={bounds}
            enable={enable}
            handleStyles={{
                ...handleStyles,
                top: {
                    cursor: "ns-resize",
                    ...handleStyles?.top
                },
                right: {
                    cursor: "ew-resize",
                    ...handleStyles?.right
                },
                bottom: {
                    cursor: "ns-resize",
                    ...handleStyles?.bottom
                },
                left: {
                    cursor: "ew-resize",
                    ...handleStyles?.left
                }
            }}
            handleClasses={handleClassNames}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >
            {children}
        </Resizable>
    );
}

// 定义参数或属性
FefferyResizable.propTypes = {
    // 部件id
    id: PropTypes.string,

    key: PropTypes.string,

    // 设置内部嵌套的子元素
    children: PropTypes.node,

    //设置css类名
    className: PropTypes.string,

    // 设置css样式
    style: PropTypes.object,

    // 监听或设置尺寸调整组件初始化时的宽度、高度，可传入如300、'300px'、'50%'、'50vh'等形式
    defaultSize: PropTypes.exact({
        // 设置宽度
        width: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ]),
        // 设置高度
        height: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ])
    }),

    // 设置尺寸调整组件的最小宽度，默认为10
    minWidth: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    // 设置尺寸调整组件的最小高度，默认为10
    minHeight: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    // 设置尺寸调整组件的最大宽度
    maxWidth: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    // 设置尺寸调整组件的最大高度
    maxHeight: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    // 设置允许进行尺寸调整的方向，多选，可选项有'top'、'right'、'bottom'、'left'、'topRight'、'bottomRight'、'bottomLeft'、'topLeft'
    // 默认为['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft']
    direction: PropTypes.arrayOf(
        PropTypes.oneOf(['top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft'])
    ),

    // 设置尺寸调整在水平和竖直方向上的最小调整像素步长，默认为[1, 1]
    grid: PropTypes.arrayOf(PropTypes.number),

    // 设置尺寸调整组件的外边界类型，可选的有'window'、'parent'
    // 默认为'window'
    bounds: PropTypes.oneOf(['window', 'parent']),

    // 用于分别设置不同方向上拖拽控件部分的css样式
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

    // 用于分别设置不同方向上拖拽控件部分的css类名
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