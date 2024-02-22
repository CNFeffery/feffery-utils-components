import { useEffect, useState, useRef } from 'react';
import { useDraggable } from '@reactuses/core';
import { useSize, useHover, useFocusWithin } from 'ahooks';
import PropTypes from 'prop-types';

const DragLine = (props) => {
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

// 定义可拖拽组件FefferyDraggable
const FefferyDraggable = (props) => {
    // 取得必要属性或参数
    const {
        id,
        key,
        style,
        className,
        children,
        draggable,
        showDragLine,
        dragLineColors,
        focusWithinStyle,
        initialX,
        initialY,
        x,
        y,
        setProps,
        loading_state
    } = props;

    const ref = useRef(null);
    const handleRef = useRef(null);

    const [initialValue, setInitialValue] = useState({ x: initialX, y: initialY });

    const [_x, _y, isDragging] = useDraggable(ref, {
        initialValue,
        handle: handleRef
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
                position: 'fixed',
                left: x || initialX,
                top: y || initialY,
                // 根据是否处于聚焦状态，进行聚焦样式的添加
                ...(_isFocusWithin ? focusWithinStyle : {}),
            }}
            className={className}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }>
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
                    <DragLine x={_x} y={_y} width={size.width} height={size.height} dragLineColors={dragLineColors} /> :
                    null
            }
        </div>
    );
}

// 定义参数或属性
FefferyDraggable.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 强制刷新用
     */
    key: PropTypes.string,

    /**
     * 当前可拖拽组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前可拖拽组件css类名
     */
    className: PropTypes.string,

    /**
     * 设置内部元素
     */
    children: PropTypes.node,

    /**
     * 是否开启可拖拽
     * 默认：true
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
     * 默认：false
     */
    showDragLine: PropTypes.bool,

    /**
     * 设置拖拽辅助线颜色
     * 默认：['#d9d9d9', '#8c8c8c']
     */
    dragLineColors: PropTypes.arrayOf(PropTypes.string),

    /**
     * 设置聚焦状态下的额外css样式
     */
    focusWithinStyle: PropTypes.object,

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
FefferyDraggable.defaultProps = {
    draggable: true,
    showDragLine: false,
    dragLineColors: ['#d9d9d9', '#8c8c8c'],
    focusWithinStyle: {
        boxShadow: 'rgba(0, 0, 0, 0.08) 0px 6px 16px -8px, rgba(0, 0, 0, 0.05) 0px 9px 28px, rgba(0, 0, 0, 0.03) 0px 12px 48px 16px'
    }
}

export default FefferyDraggable;