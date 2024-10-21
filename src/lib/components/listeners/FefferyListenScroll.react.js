// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useScroll } from '@reactuses/core';

/**
 * 滚动条监听组件FefferyListenScroll
 */
const FefferyListenScroll = (props) => {
    let {
        target,
        throttle,
        idle,
        offset,
        setProps,
        loading_state
    } = props;

    const [x, y, _isScrolling, _arrivedState, _directions] = useScroll(
        () => target ? document.getElementById(target) : document,
        {
            throttle,
            idle,
            offset
        }
    );

    useEffect(() => {
        setProps({
            position: { left: x, top: y }
        })
    }, [x, y])

    useEffect(() => {
        setProps({
            isScrolling: _isScrolling
        })
    }, [_isScrolling])

    useEffect(() => {
        setProps({
            arrivedState: _arrivedState
        })
    }, [_arrivedState])

    useEffect(() => {
        setProps({
            directions: _directions
        })
    }, [_directions])

    return <></>;
}

FefferyListenScroll.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置滚动条监听目标元素`id`，默认为整个页面
     */
    target: PropTypes.string,

    /**
     * 监听目标滚动条的水平及竖直方向上的像素偏移量
     */
    position: PropTypes.object,

    /**
     * 监听目标滚动条是否正在滚动中
     */
    isScrolling: PropTypes.bool,

    /**
     * 监听目标滚动条的到达边界状态
     */
    arrivedState: PropTypes.object,

    /**
     * 监听目标滚动条的滚动方向
     */
    directions: PropTypes.object,

    /**
     * 滚动事件监听节流时长，单位：毫秒
     * 默认值：`0`
     */
    throttle: PropTypes.number,

    /**
     * 滚动结束行为的检查时长，单位：毫秒，当`throttle>0`时，检查时长将为`throttle+idle`
     * 默认值：`0`
     */
    idle: PropTypes.number,

    /**
     * 针对各个方向的到达边界状态，设置像素阈值
     */
    offset: PropTypes.shape({
        /**
         * 上顶端到达边界像素阈值
         */
        top: PropTypes.number,
        /**
         * 下底部到达边界像素阈值
         */
        bottom: PropTypes.number,
        /**
         * 左侧到达边界像素阈值
         */
        left: PropTypes.number,
        /**
         * 右侧到达边界像素阈值
         */
        right: PropTypes.number
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

FefferyListenScroll.defaultProps = {
}

export default FefferyListenScroll;