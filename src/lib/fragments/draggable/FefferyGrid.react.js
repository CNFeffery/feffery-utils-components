import React from 'react';
import { Responsive, WidthProvider } from "react-grid-layout";
import { propTypes, defaultProps } from '../../components/draggable/FefferyGrid.react';
import { omit } from 'ramda';
import { isNumber, isEmpty, cloneDeep } from 'lodash';
import { parseChildrenToArray, resolveChildProps } from '../../components/utils';
import FefferyStyle from '../../components/FefferyStyle.react';

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
    debug,
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
        onLayoutChange={(e) => {
          if (e) {
            if (debug) {
              console.log('layouts: ', e)
            }
            setProps({ layouts: cloneDeep(e) })
          }
        }}
        setProps={setProps}
        useCSSTransforms={true}
        data-dash-is-loading={
          (loading_state && loading_state.is_loading) || undefined
        } >{gridItems}</ResponsiveReactGridLayout>
    </React.Fragment>
  );
}

export default FefferyGrid;

FefferyGrid.defaultProps = defaultProps;
FefferyGrid.propTypes = propTypes;