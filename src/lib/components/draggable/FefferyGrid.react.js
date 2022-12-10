import React from 'react';
import { Responsive, WidthProvider } from "react-grid-layout";
import PropTypes from 'prop-types';
import { omit } from 'ramda';
import { isNumber, isEmpty, cloneDeep } from 'lodash';
import { parseChildrenToArray, resolveChildProps } from '../utils';
import { FefferyStyle } from '../..';

const ResponsiveReactGridLayout = WidthProvider(Responsive);

// 定义可拖拽网格组件FefferyGrid
const FefferyGrid = (props) => {

    // 取得必要属性或参数
    let {
        id,
        children,
        key,
        style,
        className,
        height,
        autoSize,
        compactType,
        margin,
        containerPadding,
        rowHeight,
        isDraggable,
        isResizable,
        isBounded,
        allowOverlap,
        breakpoints,
        cols,
        layouts,
        placeholderBackground,
        placeholderOpacity,
        placeholderBorder,
        placeholderBorderRadius,
        setProps,
        loading_state
    } = props;

    children = parseChildrenToArray(children)

    const gridItems = children.map(
        (child) => {
            let childProps = resolveChildProps(child)

            return (
                <div
                    className={'feffery-grid-item-container'}
                    {...omit(
                        ['setProps', 'persistence', 'persistence_type', 'persisted_props', 'id', 'className', 'style'],
                        childProps
                    )}>
                    <button className={"feffery-grid-item-dragger"}>
                        <svg viewBox={"0 0 20 20"} style={{ width: 16, fill: '#919eab' }}>
                            <path d={"M7 2a2 2 0 1 0 .001 4.001A2 2 0 0 0 7 2zm0 6a2 2 0 1 0 .001 4.001A2 2 0 0 0 7 8zm0 6a2 2 0 1 0 .001 4.001A2 2 0 0 0 7 14zm6-8a2 2 0 1 0-.001-4.001A2 2 0 0 0 13 6zm0 2a2 2 0 1 0 .001 4.001A2 2 0 0 0 13 8zm0 6a2 2 0 1 0 .001 4.001A2 2 0 0 0 13 14z"}>
                            </path>
                        </svg>
                    </button>
                    {child}
                </div>
            );
        }
    )

    // 根据breakpoints为cols的通用模式重构数据结构
    let _cols = {};
    if (isNumber(cols)) {
        for (let key of Object.keys(breakpoints)) {
            _cols[key] = cols
        }
    }

    // 根据breakpoints为layouts的通用模式重构数据结构
    let _layouts = {};
    if (Array.isArray(layouts)) {
        for (let key of Object.keys(breakpoints)) {
            _layouts[key] = layouts
        }
    }


    return (
        <React.Fragment >
            <FefferyStyle
                rawStyle={
                    `
.react-grid-layout {
  position: relative;
  transition: height 200ms ease;
}
.react-grid-item {
  transition: all 200ms ease;
  transition-property: left, top;
  /* cursor: grab; */
}
.react-grid-item img {
  pointer-events: none;
  user-select: none;  
}
.react-grid-item.cssTransforms {
  transition-property: transform;
}
.react-grid-item.resizing {
  z-index: 1;
  will-change: width, height;
}

.react-grid-item.react-draggable-dragging {
  transition: box-shadow 0.3s ease;
  z-index: 3;
  will-change: transform;
  /* cursor: grabbing; */
  box-shadow: 0px 12px 32px 4px rgba(0, 0, 0, .04), 0px 8px 20px rgba(0, 0, 0, .08);
}

.react-grid-item.dropping {
  visibility: hidden;
}

.react-grid-item.react-grid-placeholder {
  background: ${placeholderBackground};
  opacity: ${placeholderOpacity};
  border: ${placeholderBorder};
  border-radius: ${placeholderBorderRadius};
  transition-duration: 100ms;
  z-index: 2;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  -o-user-select: none;
  user-select: none;
}

.react-grid-item > .react-resizable-handle {
  position: absolute;
  width: 20px;
  height: 20px;
}

.react-grid-item > .react-resizable-handle::after {
  content: "";
  position: absolute;
  right: 3px;
  bottom: 3px;
  width: 5px;
  height: 5px;
  border-right: 2px solid rgba(0, 0, 0, 0.4);
  border-bottom: 2px solid rgba(0, 0, 0, 0.4);
}

.react-resizable-hide > .react-resizable-handle {
  display: none;
}

.react-grid-item > .react-resizable-handle.react-resizable-handle-sw {
  bottom: 0;
  left: 0;
  cursor: sw-resize;
  transform: rotate(90deg);
}
.react-grid-item > .react-resizable-handle.react-resizable-handle-se {
  bottom: 0;
  right: 0;
  cursor: se-resize;
}
.react-grid-item > .react-resizable-handle.react-resizable-handle-nw {
  top: 0;
  left: 0;
  cursor: nw-resize;
  transform: rotate(180deg);
}
.react-grid-item > .react-resizable-handle.react-resizable-handle-ne {
  top: 0;
  right: 0;
  cursor: ne-resize;
  transform: rotate(270deg);
}
.react-grid-item > .react-resizable-handle.react-resizable-handle-w,
.react-grid-item > .react-resizable-handle.react-resizable-handle-e {
  top: 50%;
  margin-top: -10px;
  cursor: ew-resize;
}
.react-grid-item > .react-resizable-handle.react-resizable-handle-w {
  left: 0;
  transform: rotate(135deg);
}
.react-grid-item > .react-resizable-handle.react-resizable-handle-e {
  right: 0;
  transform: rotate(315deg);
}
.react-grid-item > .react-resizable-handle.react-resizable-handle-n,
.react-grid-item > .react-resizable-handle.react-resizable-handle-s {
  left: 50%;
  margin-left: -10px;
  cursor: ns-resize;
}
.react-grid-item > .react-resizable-handle.react-resizable-handle-n {
  top: 0;
  transform: rotate(225deg);
}
.react-grid-item > .react-resizable-handle.react-resizable-handle-s {
  bottom: 0;
  transform: rotate(45deg);
}
`
                }
            />
            <ResponsiveReactGridLayout
                id={id}
                key={key}
                style={style}
                className={className}
                height={height}
                autoSize={autoSize}
                compactType={compactType}
                margin={margin}
                containerPadding={containerPadding}
                rowHeight={rowHeight}
                isDraggable={isDraggable}
                isResizable={isResizable}
                isBounded={isBounded}
                allowOverlap={allowOverlap}
                breakpoints={breakpoints}
                cols={isEmpty(_cols) ? cols : _cols}
                layouts={isEmpty(_layouts) ? layouts : _layouts}
                draggableHandle={'.feffery-grid-item-dragger'}
                onLayoutChange={(e) => e && setProps({ layouts: cloneDeep(e) })}
                setProps={setProps}
                useCSSTransforms={true}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                } >{gridItems}</ResponsiveReactGridLayout>
        </React.Fragment>
    );
}


// 定义参数或属性
FefferyGrid.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 传入内部的各个FefferyGridItem元素
    children: PropTypes.node,

    // 唯一标识符，强制刷新用
    key: PropTypes.string,

    style: PropTypes.object,

    className: PropTypes.string,

    // 设置网格容器固定像素高度
    height: PropTypes.number,

    // 设置当前网格容器是否自使用内部元素而调整高度，默认为true
    autoSize: PropTypes.bool,

    // 设置网格项的自动调整约束方向，默认无约束
    compactType: PropTypes.oneOf(['vertical', 'horizontal']),

    // 用于设置当前网格容器内子元素之间的像素margin，格式：[x, y]
    // 也可以传入以断点为键的字典从而实现响应式
    margin: PropTypes.oneOfType([
        PropTypes.arrayOf(PropTypes.number),
        // 响应式
        PropTypes.objectOf(
            PropTypes.arrayOf(PropTypes.number)
        )
    ]),

    // 用于设置当前网格容器内部像素padding，格式：[x, y]
    // 也可以传入以断点为键的字典从而实现响应式
    containerPadding: PropTypes.oneOfType([
        PropTypes.arrayOf(PropTypes.number),
        // 响应式
        PropTypes.objectOf(
            PropTypes.arrayOf(PropTypes.number)
        )
    ]),

    // 用于设置网格中每行的像素高度，默认为150
    rowHeight: PropTypes.number,

    // 设置是否开启当前网格内部的拖拽行为，默认为true
    isDraggable: PropTypes.bool,

    // 设置是否开启当前网格内部的尺寸调整行为，默认为true
    isResizable: PropTypes.bool,

    // 设置是否限制当前网格内部的拖拽行为仅限于内部，默认为false
    isBounded: PropTypes.bool,

    // 设置是否允许相互压盖，默认为false
    allowOverlap: PropTypes.bool,

    // 用于自定义断点及其对应的像素值映射对象
    // 默认为{lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0}
    breakpoints: PropTypes.objectOf(PropTypes.number),

    // 与breakpoints对应，用于设置不同断点下网格系统的列数
    // 默认为{lg: 12, md: 10, sm: 6, xs: 4, xxs: 2}
    cols: PropTypes.oneOfType([
        PropTypes.objectOf(PropTypes.number),
        // 通用模式
        PropTypes.number
    ]),

    // 用于定义不同断点下的各个网格项布局相关参数
    layouts: PropTypes.oneOfType([
        PropTypes.objectOf(
            PropTypes.arrayOf(
                PropTypes.exact({
                    // 对应当前网格项的key值
                    i: PropTypes.string,
                    // 对应当前网格项的锚点x单位坐标
                    x: PropTypes.number,
                    // 对应当前网格项的锚点y单位坐标
                    y: PropTypes.number,
                    // 对应当前网格项的网格单位宽度
                    w: PropTypes.number,
                    // 对应当前网格项的网格单位高度
                    h: PropTypes.number,
                    // 对应当前网格项的最小网格单位宽度，默认为0
                    minW: PropTypes.number,
                    // 对应当前网格项的最大网格单位宽度，默认无限制
                    maxW: PropTypes.number,
                    // 对应当前网格项的最小网格单位高度，默认为0
                    minH: PropTypes.number,
                    // 对应当前网格项的最大网格单位高度，默认无限制
                    maxH: PropTypes.number,
                    // 设置当前网格项是否静态，默认为false
                    static: PropTypes.bool,
                    // 设置当前网格项是否允许被拖拽，默认为true
                    isDraggable: PropTypes.bool,
                    // 设置当前网格项是否允许被调整尺寸，默认为true
                    isResizable: PropTypes.bool,
                    // 设置是否为当前网格项施加边界约束，默认为false
                    isBounded: PropTypes.bool,
                    moved: PropTypes.any
                })
            )
        ),
        // 通用模式
        PropTypes.arrayOf(
            PropTypes.exact({
                // 对应当前网格项的key值
                i: PropTypes.string,
                // 对应当前网格项的锚点x单位坐标
                x: PropTypes.number,
                // 对应当前网格项的锚点y单位坐标
                y: PropTypes.number,
                // 对应当前网格项的网格单位宽度
                w: PropTypes.number,
                // 对应当前网格项的网格单位高度
                h: PropTypes.number,
                // 对应当前网格项的最小网格单位宽度，默认为0
                minW: PropTypes.number,
                // 对应当前网格项的最大网格单位宽度，默认无限制
                maxW: PropTypes.number,
                // 对应当前网格项的最小网格单位高度，默认为0
                minH: PropTypes.number,
                // 对应当前网格项的最大网格单位高度，默认无限制
                maxH: PropTypes.number,
                // 设置当前网格项是否静态，默认为false
                static: PropTypes.bool,
                // 设置当前网格项是否允许被拖拽，默认为true
                isDraggable: PropTypes.bool,
                // 设置当前网格项是否允许被调整尺寸，默认为true
                isResizable: PropTypes.bool,
                // 设置是否为当前网格项施加边界约束，默认为false
                isBounded: PropTypes.bool,
                moved: PropTypes.any
            })
        )
    ]),

    // 自定义样式相关快捷样式参数
    // 自定义拖拽预览占位的background属性，默认为'#99a3ab'
    placeholderBackground: PropTypes.string,

    // 自定义拖拽预览占位的opacity属性，默认为1
    placeholderOpacity: PropTypes.number,

    // 自定义拖拽预览占位的border属性，默认为'none'
    placeholderBorder: PropTypes.string,

    // 自定义拖拽预览占位的border-radius属性，默认为'0px'
    placeholderBorderRadius: PropTypes.string,

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
    compactType: 'vertical'
}

export default React.memo(FefferyGrid);