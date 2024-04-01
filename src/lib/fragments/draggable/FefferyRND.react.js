import { useEffect, useState } from 'react';
import { Rnd } from 'react-rnd';
import { propTypes, defaultProps } from '../../components/draggable/FefferyRND.react';
import { clone } from 'lodash';

/**
 * 尺寸可调可拖拽组件FefferyRND
 */
const FefferyRND = (props) => {
    const {
        id,
        style,
        className,
        children,
        defaultState,
        size,
        position,
        minWidth,
        minHeight,
        maxWidth,
        maxHeight,
        resizeGrid,
        dragGrid,
        lockAspectRatio,
        lockAspectRatioExtraWidth,
        lockAspectRatioExtraHeight,
        direction,
        disableDragging,
        dragAxis,
        bounds,
        selected,
        selectedStyle,
        selectedClassName,
        setProps,
        loading_state
    } = props;

    // 记录拖拽或尺寸调整结束事件时间戳
    const [dragOrResizeStopTimestamp, setDragOrResizeStopTimestamp] = useState(0);

    useEffect(() => {
        // size缺省且defaultState.width，defaultState.height有效时，进行赋值
        if (!size && defaultState.width && defaultState.height) {
            setProps({
                size: {
                    width: defaultState.width,
                    height: defaultState.height
                }
            })
        }
        // position缺省且defaultState.x，defaultState.y有效时，进行赋值
        if (!position && (defaultState.x || defaultState.x === 0) && (defaultState.y || defaultState.y === 0)) {
            setProps({
                position: {
                    x: defaultState.x,
                    y: defaultState.y
                }
            })
        }
    }, [size,position])

    // 初始化enableResizing
    const defaultEnableResizing = {
        top: false,
        right: false,
        bottom: false,
        left: false,
        topRight: false,
        bottomRight: false,
        bottomLeft: false,
        topLeft: false
    }

    const enableResizing = clone(defaultEnableResizing);

    // 根据direction更新enableResizing
    for (let d of direction) {
        enableResizing[d] = true
    }

    return (
        <Rnd id={id}
            style={{ ...style, ...(selected ? selectedStyle : {}) }}
            className={(selected && selectedClassName) ? className + ' ' + selectedClassName : className}
            default={defaultState}
            size={size}
            position={position}
            minWidth={minWidth}
            minHeight={minHeight}
            maxWidth={maxWidth}
            maxHeight={maxHeight}
            resizeGrid={resizeGrid}
            dragGrid={dragGrid}
            lockAspectRatio={lockAspectRatio}
            lockAspectRatioExtraWidth={lockAspectRatioExtraWidth}
            lockAspectRatioExtraHeight={lockAspectRatioExtraHeight}
            enableResizing={enableResizing}
            disableDragging={disableDragging}
            dragAxis={dragAxis}
            bounds={bounds}
            onDragStop={(e, d) => {
                // 若本次拖拽事件导致了有效偏移，则更新拖拽结束事件时间戳
                if (position && (position.x !== d.x || position.y !== d.y)) {
                    setDragOrResizeStopTimestamp(new Date().getTime());
                }
                setProps({ position: { x: d.x, y: d.y } })
            }}
            onResizeStop={(e, direction, ref, delta, p) => {
                setDragOrResizeStopTimestamp(new Date().getTime());
                setProps({
                    size: {
                        width: ref.style.width,
                        height: ref.style.height
                    },
                    position: {
                        x: p.x,
                        y: p.y
                    }
                })
            }}
            onClick={() => {
                // 若距离最近一次拖拽结束事件时间戳大于200ms，则切换选中状态
                // 从而避免拖拽导致的选中误操作
                if (new Date().getTime() - dragOrResizeStopTimestamp >= 200) {
                    setProps({ selected: !selected })
                }
            }}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }>
            {children}
        </Rnd>
    );
}

export default FefferyRND;

FefferyRND.defaultProps = defaultProps;
FefferyRND.propTypes = propTypes;
