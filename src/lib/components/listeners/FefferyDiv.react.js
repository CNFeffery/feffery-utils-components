import React, { useEffect, useRef } from 'react';
import { useSize } from 'ahooks';

// 定义进阶div容器组件FefferyDiv
const FefferyDiv = (props) => {
    // 取得必要属性或参数
    const {
        id,
        children,
        style,
        className,
        mouseEnterCounts,
        mouseLeaveCounts,
        nClicks,
        nDoubleClicks,
        enableListenContextMenu,
        setProps,
        loading_state
    } = props;

    const ref = useRef(null);
    const size = useSize(ref);

    useEffect(() => {
        // 监听div容器尺寸变化从而刷新_width，_height属性值
        setProps({
            _width: size.width,
            _height: size.height
        });
    }, [size]);

    return <div
        id={id}
        style={style}
        className={className}
        ref={ref}
        onClick={() => setProps({ nClicks: nClicks + 1 })}
        onDoubleClick={() => setProps({ nDoubleClicks: nDoubleClicks + 1 })}
        onContextMenu={(e) => {
            if (enableListenContextMenu) {
                e.preventDefault()
                setProps({
                    contextMenuEvent: {
                        pageX: e.pageX,
                        pageY: e.pageY,
                        timestamp: Date.now()
                    }
                })
            }
        }}
        onMouseEnter={() => setProps({ mouseEnterCounts: mouseEnterCounts + 1 })}
        onMouseLeave={() => setProps({ mouseLeaveCounts: mouseLeaveCounts + 1 })}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } >
        {children}
    </ div>;
}


// 定义参数或属性
FefferyDiv.propTypes = {
    // 部件id
    id: PropTypes.string,

    children: PropTypes.node,

    style: PropTypes.object,

    className: PropTypes.string,

    // 监听容器像素宽度变化
    _width: PropTypes.number,

    // 监听容器像素高度变化
    _height: PropTypes.number,

    // 监听鼠标移入事件次数，初始化为0
    mouseEnterCounts: PropTypes.number,

    // 监听鼠标移出事件次数，初始化为0
    mouseLeaveCounts: PropTypes.number,

    // 监听单击事件次数，初始化为0
    nClicks: PropTypes.number,

    // 监听双击事件次数，初始化为0
    nDoubleClicks: PropTypes.number,

    // 设置是否针对当前div监听右键点击事件，开启后会强制关闭当前div内的默认右键菜单弹出
    // 默认为false
    enableListenContextMenu: PropTypes.bool,

    // 监听右键事件
    contextMenuEvent: PropTypes.exact({
        // 在页面中的x坐标
        pageX: PropTypes.number,
        // 在页面中的y坐标
        pageY: PropTypes.number,
        // 点击事件对应的时间戳
        timestamp: PropTypes.number
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

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
    })
};

// 设置默认参数
FefferyDiv.defaultProps = {
    mouseEnterCounts: 0,
    mouseLeaveCounts: 0,
    nClicks: 0,
    nDoubleClicks: 0,
    enableListenContextMenu: false
}

export default FefferyDiv;