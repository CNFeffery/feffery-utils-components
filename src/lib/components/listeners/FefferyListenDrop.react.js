// react核心
import PropTypes from 'prop-types';
// 组件核心
import { useDrop, useRequest } from 'ahooks';

/**
 * 放置事件监听组件FefferyListenDrop
 */
const FefferyListenDrop = ({
    targetSelector,
    hoverEvent,
    setProps
}) => {

    const { run: onDragOver } = useRequest(
        (e) => {
            if (!(e.pageX === hoverEvent?.pageX && e.pageY === hoverEvent?.pageY)) {
                setProps({
                    hoverEvent: {
                        time: Date.now(),
                        pageX: e.pageX,
                        pageY: e.pageY,
                        clientX: e.clientX,
                        clientY: e.clientY,
                        screenX: e.screenX,
                        screenY: e.screenY
                    }
                })
            }
        },
        {
            throttleWait: 200,
            manual: true
        });

    useDrop(
        () => document.querySelector(targetSelector),
        {
            onDom: (content, e) => {
                setProps({
                    dropEvent: {
                        time: Date.now(),
                        data: content,
                        pageX: e.pageX,
                        pageY: e.pageY,
                        clientX: e.clientX,
                        clientY: e.clientY,
                        screenX: e.screenX,
                        screenY: e.screenY
                    },
                    isHovering: false
                })
            },
            onDragEnter: () => setProps({ isHovering: true }),
            onDragLeave: () => setProps({ isHovering: false }),
            onDragOver: onDragOver
        }
    )

    return <></>;
}

FefferyListenDrop.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 放置事件监听目标容器选择器规则字符串
     */
    targetSelector: PropTypes.string,

    /**
     * 监听最近一次基于`FefferyListenDrag`的元素拖拽放置事件
     */
    dropEvent: PropTypes.shape({
        /**
         * 事件对应时间戳
         */
        time: PropTypes.number,
        /**
         * 事件携带数据
         */
        data: PropTypes.any,
        /**
         * 以页面整体左上角为原点，记录`x`坐标
         */
        pageX: PropTypes.number,
        /**
         * 以页面整体左上角为原点，记录`y`坐标
         */
        pageY: PropTypes.number,
        /**
         * 以浏览器窗口左上角为原点，记录`x`坐标
         */
        clientX: PropTypes.number,
        /**
         * 以浏览器窗口左上角为原点，记录`y`坐标
         */
        clientY: PropTypes.number,
        /**
         * 以屏幕左上角为原点，记录`x`坐标
         */
        screenX: PropTypes.number,
        /**
         * 以屏幕左上角为原点，记录`y`坐标
         */
        screenY: PropTypes.number,
    }),

    /**
     * 监听放置事件监听目标容器是否正处于待放置鼠标悬停状态
     */
    isHovering: PropTypes.bool,

    /**
     * 监听最近一次正处于待放置鼠标悬停状态时的事件
     */
    hoverEvent: PropTypes.shape({
        /**
         * 事件对应时间戳
         */
        time: PropTypes.number,
        /**
         * 以页面整体左上角为原点，记录`x`坐标
         */
        pageX: PropTypes.number,
        /**
         * 以页面整体左上角为原点，记录`y`坐标
         */
        pageY: PropTypes.number,
        /**
         * 以浏览器窗口左上角为原点，记录`x`坐标
         */
        clientX: PropTypes.number,
        /**
         * 以浏览器窗口左上角为原点，记录`y`坐标
         */
        clientY: PropTypes.number,
        /**
         * 以屏幕左上角为原点，记录`x`坐标
         */
        screenX: PropTypes.number,
        /**
         * 以屏幕左上角为原点，记录`y`坐标
         */
        screenY: PropTypes.number,
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyListenDrop;