import { useDrop } from 'ahooks';
import PropTypes from 'prop-types';

/**
 * 放置事件监听组件FefferyListenDrop
 */
const FefferyListenDrop = (props) => {
    const {
        targetSelector,
        setProps,
        loading_state
    } = props;

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
                    }
                })
            },
            onDragEnter: () => setProps({ isHovering: true }),
            onDragLeave: () => setProps({ isHovering: false }),
        }
    )

    return <></>;
}

FefferyListenDrop.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 放置事件监听目标容器选择器规则字符串
     */
    targetSelector: PropTypes.string,

    /**
     * 监听最近一次基于FefferyListenDrag的元素拖拽放置事件
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
         * 以页面整体左上角为原点，记录x坐标
         */
        pageX: PropTypes.number,
        /**
         * 以页面整体左上角为原点，记录y坐标
         */
        pageY: PropTypes.number,
        /**
         * 以浏览器窗口左上角为原点，记录x坐标
         */
        clientX: PropTypes.number,
        /**
         * 以浏览器窗口左上角为原点，记录y坐标
         */
        clientY: PropTypes.number,
        /**
         * 以屏幕左上角为原点，记录x坐标
         */
        screenX: PropTypes.number,
        /**
         * 以屏幕左上角为原点，记录y坐标
         */
        screenY: PropTypes.number,
    }),

    /**
     * 监听放置事件监听目标容器是否正处于待放置鼠标悬停状态
     */
    isHovering: PropTypes.bool,

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
FefferyListenDrop.defaultProps = {
}

export default FefferyListenDrop;