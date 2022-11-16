import React, { useEffect, useRef } from 'react';
import { useCss } from 'react-use';
import { isString } from 'lodash';
import PropTypes from 'prop-types';
import { useSize, useRequest, useHover, useClickAway } from 'ahooks';
import './styles.css'

// 定义进阶div容器组件FefferyDiv
const FefferyDiv = (props) => {
    // 取得必要属性或参数
    let {
        id,
        key,
        children,
        style,
        className,
        mouseEnterCount,
        mouseLeaveCount,
        nClicks,
        nDoubleClicks,
        enableListenContextMenu,
        debounceWait,
        clickAwayCount,
        appendChild,
        insertChild,
        replaceChild,
        deleteChildIndex,
        shadow,
        enableClickAway,
        setProps,
        loading_state
    } = props;

    const ref = useRef(null);
    const size = useSize(ref);
    const _isHovering = useHover(ref);

    // 快捷children数组增删操作
    useEffect(() => {
        if (children && appendChild) {
            setProps({
                children: children.concat(appendChild),
                appendChild: null // 重置
            })
        }
    }, [appendChild])

    useEffect(() => {
        if (children && insertChild && insertChild.index && insertChild.element) {
            setProps({
                children: children.slice(0, insertChild.index)
                    .concat([insertChild.element])
                    .concat(children.slice(insertChild.index)),
                insertChild: null // 重置
            })
        }
    }, [insertChild])

    useEffect(() => {
        if (children && replaceChild && replaceChild.index && replaceChild.element) {
            children[replaceChild.index] = replaceChild.element
            setProps({
                children: children,
                replaceChild: null // 重置
            })
        }
    }, [replaceChild])

    useEffect(() => {
        if (children && (deleteChildIndex || deleteChildIndex === 0)) {
            setProps({
                children: children.filter((_, i) => i !== deleteChildIndex),
                deleteChildIndex: null // 重置
            })
        }
    }, [deleteChildIndex])

    // 防抖更新容器尺寸
    const { run: updateWidthHeight } = useRequest(
        (e) => {
            if (e) {
                // 监听div容器尺寸变化从而刷新_width，_height属性值
                setProps({
                    _width: size.width,
                    _height: size.height
                })
            }
        },
        {
            debounceWait: debounceWait,
            manual: true
        }
    )

    // 当size变化时进行_width、_height的更新
    useEffect(() => {
        updateWidthHeight(size)
    }, [size]);

    // 当_isHovering变化时进isHovering状态的更新
    useEffect(() => {
        setProps({
            isHovering: _isHovering
        })
    }, [_isHovering])

    // 监听元素外点击事件
    if (enableClickAway) {
        useClickAway(() => {
            setProps({ clickAwayCount: clickAwayCount + 1 })
        }, ref);
    }

    // 根据shadow参数预处理className
    if (shadow === 'hover-shadow') {
        className = className ? `${className} feffery-div-hover-shadow` : 'feffery-div-hover-shadow'
    } else if (shadow === 'always-shadow') {
        className = className ? `${className} feffery-div-always-shadow` : 'feffery-div-always-shadow'
    }

    return <div
        id={id}
        key={key}
        style={style}
        className={
            isString(className) ?
                className :
                (className ? useCss(className) : undefined)
        }
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
                        clientX: e.clientX,
                        clientY: e.clientY,
                        screenX: e.screenX,
                        screenY: e.screenY,
                        timestamp: Date.now()
                    }
                })
            }
        }}
        onMouseEnter={() => setProps({ mouseEnterCount: mouseEnterCount + 1 })}
        onMouseLeave={() => setProps({ mouseLeaveCount: mouseLeaveCount + 1 })}
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

    key: PropTypes.string,

    children: PropTypes.node,

    // 快捷children数组增删参数，在有效值传入促使组件更新后会自动重置为undefined
    // 用于快捷向children数组末尾追加新元素
    appendChild: PropTypes.node,

    // 用于快捷在原children数组第index个位置插入新元素
    insertChild: PropTypes.exact({
        // 要插入的位序
        index: PropTypes.number,
        // 要插入的元素
        element: PropTypes.node
    }),

    // 用于快捷对children数组第index个位置的元素进行替换
    replaceChild: PropTypes.exact({
        // 要替换元素的位序
        index: PropTypes.number,
        // 要替换的新元素
        element: PropTypes.node
    }),

    // 用于快捷删除原children第index个位置的元素
    deleteChildIndex: PropTypes.number,

    style: PropTypes.object,

    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    // 监听容器像素宽度变化
    _width: PropTypes.number,

    // 监听容器像素高度变化
    _height: PropTypes.number,

    // 设置针对尺寸变化事件的防抖等待时间（单位：毫秒），默认为150
    debounceWait: PropTypes.number,

    // 监听鼠标移入事件次数，初始化为0
    mouseEnterCount: PropTypes.number,

    // 监听鼠标移出事件次数，初始化为0
    mouseLeaveCount: PropTypes.number,

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

    // 监听当前元素是否被鼠标悬浮
    isHovering: PropTypes.bool,

    // 设置是否启用元素外点击事件监听，当页面中有大量FefferyDiv元素时，建议不要开启此特性，会导致明显的性能问题
    // 默认为false
    enableClickAway: PropTypes.bool,

    // 监听元素外点击事件发生次数，默认为0
    clickAwayCount: PropTypes.number,

    // 设置当前容器的快捷阴影效果，可选的有'no-shadow'、'hover-shadow'、'always-shadow'
    // 默认为'no-shadow'
    shadow: PropTypes.oneOf(['no-shadow', 'hover-shadow', 'always-shadow']),

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
    mouseEnterCount: 0,
    mouseLeaveCount: 0,
    nClicks: 0,
    nDoubleClicks: 0,
    enableListenContextMenu: false,
    debounceWait: 150,
    clickAwayCount: 0,
    shadow: 'no-shadow',
    enableClickAway: false
}

export default React.memo(FefferyDiv);