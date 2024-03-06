import { useEffect } from 'react';
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
        setProps,
        loading_state
    } = props;

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
    }, [])

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
            style={style}
            className={className}
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
            onDragStop={(e, d) => setProps({ position: { x: d.x, y: d.y } })}
            onResizeStop={(e, direction, ref, delta, p) => {
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