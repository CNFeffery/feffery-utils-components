// react核心
import { useEffect, useState, useRef } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useDraggable } from '@reactuses/core';
// 辅助库
import { useSize, useHover, useFocusWithin } from 'ahooks';
import { useLoading } from '../utils';

const DragLine = (props) => {
    // 局部容器模式
    if (props.boundsRef?.current) {
        // 获取局部容器的位置及尺寸信息
        let boundsRect = props.boundsRef.current.getBoundingClientRect();
        return (
            <>
                {/* 顶端线 */}
                <div style={{ height: 1, borderTop: `1px dashed ${props.dragLineColors[0]}`, position: 'fixed', boxSizing: 'border-box', left: 0, right: 0, top: props.y + boundsRect.top }} />
                {/* 底端线 */}
                <div style={{ height: 1, borderBottom: `1px dashed ${props.dragLineColors[0]}`, position: 'fixed', boxSizing: 'border-box', left: 0, right: 0, top: props.y + props.height - 1 + boundsRect.top }} />
                {/* 左侧线 */}
                <div style={{ width: 1, borderLeft: `1px dashed ${props.dragLineColors[0]}`, position: 'fixed', boxSizing: 'border-box', top: 0, bottom: 0, left: props.x + boundsRect.left }} />
                {/* 右侧线 */}
                <div style={{ width: 1, borderRight: `1px dashed ${props.dragLineColors[0]}`, position: 'fixed', boxSizing: 'border-box', top: 0, bottom: 0, left: props.x + props.width + boundsRect.left }} />
                {/* 中心水平线 */}
                <div style={{ height: 1, borderTop: `1px dashed ${props.dragLineColors[1]}`, position: 'fixed', boxSizing: 'border-box', left: 0, right: 0, top: props.y + 0.5 * props.height + boundsRect.top }} />
                {/* 中心垂直线 */}
                <div style={{ width: 1, borderLeft: `1px dashed ${props.dragLineColors[1]}`, position: 'fixed', boxSizing: 'border-box', top: 0, bottom: 0, left: props.x + 0.5 * props.width + boundsRect.left }} />
            </>
        );
    }
    return (
        <>
            {/* 顶端线 */}
            <div style={{ height: 1, borderTop: `1px dashed ${props.dragLineColors[0]}`, position: 'fixed', boxSizing: 'border-box', left: 0, right: 0, top: props.y }} />
            {/* 底端线 */}
            <div style={{ height: 1, borderBottom: `1px dashed ${props.dragLineColors[0]}`, position: 'fixed', boxSizing: 'border-box', left: 0, right: 0, top: props.y + props.height - 1 }} />
            {/* 左侧线 */}
            <div style={{ width: 1, borderLeft: `1px dashed ${props.dragLineColors[0]}`, position: 'fixed', boxSizing: 'border-box', top: 0, bottom: 0, left: props.x }} />
            {/* 右侧线 */}
            <div style={{ width: 1, borderRight: `1px dashed ${props.dragLineColors[0]}`, position: 'fixed', boxSizing: 'border-box', top: 0, bottom: 0, left: props.x + props.width }} />
            {/* 中心水平线 */}
            <div style={{ height: 1, borderTop: `1px dashed ${props.dragLineColors[1]}`, position: 'fixed', boxSizing: 'border-box', left: 0, right: 0, top: props.y + 0.5 * props.height }} />
            {/* 中心垂直线 */}
            <div style={{ width: 1, borderLeft: `1px dashed ${props.dragLineColors[1]}`, position: 'fixed', boxSizing: 'border-box', top: 0, bottom: 0, left: props.x + 0.5 * props.width }} />
        </>
    );
}

/**
 * 可拖拽组件FefferyDraggable
 */
const FefferyDraggable = ({
    id,
    key,
    style,
    className,
    children,
    draggable = true,
    showDragLine = false,
    dragLineColors = ['#d9d9d9', '#8c8c8c'],
    focusWithinStyle = {
        boxShadow: 'rgba(0, 0, 0, 0.08) 0px 6px 16px -8px, rgba(0, 0, 0, 0.05) 0px 9px 28px, rgba(0, 0, 0, 0.03) 0px 12px 48px 16px'
    },
    boundsSelector,
    initialX,
    initialY,
    x,
    y,
    setProps
}) => {

    const ref = useRef(null);
    const handleRef = useRef(null);
    const boundsRef = useRef(null);

    useEffect(() => {
        if (boundsSelector) {
            boundsRef.current = document.querySelector(boundsSelector);
        }
    }, [boundsSelector])

    const [initialValue, setInitialValue] = useState({ x: initialX, y: initialY });

    const [_x, _y, isDragging] = useDraggable(ref, {
        initialValue,
        handle: handleRef,
        containerElement: boundsRef
    });
    const size = useSize(ref);
    const isHovering = useHover(ref);
    const _isFocusWithin = useFocusWithin(ref);

    // 同步最新的_x，_y值
    useEffect(() => {
        if (draggable) {
            setProps({
                x: _x,
                y: _y
            })
        }
    }, [_x, _y])

    // 同步最新的聚焦状态
    useEffect(() => {
        setProps({
            isFocusWithin: _isFocusWithin
        })
    }, [_isFocusWithin])

    return (
        <div ref={ref}
            id={id}
            key={key}
            style={{
                zIndex: 999,
                ...style,
                position: boundsSelector ? 'absolute' : 'fixed',
                left: x === 0 ? x : (x || initialX),
                top: y === 0 ? y : (y || initialY),
                // 根据是否处于聚焦状态，进行聚焦样式的添加
                ...(_isFocusWithin ? focusWithinStyle : {}),
            }}
            className={className}
            data-dash-is-loading={useLoading()}>
            <button ref={handleRef}
                style={{
                    position: 'absolute',
                    top: 0,
                    right: 0,
                    transform: 'translateX(calc(100% + 5px))',
                    cursor: draggable ? 'all-scroll' : 'no-drop'
                }}
                className={'feffery-draggable-dragger'}>
                <svg viewBox={"0 0 20 20"} style={{ width: 16, fill: '#919eab' }}>
                    <path d={"M7 2a2 2 0 1 0 .001 4.001A2 2 0 0 0 7 2zm0 6a2 2 0 1 0 .001 4.001A2 2 0 0 0 7 8zm0 6a2 2 0 1 0 .001 4.001A2 2 0 0 0 7 14zm6-8a2 2 0 1 0-.001-4.001A2 2 0 0 0 13 6zm0 2a2 2 0 1 0 .001 4.001A2 2 0 0 0 13 8zm0 6a2 2 0 1 0 .001 4.001A2 2 0 0 0 13 14z"}>
                    </path>
                </svg>
            </button>
            {children}
            {
                (showDragLine && draggable && (isDragging || isHovering)) ?
                    <DragLine x={_x} y={_y} width={size.width} height={size.height} dragLineColors={dragLineColors} boundsRef={boundsRef} /> :
                    null
            }
        </div>
    );
}

FefferyDraggable.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，内嵌元素
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
     * 是否开启可拖拽
     * 默认值：`true`
     */
    draggable: PropTypes.bool,

    /**
     * 必填，设置初始状态下当前可拖拽组件左上角距离页面顶端的像素距离
     */
    initialX: PropTypes.number.isRequired,

    /**
     * 必填，设置初始状态下当前可拖拽组件左上角距离页面左侧的像素距离
     */
    initialY: PropTypes.number.isRequired,

    /**
     * 设置是否在拖拽时显示相关辅助线
     * 默认值：`false`
     */
    showDragLine: PropTypes.bool,

    /**
     * 设置拖拽辅助线颜色
     * 默认值：`['#d9d9d9', '#8c8c8c']`
     */
    dragLineColors: PropTypes.arrayOf(PropTypes.string),

    /**
     * 设置聚焦状态下的额外`css`样式
     */
    focusWithinStyle: PropTypes.object,

    /**
     * 设置可拖拽范围边界容器对应的`css`选择器，设置后拖拽将基于*相对-绝对布局*被限制在边界容器内部
     */
    boundsSelector: PropTypes.string,

    /**
     * 只读，用于监听当前可拖拽组件左上角距离页面顶端的像素距离
     */
    x: PropTypes.number,

    /**
     * 只读，用于监听当前可拖拽组件左上角距离页面左侧的像素距离
     */
    y: PropTypes.number,

    /**
     * 只读，用于监听当前可拖拽组件是否处于聚焦状态
     */
    isFocusWithin: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyDraggable;