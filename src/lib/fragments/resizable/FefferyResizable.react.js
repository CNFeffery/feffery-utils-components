import { useEffect } from 'react';
import { Resizable } from 're-resizable';
import { propTypes, defaultProps } from '../../components/resizable/FefferyResizable.react';
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
        size,
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

    useEffect(() => {
        // size缺省且defaultSize有效时，进行赋值
        if (!size && defaultSize) {
            setProps({
                size: defaultSize
            })
        }
    }, [])

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
            size={size}
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
            onResizeStop={(e, direction, ref, d) => {
                if (size) {
                    setProps({
                        size: {
                            width: size.width + d.width,
                            height: size.height + d.height,
                        }
                    });
                }
            }}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >
            {children}
        </Resizable>
    );
}

export default FefferyResizable;

FefferyResizable.defaultProps = defaultProps;
FefferyResizable.propTypes = propTypes;