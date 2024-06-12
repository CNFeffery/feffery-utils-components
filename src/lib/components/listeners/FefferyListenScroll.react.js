import { useEffect } from 'react';
import { useScroll } from '@reactuses/core';
import PropTypes from 'prop-types';

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

    return <></>;
}

FefferyListenScroll.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 强制刷新用key值
     */
    key: PropTypes.string,

    /**
     * 设置滚动条监听目标元素id，默认为整个页面
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
     * 默认：`0`
     */
    throttle: PropTypes.number,

    /**
     * 滚动结束行为的检查时长，单位：毫秒，当`throttle>0`时，检查时长将为`throttle+idle`
     * 默认：`0`
     */
    idle: PropTypes.number,

    /**
     * 针对到达边界状态，设置像素阈值
     * 默认：`0`
     */
    offset: PropTypes.number,

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
FefferyListenScroll.defaultProps = {
}

export default FefferyListenScroll;