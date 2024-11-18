import React from 'react';
import PropTypes from 'prop-types';
import { animateScroll as scroll, scroller } from 'react-scroll'

/**
 * 滚动操作组件FefferyScroll
 */
const FefferyScroll = (props) => {
    // 取得必要属性或参数
    let {
        id,
        scrollMode,
        executeScroll,
        scrollTopOffset,
        scrollRelativeOffset,
        scrollTargetId,
        duration,
        smooth,
        delay,
        containerId,
        offset,
        setProps,
        loading_state
    } = props;

    if (executeScroll && scrollMode) {
        if (scrollMode === 'to-top') {
            scroll.scrollToTop({
                duration,
                smooth,
                delay,
                containerId,
                offset
            })
        } else if (scrollMode === 'to-bottom') {
            scroll.scrollToBottom({
                duration,
                smooth,
                delay,
                containerId,
                offset
            })
        } else if (scrollMode === 'top-offset') {
            scroll.scrollTo(
                scrollTopOffset,
                {
                    duration,
                    smooth,
                    delay,
                    containerId,
                    offset
                }
            )
        } else if (scrollMode === 'relative-offset') {
            scroll.scrollMore(
                scrollRelativeOffset,
                {
                    duration,
                    smooth,
                    delay,
                    containerId,
                    offset
                }
            )
        } else {
            scroller.scrollTo(
                scrollTargetId,
                {
                    duration,
                    smooth,
                    delay,
                    containerId,
                    offset
                }
            )
        }

        // 重置executeScroll为false
        setProps({
            executeScroll: false
        })
    }

    return <></>;
}

FefferyScroll.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置页面滚动模式，可选的有`'to-top'`、`'to-bottom'`、`'top-offset'`、`'relative-offset'`、`'target'`
     * 默认值：`'to-top'`
     */
    scrollMode: PropTypes.oneOf([
        'to-top', 'to-bottom', 'top-offset', 'relative-offset', 'target'
    ]).isRequired,

    /**
     * 用于指示是否进行滚动操作，在回调中设置`executeScroll`参数Output为`true`从而触发新一次滚动，每次由`executeScroll=true`触发的滚动完成后，`executeScroll`会自动重置为`false`
     * 默认值：`false`
     */
    executeScroll: PropTypes.bool,

    /**
     * 当`scrollMode='top-offset'`时，用于设置滚动终点距离页面顶端的像素
     */
    scrollTopOffset: PropTypes.number,

    /**
     * 当`scrollMode='relative-offset'`时，用于设置相对滚动的像素距离，负数则为向上滚动
     */
    scrollRelativeOffset: PropTypes.number,

    /**
     * 当`scrollMode='target'`时，用于设置滚动目标元素的id信息
     */
    scrollTargetId: PropTypes.string,

    /**
     * 用于设置滚动过程耗时（单位：毫秒）
     * 默认值：`500`
     */
    duration: PropTypes.number,

    /**
     * 用于设置滚动过程动画模式
     * 默认值：true
     */
    smooth: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.oneOf([
            'linear',
            'easeInQuad',
            'easeOutQuad',
            'easeInOutQuad',
            'easeInCubic',
            'easeOutCubic',
            'easeInOutCubic',
            'easeInQuart',
            'easeOutQuart',
            'easeInOutQuart',
            'easeInQuint',
            'easeOutQuint',
            'easeInOutQuint'
        ])
    ]),

    /**
     * 用于设置滚动延时（单位：毫秒）
     * 默认值：0
     */
    delay: PropTypes.number,

    /**
     * 当滚动目标位于局部滚动条内时，用于设置局部滚动条所在的容器id信息
     */
    containerId: PropTypes.string,

    /**
     * 设置滚动过程的额外偏移像素距离
     */
    offset: PropTypes.number,

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
    setProps: PropTypes.func
};

// 设置默认参数
FefferyScroll.defaultProps = {
    executeScroll: false,
    scrollMode: 'to-top',
    duration: 500,
    delay: 0,
    smooth: true
}

export default FefferyScroll;